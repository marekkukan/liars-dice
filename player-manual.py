#!/usr/bin/python3 -u


import os
import sys


if not os.path.exists('pipe-in'):
    os.mkfifo('pipe-in')
if not os.path.exists('pipe-out'):
    os.mkfifo('pipe-out')

pipe_in = open('pipe-in', 'r')
pipe_out = open('pipe-out', 'w')

line = sys.stdin.readline()
while line:
    pipe_out.write(line)
    pipe_out.flush()
    parts = line.split(' ')
    if parts[0] == 'PLAY':
        move = pipe_in.readline().rstrip()
        print(move)
    line = sys.stdin.readline()

