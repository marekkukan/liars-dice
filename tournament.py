import sys
import random
from game import Game


class Tournament:

    def __init__(self, players, n_games=1):
        self.players = players
        self.n_games = n_games

    def run(self):
        for i,p in enumerate(self.players):
            p.id = i
            p.write('NEW_TOURNAMENT ' + str(len(self.players)) + ' ' + str(p.id) + ' ' + str(self.n_games))
        for i in range(self.n_games):
            sys.stderr.write('\r' + str(i+1) + '/' + str(self.n_games))
            random.shuffle(self.players)
            game = Game(self.players)
            game.run()
        sys.stderr.write('\n')
        print('results:')
        for i,p in enumerate(sorted(self.players, key=lambda x: x.n_wins, reverse=True)):
            print(str(i+1) + '. ' + str(p) + '\t(' + str(p.n_wins) + ' wins)')

