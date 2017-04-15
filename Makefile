all: player_random_c player_random_java

player_random_c: player_random.c
	gcc -o $@ $<

player_random_java: PlayerRandom.class

PlayerRandom.class: PlayerRandom.java
	javac $<
