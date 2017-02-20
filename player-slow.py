#!/usr/bin/python3 -u


import sys
import random
import time


line = sys.stdin.readline()
while line:
    parts = line.split(' ')
    if parts[0] == 'NEW_ROUND':
        count, value = 0, 6
    elif parts[0] == 'PLAYER_BIDS':
        count, value = int(parts[2]), int(parts[3])
    elif parts[0] == 'PLAY':
        if random.random() < 0.01:
            time.sleep(0.1)
        if count > 0 and random.random() < 0.4:
            print('CHALLENGE')
        else:
            print('BID ' + str(count+1) + ' ' + str(value))
    line = sys.stdin.readline()

