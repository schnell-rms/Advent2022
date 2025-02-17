
import time

import utils

def sol():
    start = time.perf_counter()

    score1 = 0
    score2 = 0
    with open('inputs/input04.txt', 'r') as file:
        for line in file:
            ln = line.strip()
            if ln:
                out = utils.extractAllNumbers(ln)
                isInclusion = out[0] >= out[2] and out[1] <= out[3] or out[0] <= out[2] and out[1] >= out[3]
                score1 += isInclusion
                score2 +=  (isInclusion or 
                            out[0] >= out[2] and out[0] <= out[3] or
                            out[1] >= out[2] and out[1] <= out[3])


    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
