
import time

from multiset import *

def findStart(line, n):
    lastn = line[:n]

    if len(set(lastn)) == n:
        return n

    for i in range(n, len(line)):
        lastn = line[i-(n-1):i+1]
        if len(set(lastn)) == n:
            return i+1

    return -1

# SLOWER:
# def findStart(line, n):
#     lastn = Multiset(line[:n])

#     if len(set(lastn)) == n:
#         return n

#     for i in range(n, len(line)):
#         lastn.remove(line[i-n],1)
#         lastn.add(line[i])
#         if len(set(lastn)) == n:
#             return i+1

#     return -1


def sol():
    start = time.perf_counter()

    file = open('inputs/input06.txt', 'r')
    line = file.readline()
    file.close()

    score1 = findStart(line,4)
    score2 = findStart(line,14)

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
