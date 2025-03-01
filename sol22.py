import time

from functools import reduce

from typing import Callable

# import math

import re

from collections import deque, namedtuple

xy_tuple_type = namedtuple("xy_tuple_type", ["x", "y"])
class xy_tuple(xy_tuple_type):
    def __add__(self, other):
        return xy_tuple(self.x + other.x, self.y + other.y)

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
            notes |= {xy_tuple(x,y):val for x, val in enumerate(line.rstrip()) if val != ' '}
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
    # Split by the "" between a [LR] and a \d
    directions = re.split(r"(?<=[LR])(?=\d)|(?<=\d)(?=[LR])",directions)
    orientationXY = [xy_tuple(1,0), xy_tuple(0, 1), xy_tuple(-1, 0), xy_tuple(0, -1)]

    def moveOneStep(current_pos:xy_tuple, dirIdx:int):
        step = orientationXY[dirIdx]
        next_pos = current_pos + step   
        
        # while outside the map, just go in the until back in the map:
        while next_pos not in notes:
            next_pos += step
            next_pos = xy_tuple((next_pos[0] + maxBorderX) % maxBorderX, (next_pos[1] + maxBorderY) % maxBorderY)

        # Check wall
        if notes[next_pos] == "#":
            return current_pos, dirIdx
        
        return next_pos, dirIdx

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
                        pos, dirIdx = movefunction(pos, dirIdx)
                        if doDraw: notes[pos] = draw[dirIdx]

        return pos, dirIdx

    # printNotes()

    # First star:
    pos, dirIdx = move(moveOneStep, xy_tuple(startX, startY), 0, False)
    pos += xy_tuple(1,1) # because of starting from (0,0) in the code
    score1 = 1000 * pos[1] + 4 * pos[0] + dirIdx

    # Second star

    # Faces in input:
    #   1 2
    #   3
    # 4 5
    # 6
    # faces =[[None, 1   , 2],
    #         [None, 3   , None],
    #         [4   , 5   , None],
    #         [6   , None, None]]

    #   1       6       3        6         3         4
    # 4 3 2   4 1 2   4 5 2   1  2  5   1  4  5   1  6  5
    #   5       3       6        3         6         2

    # kCUBE_SIZE = math.gcd(maxBorderX, maxBorderY) # Just hardcoded it, together with the shape

    def moveOnCube(current_pos:xy_tuple, dirIdx:int):
        step = orientationXY[dirIdx]
        next_pos = current_pos + step
        next_dirIdx = dirIdx

        # When outside the map, must find the next face and direction
        if next_pos not in notes:

            def changeFace(x,y, dirIdx):
                match dirIdx, x, y:
                    # Out to right
                    case 0, 150, _ if y in range(50):
                        return xy_tuple(99, 149 - y) , 2 #out from 2, to right. Go to 5
                    case 0, 100, _ if y in range(50, 100):
                        return xy_tuple(50 + y, 49), 3
                    case 0, 100, _ if y in range(100, 150):
                        return xy_tuple(149, 149 - y), 2
                    case 0, 50, _ if y in range(150, 200):
                        return xy_tuple(y - 100, 149), 3
                    # Out to down
                    case 1, _, 200 if x in range(50):
                        return xy_tuple(x + 100, 0), 1 #out from face 6. Go to 1
                    case 1, _, 150 if x in range(50, 100):
                        return xy_tuple(49, x + 100), 2  #out from face 5. Go to 6
                    case 1, _, 50 if x in range(100, 150):
                        return xy_tuple(99, x - 50), 2  # 2 -> 3
                    # Out to left
                    case 2, 49, _ if y in range(0, 50):
                        return xy_tuple(0, 149 - y), 0  # 1 -> 4
                    case 2, 49, _ if y in range(50, 100):
                        return xy_tuple(y - 50, 100), 1 # 3 -> 4
                    case 2, -1, _ if y in range(100, 150):
                        return xy_tuple(50, 149 - y), 0 # 4 -> 1
                    case 2, -1, _ if y in range(150, 200):
                        return xy_tuple(y - 100, 0), 1 # 6 -> 1
                    # Out to top
                    case 3, _, 99 if x in range(50):
                        return xy_tuple(50, 50 + x), 0 # 4 -> 3
                    case 3, _, -1 if x in range(50, 100):
                        return xy_tuple(0, x + 100), 0 # 1 -> 6
                    case 3, _, -1 if x in range(100, 150):
                        return xy_tuple(x - 100, 199), 3 # 2 -> 6
                return current_pos, dirIdx

            next_pos, next_dirIdx = changeFace(next_pos.x, next_pos.y, dirIdx)

        if notes[next_pos] == "#":
            return current_pos, dirIdx

        return next_pos, next_dirIdx

    pos, dirIdx = move(moveOnCube, xy_tuple(startX, startY), 0, False)
    pos += xy_tuple(1,1) # because of starting from (0,0) in the code
    score2 =  1000 * pos[1] + 4 * pos[0] + dirIdx

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
