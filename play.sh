#!/usr/bin/env bash

trap "kill 0" SIGINT

[[ -p "pipe-in" ]] || mkfifo pipe-in
[[ -p "pipe-out" ]] || mkfifo pipe-out

./manager.py player-manual.py player-random.py >log.txt 2>/dev/null &

(
while true
do
    cat pipe-out
done
) &

while true
do
    cat > pipe-in
done
