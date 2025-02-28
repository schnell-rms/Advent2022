import time

import utils

from collections import deque

def sol():
    start = time.perf_counter()

    numbers = deque()
    with open('inputs/input20.txt', 'r') as file:
        id = 0
        for line in file:
            numbers.append((id, utils.firstNumber(line)))
            id += 1

    cp = list(numbers)
    for num in cp:
        pos = [idx for idx, val in enumerate(numbers) if num[0] == val[0]][0]
        numbers.rotate(-pos)
        numbers.popleft()
        numbers.rotate(-num[1])
        numbers.appendleft(num)


    print(num)

    pos0 = [idx for idx, val in enumerate(numbers) if val[1] == 0][0]
    numbers.rotate(-pos0)

    n = len(numbers)

    # First star
    score1 = numbers[1000 % n][1] + numbers[2000 % n][1] + numbers[3000 % n][1]

    # Second star:
    score2 = 0

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
