#!/usr/bin/python3 -u


import sys
import random
from bid import Bid


instruction = sys.stdin.readline()
while instruction:
    parts = instruction.split(' ')
    if parts[0] == 'NEW_ROUND':
        bid = Bid(0, 6)
    elif parts[0] == 'OPPONENT_BIDS':
        bid = Bid(int(parts[1]), int(parts[2]))
    elif parts[0] == 'PLAY':
        if bid.count > 0 and random.random() < 0.4:
            print('CHALLENGE')
        else:
            print('BID ' + str(bid.count+1) + ' ' + str(bid.value))
    instruction = sys.stdin.readline()

