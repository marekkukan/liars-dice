usage example:

```bash
# compile players in C and Java
make

# run tournament
./run_tournament.py 1000 player_random_c player_random_java player_smart.py

# see results
tail -n 5 log.txt

# manual play against two smart players
./play.sh player_smart.py player_smart.py
```
