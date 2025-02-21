
import time

from functools import total_ordering

from math import prod

def isInOrder(left, right):
    if (isinstance(left, int)) and isinstance(right, int):
        if left < right:
            return True
        if left == right:
            return None
        return False
    
    if (isinstance(left, list)) and isinstance(right, list):
        for l,r in zip(left,right):
            result = isInOrder(l,r)
            if False == result:
                return False
            elif True == result:
                return True

        if len(left) < len(right):
            return True
        elif len(left) == len(right):
            return None
        return False

    if (isinstance(left, list)):
        return isInOrder(left, [right])
    
    if not isinstance(right, list):
        print(type(right))
        print(right)
    assert(isinstance(right, list))
    return isInOrder([left], right)

@total_ordering
class comparor:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return isInOrder(self.value, other.value) == None
    
    def __lt__(self, other):
        return isInOrder(self.value, other.value) == True

def sol():
    start = time.perf_counter()

    file = open('inputs/input13.txt', 'r')

    score1 = 0

    all_lines = [eval(line) for line in file if not line.isspace()]
    file.close()

    for i in range(len(all_lines) // 2):
        if isInOrder(all_lines[i*2], all_lines[i*2+1]):
            # print(i+1)
            score1 += i + 1

    dividers = [[[2]], [[6]]]
    ordered = sorted([*all_lines, *dividers], key = comparor)

    score2 = prod(ordered.index(x) + 1 for x in dividers)

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
