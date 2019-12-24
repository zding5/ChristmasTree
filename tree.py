#!/usr/bin/env python3

import threading as elf
import random
import os
import time

mutex = elf.Lock()

# 'tree.txt' for non-colored version.
tree = list(open('tree2.txt').read().rstrip())

# We can try a random range for rainbowish effect.
def colored_dot(color):
    if color == 'red':
        return f'\033[91m☆\033[0m'
    if color == 'green':
        return f'\033[92m☆\033[0m'
    if color == 'yellow':
        return f'\033[93m☆\033[0m'
    if color == 'blue':
        return f'\033[94m☆\033[0m'

def lights(color, indexes):
    off = True
    while True:
        for idx in indexes:
            tree[idx] = colored_dot(color) if off else '☆'

        mutex.acquire()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(''.join(tree))
        mutex.release()

        off = not off
        # Should experiment with some non-unform timing.
        time.sleep(random.uniform(.5, 1.5))

# Mains
# TODO: Actually make a main...

yellow = []
red = []
green = []
blue = []

for i, c in enumerate(tree):
    if c == 'Y':
        yellow.append(i)
        tree[i] = '☆'
    elif c == 'R':
        red.append(i)
        tree[i] = '☆'
    elif c == 'G':
        green.append(i)
        tree[i] = '☆'
    elif c == 'B':
        blue.append(i)
        tree[i] = '☆'

ty = elf.Thread(target=lights, args=('yellow', yellow))
tr = elf.Thread(target=lights, args=('red', red))
tg = elf.Thread(target=lights, args=('green', green))
tb = elf.Thread(target=lights, args=('blue', blue))

for t in [ty, tr, tg, tb]:
    t.start()
for t in [ty, tr, tg, tb]:
    t.join()

# End Mains
