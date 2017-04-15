#!/usr/bin/python3 -u


import sys
import random


line = sys.stdin.readline()
while line:
    parts = line.split(' ')
    if parts[0] == 'NEW_ROUND':
        quantity, value = 0, 6
        n_dice = sum(int(x) for x in parts[1:])
    elif parts[0] == 'PLAYER_BIDS':
        quantity, value = int(parts[2]), int(parts[3])
    elif parts[0] == 'PLAY':
        if quantity > n_dice / 3:
            print('CHALLENGE')
        else:
            print('BID ' + str(quantity+1) + ' ' + str(value))
    line = sys.stdin.readline()

