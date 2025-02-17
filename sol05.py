
import time

import copy

import utils

def sol():
    start = time.perf_counter()

    score1 = ""
    score2 = ""
    stackLines = []
    stacks = [[]] #stack with index 0 already added: it will not be used
    stacks9001 = [] 
    isStatusRead = False
    with open('inputs/input05.txt', 'r') as file:
        for line in file:
            if not line.isspace():
                if isStatusRead:
                    moves = utils.extractAllNumbers(line)
                    stacks[moves[2]] += reversed(stacks[moves[1]][-moves[0]:])
                    stacks[moves[1]] = stacks[moves[1]][:-moves[0]]

                    stacks9001[moves[2]] += stacks9001[moves[1]][-moves[0]:]
                    stacks9001[moves[1]] = stacks9001[moves[1]][:-moves[0]]
                else:
                    stackLines.append(line)
            elif isStatusRead == False:
                isStatusRead = True
                # Init the status proper structures:
                stackIds = stackLines[-1]
                out = utils.extractAllNumbers(stackIds)
                for id in out:
                    stacks.append([])
                    cpos = stackIds.index(str(id))
                    for linestr in reversed(stackLines[:-1]):
                        if cpos < len(linestr) and linestr[cpos] != ' ':
                            stacks[-1].append(linestr[cpos])
                        else:
                            break
                stacks9001 = copy.deepcopy(stacks)

                print()

                print(stacks)

                print()


    for s in stacks[1:]:
        score1 += s[-1]

    for s in stacks9001[1:]:
        score2 += s[-1]

    print(stacks)
    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
