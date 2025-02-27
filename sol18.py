import time

import utils

def neighbours(xyz):
    x , y, z = xyz
    return [(x,y,z-1),(x,y,z+1),(x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z)]


def sol():
    start = time.perf_counter()

    nums = set()
    with open('inputs/input18.txt', 'r') as file:
        for line in file:
            nums.add(tuple(utils.extractAllNumbers(line)))

    score1 = len(nums) * 6
    for cube in nums:
        score1 -= len([nei for nei in neighbours(cube) if nei in nums])

    score2 = 0

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
