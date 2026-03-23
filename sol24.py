import time

from functools import reduce

from itertools import count

import math

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
    y = -1 # to start the blizzard flakes from 0
    valley = {}
    with open('inputs/input24.txt', 'r') as file:
        for line in file:
            valley |= {xy_tuple(x-1,y) : val for x, val in enumerate(line.rstrip()) if val not in '#'}
            initmaxX = len(line) - 2 # without the # borders
            y += 1

    initmaxY = y - 1 # do not count the border, i.e. the destination XY

    startXY = xy_tuple(0,-1)
    endXY = xy_tuple(initmaxX-1,initmaxY)

    # print("Start ", startXY)
    # print("End ", endXY)

    def printValley(valley: set):
        print()
        for y in range(initminY-1, initmaxY + 1):
            for x in range(initminX-1, initmaxX + 1):
                xy = xy_tuple(x,y)
                if xy in valley:
                    print(valley[xy][0] if len(valley[xy]) == 1 else len(valley[xy]), end = "")
                else:
                    print(" ", end="")
            print()
        print()

    # printValley(valley)

    def isFlake(xy:xy_tuple, time, valley):
        if xy == startXY or xy == endXY:
            return False
        
        if xy in valley:
            return  valley[xy_tuple((xy.x - time) % initmaxX, xy.y)] == ">" or \
                    valley[xy_tuple((xy.x + time) % initmaxX, xy.y)] == "<" or \
                    valley[xy_tuple( xy.x                   , (xy.y + time) % initmaxY)] == "^" or \
                    valley[xy_tuple( xy.x                   , (xy.y - time) % initmaxY)] == "v"
        else:
            return True

    def route(startXY:xy_tuple, endXY:xy_tuple, valley, start_time):
        q = deque() # propeer priority queue not needed for this specific routing
        q.append((start_time, startXY))

        moves = [xy_tuple(0,0), xy_tuple(0,-1), xy_tuple(0,1), xy_tuple(-1,0), xy_tuple(1,0)]

        # Normally it sould be costs, but for this a visited like usage is enough.
        # More over, the cost is time
        visited = set() 

        while len(q) > 0:
            time, xy = q.popleft()

            if (xy,time) in visited:
                    continue
            visited.add((xy,time))

            if xy == endXY:
                return time

            for step in moves:
                next_xy = xy + step

                if not isFlake(next_xy, time + 1, valley):
                    q.append((time + 1, next_xy))

        return math.inf


    score1 = route(startXY, endXY, valley, 0)

    score2 = route(startXY, endXY, valley, 0)
    score2 = route(endXY, startXY, valley, score2)
    score2 = route(startXY, endXY, valley, score2)

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
