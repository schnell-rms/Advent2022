import time

from functools import reduce

from typing import Callable

# import math

import re

from collections import deque, namedtuple

class xy_tuple(namedtuple("xy_tuple", ["x", "y"])):
    def __add__(self, other):
        return xy_tuple(self.x + other.x, self.y + other.y)

def sol():

    start = time.perf_counter()


    initminX = 0
    initmaxX = 0
    initminY = 0
    initmaxY = 0
    y = 0
    garden = set()
    with open('inputs/input23.txt', 'r') as file:
        for line in file:
            garden |= {xy_tuple(x,y) for x, val in enumerate(line.rstrip()) if val != '.'}
            initmaxX = len(line)
            y += 1

    initmaxY = y

    def printGarden(garden: set):
        print()
        print(len(garden), " Elves")
        for y in range(initminY, initmaxY):
            for x in range(initminX, initmaxX):
                print("#" if xy_tuple(x,y) in garden else ".", end = "")
            print()
        print()

    # printGarden(garden)


    neighbours = {  xy_tuple(-1, -1), xy_tuple( 0, -1), xy_tuple( 1, -1),
                    xy_tuple(-1,  0),                   xy_tuple( 1,  0),
                    xy_tuple(-1,  1), xy_tuple( 0,  1), xy_tuple( 1,  1),}

    def hasNeighbours(elf:xy_tuple, garden):
        for other in neighbours:
            if elf + other in garden:
                return True
        return False

    # Move rules:
    check = [   [xy_tuple(-1, -1), xy_tuple( 0, -1), xy_tuple( 1, -1)],
                [xy_tuple(-1,  1), xy_tuple( 0,  1), xy_tuple( 1,  1)],
                [xy_tuple(-1, -1), xy_tuple(-1,  0), xy_tuple(-1,  1)],
                [xy_tuple( 1, -1), xy_tuple( 1,  0), xy_tuple( 1,  1)]]
        
    def moveElf(elf_pos: xy_tuple, currentGarden, nextGarden, check_start_idx):
        if hasNeighbours(elf_pos, currentGarden):
            for i in range(4):
                cidx = (check_start_idx + i) % 4
                p1 = elf_pos + check[cidx][0]
                p2 = elf_pos + check[cidx][1]
                p3 = elf_pos + check[cidx][2]
                if p1 not in currentGarden and p2 not in currentGarden and p3 not in currentGarden:
                    if p2 not in nextGarden:
                        nextGarden.add(p2)
                    else:
                        # conflict: two elves to move in the same pos
                        # The other elf must be put back:
                        nextGarden.remove(p2) # removed
                        nextGarden.add(p2 + check[cidx][1]) # the other elf could have come only from there.
                        nextGarden.add(elf_pos) # current elf remains in place
                    # Moved or not, decision taken. Return:
                    return
        # Still here? Than no move:
        nextGarden.add(elf_pos)

    firstCheckRuleIdx = 0
    for i in range(10):
        new_garden = set()
        for elf in garden:
            moveElf(elf, garden, new_garden, firstCheckRuleIdx)

        firstCheckRuleIdx += 1
        firstCheckRuleIdx %= 4
        garden = new_garden
        # printGarden(garden)

    minX = reduce(lambda e, other: e if e.x < other.x else other, garden).x
    maxX = reduce(lambda e, other: e if e.x > other.x else other, garden).x
    minY = reduce(lambda e, other: e if e.y < other.y else other, garden).y
    maxY = reduce(lambda e, other: e if e.y > other.y else other, garden).y

    # print("X: ", minX, maxX, "Y: ", minY, maxY)

    nb_positions = (maxX - minX + 1) * (maxY - minY + 1)
    score1 = nb_positions - len(garden)
    score2 = 0

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
