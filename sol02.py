import time

import heapq


def sol():
    start = time.perf_counter()

    scores = {
        "A X": 43,
        "A Y": 84,
        "A Z": 38,
        "B X": 11,
        "B Y": 55,
        "B Z": 99,
        "C X": 72,
        "C Y": 26,
        "C Z": 67,
    }

    score1 = 0
    score2 = 0
    with open('input.txt', 'r') as file:
        for line in file:
            ln = line.strip()
            if ln:
                score1 += scores[ln] // 10
                score2 += scores[ln] % 10

    end = time.perf_counter()

    print(f"Reading time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
