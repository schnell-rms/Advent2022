
import time

import utils

def sol():
    start = time.perf_counter()

    X = 1

    ncycles = 0

    power_sum = 0

    CRT = ['.'] * 240

    with open('inputs/input10.txt', 'r') as file:
        for line in file:

            cp = (ncycles) % 40
            if abs(cp - X) <= 1:
                CRT[ncycles] = '#'
            ncycles += 1

            if (ncycles - 20) % 40 == 0:
                power_sum += X * ncycles

            if line.strip() != "noop":
                _, num = line.split()

                cp = (ncycles) % 40
                if abs(cp - X) <= 1:
                    CRT[ncycles] = '#'
                ncycles += 1

                if (ncycles - 20) % 40 == 0:
                    power_sum += X * ncycles

                X += int(num)


    for i in range(0, 201, 40):
        s = ''.join(CRT[i:i+40])
        print(s)
    # PGPHBEAB


    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", power_sum)
    return

if __name__ == "__main__":
    sol()
