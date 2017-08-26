#!/usr/bin/python3 -u

import sys
import random
from time import sleep
from colorama import Fore, Style, init
init()

UNICODE_DICE = ['\u2610 ', '\u2680 ', '\u2681 ', '\u2682 ', '\u2683 ', '\u2684 ', '\u2685 ']

pipe_in = open('pipe0', 'r')
pipe_out = open('pipe1', 'w')

def print_all_players():
    clear(n_players + 3)
    pipe_out.write(Fore.BLUE + 'dice: ' + str(sum(hs)) + 
                   ' \tgame: ' + str(n_game) + '/' + str(n_games) + 
                   ' \twins: ' + str(wins) + Fore.RESET + '\n')
    pipe_out.write(' ' * 5 + '\u2554' + '\u2550'*(2*max(hs)+2) + '\u2557' + '\n')
    for i in range(n_players):
        print_player(perm[i])
    pipe_out.write(' ' * 5 + '\u255A' + '\u2550'*(2*max(hs)+2) + '\u255D' + '\n')
    pipe_out.flush()
    if challenge:
        pass
    elif hs[my_id] == 0:
        sleep(0.1)
    else:
        sleep(0.5)

def clear(n_lines):
    global not_yet_called
    if not_yet_called:
        not_yet_called = False
    else:
        pipe_out.write(r'\033[' + str(n_lines + 1) + 'A\n')
    pipe_out.write((r'\033[K' + '\n') * n_lines)
    pipe_out.write(r'\033[' + str(n_lines + 1) + 'A\n')

def print_player(idx):
    def p(dice, color=''):
        if not challenge:
            return color + ''.join(UNICODE_DICE[x] for x in dice) + Fore.RESET
        style = [Style.DIM] * 7
        style[1] = Style.BRIGHT
        style[int(bid[1])] = Style.BRIGHT
        return color + ''.join(style[x] + UNICODE_DICE[x] + Style.NORMAL for x in dice) + Fore.RESET

    c = 1 if challenge else 0
    prefix = '-> ' if idx==cp else '   '
    pipe_out.write(prefix + str(idx) + ' \u2551 ' + 
                   ('{:<' + str(2*max(hs) + 3*len(Fore.RESET) + len(Fore.YELLOW) + c*hs[idx]*len(Style.BRIGHT + Style.NORMAL)) + '}')
                   .format(p(rd[idx]) + p(jrd[idx], Fore.YELLOW) + p([0]*(hs[idx]-len(rd[idx]+jrd[idx]))))
                   + ' \u2551 ' + ' '.join(bids[idx]) + '\n')

def inform(message, color=Fore.GREEN):
    pipe_out.write(color + message + Fore.RESET + '\n')
    pipe_out.flush()
    pipe_in.readline()
    pipe_out.write(r'\033[3A'+'\n'+r'\033[K'+'\n'+r'\033[2A'+'\n')

def formatted_bid(q, v):
    return '{:>4}'.format(q + UNICODE_DICE[int(v)])

