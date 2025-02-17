import time

import heapq

def sol():
    start = time.perf_counter()
    allNumbers = []
    with open('input.txt', 'r') as file:
        allNumbers.append([])
        for line in file:
            ln = line.strip()
            if ln: 
                allNumbers[-1].append(int(ln))
            else:
                allNumbers.append([])

    end = time.perf_counter()

    print(f"Reading time {end-start:.3f} seconds")

    start = time.perf_counter()
    sums = [sum(x) for x in allNumbers]
    ret = max(sums)
    end = time.perf_counter()
    print(f"Solve time {end-start:.3f} seconds")
    print("First star: ", ret)

    # Second star:
    start = time.perf_counter()
    ret = max([sum(x) for x in allNumbers])
    end = time.perf_counter()
    print(f"Solve time {end-start:.3f} seconds")

    heap = sums
    ret2 = sum(heapq.nlargest(3, heap))
    print("Second star: ", ret2)
    return

if __name__ == "__main__":
    sol()