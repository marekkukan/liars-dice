#!/usr/bin/env python3


import os
import sys
import datetime
import matplotlib.pyplot as plt
from player import Player
from tournament import Tournament


if __name__ == '__main__':
    os.dup2(os.open('log.txt', os.O_CREAT | os.O_WRONLY | os.O_TRUNC), 1)
    n_games = int(sys.argv[1])
    players = [Player(x) for x in sys.argv[2:]]
    for p in players:
        p.run()
    tournament = Tournament(players, n_games)
    wins = tournament.run()
    players = sorted(players, key=lambda x: x.id)

    ### plot
    G = len(wins)
    P = len(players)
    COLORS = ['purple', 'orange', 'r', 'g', 'b'] + ['k'] * P
    c = [0] * P
    d = [[0] * (G+1) for _ in range(P)]
    for i,p in enumerate(wins):
        c[p] += 1
        for j in range(P):
            d[j][i+1] = d[j][i]
        d[p][i+1] += 1
    for i in range(P):
        plt.plot(range(G+1), d[i], COLORS[i], linestyle='-')
        plt.text(G+G//100, d[i][-1], players[i]._path, color=COLORS[i])
    plt.title(str(datetime.date.today()))
    plt.xlabel('number of games')
    plt.ylabel('number of wins')
    plt.savefig('graph-'+str(datetime.date.today())+'.svg', bbox_inches='tight')
    ### end plot

    print('the end.')

