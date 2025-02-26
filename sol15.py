
import time

import utils

from itertools import count, product

def count_positions(nums, y):

    # Collect all x intervals on y row
    beacons = set()
    positions = set()
    for sensor in nums:
        beacons.add((sensor[2], sensor[3]))
        dist = abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])
        y_line_dist = abs(sensor[1] - y)
        if y_line_dist <= dist:
            x_wide = dist - y_line_dist
            positions.add(range(sensor[0] - x_wide, sensor[0] + x_wide + 1))
        
    # Count all the beacons on y row
    nb_beacons_on_y = 0
    for b in beacons:
        if y == b[1]:
            for r in positions:
                if b[0] in r:
                    nb_beacons_on_y += 1
                    break
    
    # Merge all x intervals
    while(True):
        is_change = False
        for r1 in positions:
            for r2 in positions:
                if r1 == r2:
                    continue

                # No intersection:
                if r1.stop < r2.start or r2.stop < r1.start:
                    continue

                # Intersection (or inclusion) for sure
                new_range = range(min(r1.start, r2.start), max(r1.stop, r2.stop))
                positions.remove(r1)
                positions.remove(r2)
                positions.add(new_range)
                is_change = True
                break

            if is_change:
                break

        if not is_change:
            break

    # Count all x positions on y
    counter = 0
    for p in positions:
        counter += len(p)

    # Substract the beacons on that y
    counter -= nb_beacons_on_y
    return counter

def sol():
    start = time.perf_counter()

    nums = []
    with open('inputs/input15.txt', 'r') as file:
        for line in file:
            nums.append(utils.extractAllNumbers(line))

    # simple
    # score1 = count_positions(nums, 10)
    score1 = count_positions(nums, 2000000)


    score2 = 0

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
