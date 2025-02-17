
import time

import heapq

def prio(c):
    if c <= 'Z':
        assert(c >= 'A')
        return ord(c) - ord('A') + 27
    return ord(c) - ord('a') + 1

def sol():
    start = time.perf_counter()

    score1 = 0
    score2 = 0
    with open('inputs/input03.txt', 'r') as file:
        counter = 0
        group = [set(),set(),set()] #or [1,2,3] aka any 3 elements
        for line in file:
            ln = line.strip()
            if ln:
                halfsize = len(ln)//2
                common = [x for x in ln[:halfsize] if x in set(ln[halfsize:])]
                score1 += prio(common[0])

                group[counter] = set(ln)
                counter += 1
                if counter == 3:
                    common = list(group[0].intersection(group[1], group[2]))
                    score2 += prio(common[0])
                    counter = 0



    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
