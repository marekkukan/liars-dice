#!/usr/bin/python3 -u


import os
import sys


if not os.path.exists('pipe-in'):
    os.mkfifo('pipe-in')
if not os.path.exists('pipe-out'):
    os.mkfifo('pipe-out')

pipe_in = open('pipe-in', 'r')
pipe_out = open('pipe-out', 'w')

instruction = sys.stdin.readline()
while instruction:
    pipe_out.write(instruction)
    pipe_out.flush()
    if instruction.startswith('PLAY'):
        move = pipe_in.readline().rstrip()
        print(move)
    instruction = sys.stdin.readline()

