
import time

import utils

def sol():
    start = time.perf_counter()

    positions = set()
    
    hx = 0
    hy = 0
    tx = 0
    ty = 0

    nbKnots = 10
    ropeX = [0] * nbKnots
    ropeY = [0] * nbKnots
    positionsLongRope = set()

    with open('inputs/input09.txt', 'r') as file:
        for line in file:
            n = utils.firstNumber(line)
            for i in range(n):
                match line[0]:
                    case 'R':
                        hx += 1
                        ropeX[0] += 1
                    case 'D':
                        hy -= 1
                        ropeY[0] -= 1
                    case 'L':
                        hx -= 1
                        ropeX[0] -= 1
                    case 'U':
                        hy += 1
                        ropeY[0] += 1

                if abs(hy-ty) > 1:
                    ty += (hy - ty) // 2
                    tx = hx
                elif abs(hx-tx) > 1:
                    tx += (hx - tx) // 2
                    ty = hy

                for i in range(1,len(ropeX)):
                    dx = min(1, max(-1, ropeX[i-1] - ropeX[i]))
                    dy = min(1, max(-1, ropeY[i-1] - ropeY[i]))

                    if abs(ropeY[i-1] - ropeY[i]) > 1 or abs(ropeX[i-1] - ropeX[i]) > 1:
                        ropeX[i] += dx
                        ropeY[i] += dy

                positions.add((tx,ty))
                positionsLongRope.add((ropeX[-1], ropeY[-1]))


    score1 = len(positions)
    score2 = len(positionsLongRope)

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
