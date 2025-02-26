
import time

import utils

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

    x = -1
    if len(positions) == 2:
        pp = list(positions)
        if pp[0].start > pp[1].stop:
            x = (pp[0].start + pp[1].stop) // 2
        else:
            x = (pp[1].start + pp[0].stop) // 2

    return counter, x

def sensor_range(sensor):
    return abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])

def findFreePosition(nums):

    for sensor in nums:
        sensor.append(sensor_range(sensor))

    for sensor in nums:
        sx = sensor[0]
        sy = sensor[1]
        on_border_dist = sensor[4] + 1

        for y in range(max(0,sy - on_border_dist), min(4000000, sy + on_border_dist)):
            dy = abs(sy - y)
            dx = on_border_dist - dy
            for borderx in [sx + dx, sx - dx]:
                if borderx < 0 or borderx > 4000000:
                    continue

                found = True
                for other_sensor in nums:
                    if other_sensor is sensor:
                        continue

                    other_dist = other_sensor[4]
                    curr_dist = sensor_range([*other_sensor[:2],borderx, y])
                    if curr_dist <= other_dist:
                        found = False
                        break

                if found:
                    return borderx * 4000000 + y

    return -1

def sol():
    start = time.perf_counter()

    nums = []
    with open('inputs/input15.txt', 'r') as file:
        for line in file:
            nums.append(utils.extractAllNumbers(line))

    # simple
    # score1 = count_positions(nums, 10)
    score1, _ = count_positions(nums, 2000000)

    # Brute force:
    # x = -1
    # y = -1
    # while x < 0 and y<=4e6:
    #     y += 1
    #     score2, x = count_positions(nums, y)
    # score2 = x * int(4e6) + y

    # Other method:
    # That point must be near at least one sensor area:
    # For each sensor go along its border and check each point near it
    # to be far away from all other sensors
    # 4 times faster:
    score2 = findFreePosition(nums)

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
