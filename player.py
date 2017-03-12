import os
import sys
import random
import time


class Player:

    fds = []

    @staticmethod
    def create_pipe():
        pipe = os.pipe()
        Player.fds.extend(list(pipe))
        return pipe

    def __init__(self, path, arg=""):
        self._path = path
        self._pipe_out = self.create_pipe()
        self._pipe_in = self.create_pipe()
        self._fo = os.fdopen(self._pipe_in[0])
        self.n_dice = 6
        self.hidden_dice = []
        self.revealed_dice = []
        self.id = None
        self.arg = arg
        self.n_wins = 0

    def __str__(self):
        return self._path + '[' + str(self.id) + ']'

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
            os.execl(self._path, '', str(self.id), self.arg)
            sys.stderr.write("exec failed\n")
            os._exit(1)
        else:
            os.close(self._pipe_in[1])
            os.close(self._pipe_out[0])
            self._pid = pid

    def write(self, msg):
        if msg == 'YOU_WIN':
            self.n_wins += 1
        print('manager -> ' + str(self) + ':\t' + msg)
        os.write(self._pipe_out[1], (msg+'\n').encode())

    def read(self):
        msg = self._fo.readline().rstrip()
        print(str(self) + ' -> manager:\t' + msg)
        return msg

    def roll(self):
        self.hidden_dice = [random.randint(1, 6) for _ in 
                            range(self.n_dice - len(self.revealed_dice))]

    def play(self):
        self.write('PLAY ' + ' '.join(str(x) for x in self.hidden_dice))
        t = time.time()
        move = self.read()
        dt = time.time() - t
        if dt > 0.1:
            print('slow response by player ' + str(self) + ' (' + str(dt) + 's)')
        return move

