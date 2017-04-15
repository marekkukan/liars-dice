#!/usr/bin/env python3


import os
import sys
from player import Player
from tournament import Tournament


if __name__ == '__main__':
    os.dup2(os.open('log.txt', os.O_CREAT | os.O_WRONLY | os.O_TRUNC), 1)
    n_games = int(sys.argv[1])
    players = [Player(x) for x in sys.argv[2:]]
    for p in players:
        p.run()
    tournament = Tournament(players, n_games)
    tournament.run()
    print('the end.')

