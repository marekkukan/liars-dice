#!/usr/bin/python3 -u


import sys
import random


line = sys.stdin.readline()
while line:
    parts = line.split(' ')
    if parts[0] == 'NEW_ROUND':
        quantity, value = 0, 6
    elif parts[0] == 'PLAYER_BIDS':
        quantity, value = int(parts[2]), int(parts[3])
    elif parts[0] == 'PLAY':
        if quantity > 0 and random.random() < 0.4:
            print('CHALLENGE')
        else:
            print('BID ' + str(quantity+1) + ' ' + str(value))
    line = sys.stdin.readline()

