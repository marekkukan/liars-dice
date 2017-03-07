#!/usr/bin/python3 -u


import os
import sys

UNICODE_DICE = [None, "\u2680 ", "\u2681 ", "\u2682 ", "\u2683 ", "\u2684 ", "\u2685 "]

pipe_in = open('pipe0', 'r')
pipe_out = open('pipe1', 'w')

pipe_out.write('instead of BID/CHALLENGE/REVEAL you can type b/c/r\n' + 
               'press <Enter> for some info\n' + '#'*40 + '\n')
pipe_out.flush()

line = sys.stdin.readline()
while line:
    pipe_out.write(line)
    pipe_out.flush()
    parts = line.rstrip().split(' ')
    if parts[0] == 'NEW_ROUND':
        bid = '-'
        revealed_dice = ''
    elif parts[0] == 'PLAYER_BIDS':
        bid = parts[2] + ' x ' + UNICODE_DICE[int(parts[3])]
    if parts[0] == 'PLAY':
        hidden_dice = ' '.join(UNICODE_DICE[int(x)] for x in parts[1:])
        move = pipe_in.readline().rstrip()
        if move == '':
            pipe_out.write('\tcurrent bid:\t\t' + bid + 
                           '\n\tyour revealed dice:\t' + revealed_dice + 
                           '\n\tyour hidden dice:\t' + hidden_dice + 
                           '\n\n')
            pipe_out.flush()
            move = pipe_in.readline().rstrip()
        if move[0] == 'b':
            move = 'BID' + move[1:]
        elif move[0] == 'c':
            move = 'CHALLENGE' + move[1:]
        elif move[0] == 'r':
            move = 'REVEAL' + move[1:]
        if move.startswith('REVEAL'):
            revealed_dice += ' '.join(UNICODE_DICE[int(x)] for x in move.split(' ')[1:])
            revealed_dice += ' '
        print(move)
    line = sys.stdin.readline()

