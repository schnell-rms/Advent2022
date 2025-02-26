
import time

import utils

from itertools import product

def add_rocks(x1, y1, x2, y2, rocks):
    rocks.update(product(range(min(x1,x2), max(x1,x2) + 1), range(min(y1,y2), max(y1,y2) + 1)))

def fall(x,y,rocks):
    if (x,y+1) not in rocks:
        return (x,y+1)
    
    if (x - 1, y + 1) not in rocks:
        return (x - 1,y+1)
    
    if (x + 1, y + 1) not in rocks:
        return (x + 1, y + 1)
    
    return (x,y)

def countSandGrains(rocks, free_fall_y, add_free_falls):
    startPos = (500,0)
    nb_rocks = len(rocks)
    is_sand_added = True
    while(is_sand_added): # covers the case when the sand entry is in a closed room
        # which will eventually be filled with sand
        pos = startPos

        is_sand_added = False
        while(pos[1] < free_fall_y):
            next_pos = fall(pos[0], pos[1], rocks)
            if (next_pos == pos) or (add_free_falls and next_pos[1] == free_fall_y - 1):
                is_sand_added = next_pos not in rocks
                rocks.add(next_pos)
                break
            pos = next_pos

    return  len(rocks) - nb_rocks

def sol():
    start = time.perf_counter()

    rocks = set()

    with open('inputs/input14.txt', 'r') as file:
        for line in file:
            nums = utils.extractAllNumbers(line)
            for i in range(0,len(nums)-3,2):
                add_rocks(nums[i], nums[i+1], nums[i+2], nums[i+3], rocks)


    free_fall_y = max(y for _, y in rocks)

    rocks2 = rocks.copy()
    score1 = countSandGrains(rocks, free_fall_y, False)


    # Method 1:
    # add_rocks(-2000, free_fall_y + 2, 2000, free_fall_y + 2, rocks2)
    # score2 = countSandGrains(rocks2, free_fall_y + 2, False)
    # or Method2: 
    score2 = countSandGrains(rocks2, free_fall_y + 2, True)

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
