
import time

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
    
    assert(isinstance(right, list))
    return isInOrder([left], right)

def sol():
    start = time.perf_counter()

    file = open('inputs/input13.txt', 'r')

    left_line = file.readline()
    right_line = file.readline()

    idx = 1
    score1 = 0
    while left_line != "":
        if isInOrder(eval(left_line), eval(right_line)):
            # print(idx)
            score1 += idx

        left_line = "\n"
        while(left_line.isspace()):
            left_line = file.readline()
        right_line = file.readline()
        idx += 1

    signal = [line.strip() for line in file.readlines()]

    file.close()


    score2 = 0

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
