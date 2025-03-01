import time

from functools import reduce

from typing import Callable

import re

class xy_tuple(tuple):
    def __add__(self, other):
        return xy_tuple(a + b for a,b, in zip(self,other))

def sol():

    start = time.perf_counter()

    notes = {}
    directions = ""
    startX = 0
    startY = 0
    with open('inputs/input22.txt', 'r') as file:
        y = 0
        for line in file:
            if (line.isspace()):
                break
            if y == 0:
                # assume it is not a '#'
                startX = len(line) - len(line.lstrip())
            notes |= {xy_tuple((x,y)):val for x, val in enumerate(line.rstrip()) if val != ' '}
            y += 1

        directions = next(file)

    maxBorderX = reduce(lambda xy, other_xy: xy if xy[0] > other_xy[0] else other_xy, notes.keys())[0] + 1
    maxBorderY = reduce(lambda xy, other_xy: xy if xy[1] > other_xy[1] else other_xy, notes.keys())[1] + 1

    def printNotes():
        for y in range(maxBorderY):
            for x in range(maxBorderX):
                if (pos := xy_tuple((x,y))) in notes:
                    print(notes[pos], end="")
                else:
                    print(" ", end="")
            print()

    # printNotes()

    def moveOneStep(step:xy_tuple, current_pos:xy_tuple):
        next_pos = current_pos + step   
        
        # while outside the map, just go in the until back in the map:
        while next_pos not in notes:
            next_pos += step
            next_pos = xy_tuple(((next_pos[0] + maxBorderX) % maxBorderX, (next_pos[1] + maxBorderY) % maxBorderY))

        # Check wall
        if notes[next_pos] == "#":
            return current_pos
        
        return next_pos

    # Split by the "" between a [LR] and a \d
    directions = re.split(r"(?<=[LR])(?=\d)|(?<=\d)(?=[LR])",directions) 
    orientationXY = [xy_tuple(c) for c in [(1,0),  (0, 1), (-1, 0), (0, -1)]]

    draw = [">","v","<","^"]

    def move(movefunction:Callable, pos:xy_tuple, dirIdx:int , doDraw: bool):
        if doDraw: notes[pos] = draw[0]

        for d in directions:
            match d:
                case "L":
                    dirIdx += 3
                    dirIdx %= 4
                    if doDraw: notes[pos] = draw[dirIdx]
                    pass
                case "R":
                    dirIdx += 1
                    dirIdx %= 4
                    if doDraw: notes[pos] = draw[dirIdx]
                    pass
                case _:
                    for _ in range(int(d)):
                        pos = movefunction(orientationXY[dirIdx], pos)
                        if doDraw: notes[pos] = draw[dirIdx]

        return pos, dirIdx

    # printNotes()

    # First star:
    pos, dirIdx = move(moveOneStep, xy_tuple((startX, startY)), 0, False)
    pos += xy_tuple((1,1)) # because of starting from (0,0) in the code
    score1 = 1000 * pos[1] + 4 * pos[0] + dirIdx

    # Second star
    score2 = 0

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
