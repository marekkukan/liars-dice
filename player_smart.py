#!/usr/bin/python3 -u


import sys
import random


line = sys.stdin.readline()
while line:
    parts = line.split(' ')
    if parts[0] == 'NEW_ROUND':
        count, value = 0, 6
        n_dice = sum(int(x) for x in parts[1:])
    elif parts[0] == 'PLAYER_BIDS':
        count, value = int(parts[2]), int(parts[3])
    elif parts[0] == 'PLAY':
        if count > n_dice / 3:
            print('CHALLENGE')
        else:
            print('BID ' + str(count+1) + ' ' + str(value))
    line = sys.stdin.readline()

