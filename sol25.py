import time

def from5to10(line):
    dic  = {"2":2, "1":1, "0":0, "-":-1, "=":-2}
    ret = 0
    p = 1
    for c in reversed(line):
        ret += dic[c] * p
        p *= 5
    return ret

def from10to5str(n10):
    ret = ""
    dic  = {2:"2", 1: "1", 0:"0", -1:"-", -2:"="}
    while n10 != 0:
        d = n10 % 5
        if d > 2:
            d -= 5
        ret += dic[d]

        n10 -= d
        n10 //= 5
    
    return ret[::-1]

def sol():

    start = time.perf_counter()

    score1 = 0
    with open('inputs/input25.txt', 'r') as file:
        for line in file:
            score1 += from5to10(line.rstrip())

    print("Base 10: ", score1)
    score1 = from10to5str(score1)

    end = time.perf_counter()

    print(f"Running time {end-start:.6f} seconds")

    print("First and only star: ", score1)
    return

if __name__ == "__main__":
    sol()
