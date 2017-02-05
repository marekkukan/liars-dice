#!/usr/bin/env python3


import os
import sys
import time
import random
from bid import Bid


def l2s(l):
    return ' '.join([str(x) for x in l])

def gen_roll(k):
    return [random.randint(1, 6) for _ in range(k)]


class Player:

    fds = []

    @staticmethod
    def create_pipe():
        pipe = os.pipe()
        Player.fds.extend(list(pipe))
        return pipe

    def __init__(self, path):
        self._path = path
        self._pipe_out = self.create_pipe()
        self._pipe_in = self.create_pipe()
        self._fo = os.fdopen(self._pipe_in[0])
        self.n_dice = 6
        self.hidden_dice = []
        self.revealed_dice = []

    def __str__(self):
        return str(self._path)

    def run(self):
        pid = os.fork()
        if pid == 0:
            os.dup2(self._pipe_in[1], 1)
            os.dup2(self._pipe_out[0], 0)
            for fd in Player.fds:
                try:
                    os.close(fd)
                except OSError:
                    pass
            os.execl(self._path, 'player')
            sys.stderr.write("exec failed\n")
            os._exit(1)
        else:
            os.close(self._pipe_in[1])
            os.close(self._pipe_out[0])
            self._pid = pid

    def write(self, msg):
        print('manager -> ' + str(self) + ':\t' + msg)
        os.write(self._pipe_out[1], (msg+'\n').encode())

    def read(self):
        msg = self._fo.readline().rstrip()
        print(str(self) + ' -> manager:\t' + msg)
        return msg

    def roll(self):
        self.hidden_dice = gen_roll(self.n_dice - len(self.revealed_dice))

    def play(self):
        self.write('PLAY ' + l2s(self.hidden_dice))
        return self.read()


class Game:

    def __init__(self, players):
        self.players = players
        self.cpi = 0
        self.cp = players[self.cpi]
        self.finished = False
        self.bid = Bid(0, 6)

    def shift_cp(self):
        # self.cpi = (self.cpi + 1) % len(self.players)
        self.cpi = 1 - self.cpi
        self.cp = self.players[self.cpi]

    def opp(self):
        return self.players[1 - self.cpi]

    def run(self):
        for p in self.players:
            p.write('NEW_GAME')
            p.n_dice = 6
            p.hidden_dice = []
            p.revealed_dice = []
        while not self.finished:
            self.play_round()

    def play_round(self):
        self.finished_round = False
        self.bid = Bid(0, 6)
        for i in range(len(self.players)):
            self.players[i].write('NEW_ROUND ' + l2s([p.n_dice for p in self.players[i:] + self.players[:i]]))
            self.players[i].hidden_dice = []
            self.players[i].revealed_dice = []
            self.players[i].roll()
        self.eval_move(self.cp.play(), challenge_possible=False)
        while not self.finished and not self.finished_round:
            self.shift_cp()
            self.eval_move(self.cp.play())

    def eval_move(self, move, challenge_possible=True, reveal_possible=True):
        parts = move.split(' ')
        if parts[0] == 'BID':
            try:
                bid = Bid(int(parts[1]), int(parts[2]))
                assert 1 <= bid.value <= 6
                assert bid > self.bid
            except:
                self.invalid_move(move)
                return
            self.bid = bid
            self.opp().write('OPPONENT_BIDS ' + str(bid))
        elif parts[0] == 'REVEAL':
            try:
                assert reveal_possible
                dice = (int(x) for x in parts[1:])
                for die in dice:
                    self.cp.hidden_dice.remove(die)
                    self.cp.revealed_dice.append(die)
            except:
                self.invalid_move(move)
                return
            self.opp().write('OPPONENT_REVEALS ' + ' '.join(parts[1:]))
            self.cp.roll()
            self.eval_move(self.cp.play(), False, False)
        elif parts[0] == 'CHALLENGE':
            self.finished_round = True
            if not challenge_possible:
                self.invalid_move(move)
                return
            self.opp().write('OPPONENT_CHALLENGES')
            all_dice = []
            for p in self.players:
                all_dice.extend(p.revealed_dice)
                all_dice.extend(p.hidden_dice)
            diff = self.bid.count - sum([1 for die in all_dice if die == self.bid.value or die == 1])
            if diff < 0:
                self.cp.n_dice += diff
            elif diff > 0:
                self.opp().n_dice -= diff
                self.shift_cp()
            else:
                self.cp.n_dice -= 1
                self.opp().n_dice += 1
            if self.cp.n_dice <= 0:
                self.end(self.opp())
            elif self.opp().n_dice <= 0:
                self.end(self.cp)
        else:
            self.invalid_move(move)

    def end(self, winner):
        self.finished = True
        winner.write('YOU_WIN')
        for p in self.players:
            if p == winner:
                continue
            p.write('YOU_LOSE')
        print('manager: the winner is: ' + str(winner))

    def invalid_move(self, move):
        print('manager: invalid move by player ' + str(self.cpi) + ': ' + move)
        self.end(self.opp())


if __name__ == '__main__':
    players = [Player(sys.argv[1]), Player(sys.argv[2])]
    for p in players:
        p.run()
    game = Game(players)
    game.run()
    print('the end.')

