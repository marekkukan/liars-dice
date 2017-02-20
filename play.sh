#!/usr/bin/env bash

trap "kill 0" SIGINT

rm -f pipe-in pipe-out
mkfifo pipe-in pipe-out

(
./run_tournament.py 1 player-manual.py player-smart.py >log.txt 2>/dev/null
kill -SIGINT $$
) &

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
