from bid import Bid


class Game:

    def __init__(self, players):
        self.players = players
        self.players_sorted = sorted(players, key=lambda x: x.id)
        self.n_players = len(players)
        self.cpi = 0
        self.finished = False

    def cp(self):
        return self.players[self.cpi]

    def shift_cpi(self):
        self.ppi = self.cpi
        self.cpi = (self.cpi + 1) % len(self.players)
        while self.cp().n_dice <= 0:
            self.cpi = (self.cpi + 1) % len(self.players)

    def inform_others(self, msg):
        for i,p in enumerate(self.players):
            if i == self.cpi:
                continue
            p.write(msg)

    def run(self):
        for p in self.players:
            p.write('NEW_GAME ' + ' '.join(str(p.id) for p in self.players))
            p.n_dice = 6
        while not self.finished:
            self.play_round()
        return self.winner.id

    def play_round(self):
        self.finished_round = False
        self.bid = Bid(0, 6)
        for i,p in enumerate(self.players):
            p.write('NEW_ROUND ' + ' '.join(str(p.n_dice) for p in self.players_sorted))
            p.revealed_dice = []
            p.roll()
        self.n_dice = sum(p.n_dice for p in self.players)
        self.eval_move(self.cp().play(), challenge_possible=False)
        while not self.finished and not self.finished_round:
            self.shift_cpi()
            self.eval_move(self.cp().play())

    def eval_move(self, move, challenge_possible=True, reveal_possible=True):
        parts = move.split(' ')
        if parts[0] == 'BID':
            try:
                bid = Bid(int(parts[1]), int(parts[2]))
                assert 1 <= bid.value <= 6
                assert bid > self.bid
                assert bid.count <= self.n_dice + 1
            except:
                self.invalid_move(move)
                return
            self.bid = bid
            self.inform_others('PLAYER_BIDS ' + str(self.cp().id) + ' ' + str(bid))
        elif parts[0] == 'REVEAL':
            try:
                assert reveal_possible
                assert len(parts) > 1
                dice = (int(x) for x in parts[1:])
                for die in dice:
                    self.cp().hidden_dice.remove(die)
                    self.cp().revealed_dice.append(die)
            except:
                self.invalid_move(move)
                return
            self.inform_others('PLAYER_REVEALS ' + str(self.cp().id) + ' ' + ' '.join(parts[1:]))
            self.cp().roll()
            self.eval_move(self.cp().play(), False, False)
        elif parts[0] == 'CHALLENGE':
            self.finished_round = True
            if not challenge_possible:
                self.invalid_move(move)
                return
            self.inform_others('PLAYER_CHALLENGES ' + str(self.cp().id))
            for i in range(self.n_players):
                self.inform_others('PLAYER_HAD ' + str(self.cp().id) + ' ' + ' '.join(str(x) for x in self.cp().hidden_dice))
                self.shift_cpi()
            all_dice = []
            for p in self.players:
                all_dice.extend(p.revealed_dice)
                all_dice.extend(p.hidden_dice)
            diff = self.bid.count - sum([1 for die in all_dice if die == self.bid.value or die == 1])
            if diff < 0:
                self.cp().n_dice += diff
            elif diff > 0:
                self.players[self.ppi].n_dice -= diff
                self.cpi = self.ppi
            else:
                self.cp().n_dice -= 1
                self.players[self.ppi].n_dice += 1
            self.check_if_loses()
        else:
            self.invalid_move(move)

    def check_if_loses(self):
        if self.cp().n_dice <= 0:
            self.cp().n_dice = 0
            self.n_players -= 1
            self.cp().write('YOU_LOSE')
            self.shift_cpi()
            if self.n_players < 2:
                self.finished = True
                self.winner = self.cp()
                self.cp().write('YOU_WIN')

    def invalid_move(self, move):
        print('invalid move by player ' + str(self.cp()) + ' (' + move + ')')
        self.finished_round = True
        self.cp().n_dice = 0
        self.check_if_loses()

