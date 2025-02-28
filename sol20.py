import time

import utils

from collections import deque, namedtuple

NumberInfo = namedtuple("NumberInfo", ["orig_idx", "value"])

def sol():
    start = time.perf_counter()

    numbers = deque()
    with open('inputs/input20.txt', 'r') as file:
        id = 0
        for line in file:
            numbers.append(NumberInfo(id, utils.firstNumber(line)))
            id += 1

    cp = list(numbers)
    n = len(numbers)

    def decrypt(numbers, factor, repeat):
        for _ in range(repeat):
            for num in cp:
                pos = next(idx for idx, val in enumerate(numbers) if num.orig_idx == val.orig_idx) 
                numbers.rotate(-pos)
                numbers.popleft()
                numbers.rotate( - ((num.value * factor) % (n-1)))
                numbers.appendleft(num)

        pos0 = next(idx for idx, num in enumerate(numbers) if num.value == 0)
        numbers.rotate(-pos0)

        return factor * (numbers[1000 % n].value + numbers[2000 % n].value + numbers[3000 % n].value)

    # First star
    numbers2 = numbers.copy()
    score1 = decrypt(numbers, 1, 1)

    # Second star:
    score2 = decrypt(numbers2, 811589153, 10)

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