not_yet_called = True
line = sys.stdin.readline()
while line:
    parts = line.rstrip().split()
    if parts[0] == 'NEW_TOURNAMENT':
        n_players, my_id, n_games = int(parts[1]), int(parts[2]), int(parts[3])
        n_game = 0
        wins = 0
    elif parts[0] == 'NEW_GAME':
        ids = [int(x) for x in parts[1:]]
        # rotate so that my_id is last
        perm = ids[ids.index(my_id)+1:] + ids[:ids.index(my_id)+1]
        n_game += 1
        new_game = True
    elif parts[0] == 'NEW_ROUND':
        if new_game:
            if n_game == 1:
                pass
            elif challenge:
                inform(new_game_message)
            else:
                inform('someone played an invalid move', Fore.RED)
        else:
            new_hs = [int(x) for x in parts[1:]]
            for i in range(len(hs)):
                if new_hs[i] > hs[i]:
                    if i == my_id:
                        inform('you gained 1 die')
                    else:
                        inform('player ' + str(i) + ' gained 1 die')
                    break
            else:
                for i in range(len(hs)):
                    if new_hs[i] < hs[i]:
                        if new_hs[i] == 0:
                            if i == my_id:
                                inform('you are out')
                            else:
                                inform('player ' + str(i) + ' is out')
                        else:
                            diff = hs[i] - new_hs[i]
                            d = ' die' if diff == 1 else ' dice'
                            if i == my_id:
                                inform('you lost ' + str(diff) + d)
                            else:
                                inform('player ' + str(i) + ' lost ' + str(diff) + d)
                        break
        # hs : hand size
        # rd : revealed dice
        # jrd : just revealed dice
        hs = [int(x) for x in parts[1:]]
        rd = [[] for _ in range(n_players)]
        jrd = [[] for _ in range(n_players)]
        bids = [[] for _ in range(n_players)]
        new_round = True
        challenge = False
        i_challenged = False
        if new_game:
            new_game = False
    elif parts[0] == 'PLAYER_BIDS':
        idx = int(parts[1])
        cp = idx
        if new_round:
            for i in range(n_players):
                if perm[i] == cp:
                    break
                bids[perm[i]].append(' '*4)
            new_round = False
        bid = parts[2:4]
        bids[idx].append(formatted_bid(*bid))
        print_all_players()
    elif parts[0] == 'PLAYER_REVEALS':
        idx = int(parts[1])
        cp = idx
        if new_round:
            for i in range(n_players):
                if perm[i] == cp:
                    break
                bids[perm[i]].append(' '*4)
            new_round = False
        rd[idx].extend(jrd[idx])
        jrd[idx] = []
        jrd[idx] = [int(x) for x in parts[2:]]
        print_all_players()
    elif parts[0] == 'PLAYER_CHALLENGES':
        idx = int(parts[1])
        cp = idx
        if new_round:
            for i in range(n_players):
                if perm[i] == cp:
                    break
                bids[perm[i]].append(' '*4)
            new_round = False
        bids[idx].append('  \U0001F4A3 ')
        challenge = True
        print_all_players()
    elif parts[0] == 'PLAYER_HAD':
        idx = int(parts[1])
        rd[idx].extend(jrd[idx])
        jrd[idx] = []
        jrd[idx] = [int(x) for x in parts[2:]]
        print_all_players()
    elif parts[0] == 'PLAY':
        cp = my_id
        if new_round:
            for i in range(n_players):
                if perm[i] == cp:
                    break
                bids[perm[i]].append(' '*4)
            new_round = False
        rd[my_id] = [int(x) for x in parts[1:]]
        print_all_players()
        move = pipe_in.readline().strip()
        pipe_out.write(r'\033[2A'+'\n'+r'\033[K'+'\n'+r'\033[2A'+'\n')
        tokens = move.split()
        if not move or move[0] == 'c':
            bids[my_id].append('  \U0001F4A3 ')
            challenge = True
            i_challenged = True
            print('CHALLENGE')
        elif len(tokens) == 1 or move[0] == 'r':
            if move[0] == 'r':
                dice = [int(x) for x in tokens[1:]]
            else:
                dice = [int(x) for x in move]
            jrd[my_id] = dice + jrd[my_id]
            print('REVEAL ' + ' '.join(str(x) for x in dice))
        else:
            if move[0] == 'b':
                bid = tokens[1:3]
            else:
                bid = tokens[0:2]
            bids[my_id].append(formatted_bid(*bid))
            print('BID ' + ' '.join(bid))
    elif parts[0] == 'YOU_WIN':
        wins += 1
        print_all_players()
        new_game_message = random.choice(['congrats', 'well played', 'good job'])
        if not challenge:
            inform('someone played an invalid move', Fore.RED)
    elif parts[0] == 'YOU_LOSE':
        new_game_message = random.choice(['you suck', 'maybe next time', 'try harder'])
        if not challenge or (i_challenged and new_round):
            inform('invalid move', Fore.RED)
    line = sys.stdin.readline()

pipe_out.write(Fore.GREEN + new_game_message + Fore.RESET + '\n')
pipe_out.flush()
