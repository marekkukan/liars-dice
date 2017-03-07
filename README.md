usage example:

```
# compile player in C
make

# run tournament
./run_tournament.py 1000 player_buggy.py player_random player_smart.py >log.txt

# see results
tail -n 5 log.txt

# manual play against two smart players
./play.sh player_smart.py player_smart.py
```
