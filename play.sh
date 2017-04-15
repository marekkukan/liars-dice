#!/usr/bin/env bash

exitf() {
    [[ -z `jobs -r` ]] || kill 0
    rm pipe0 pipe1
}

trap exitf EXIT

players=$@
[[ -z $@ ]] && players="player_smart.py"

mkfifo pipe0 pipe1

./run_tournament.py 1 player_manual.py ${players} >log-stdout.txt 2>log-stderr.txt &

cat pipe1 &
cat > pipe0
