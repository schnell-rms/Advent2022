import time

import utils

class Monkey:
    def __init__(self, instruction):
        self.scream = utils.firstNumber(instruction)
        if None == self.scream:
            instruction = instruction.strip()
            self.operand_1 = instruction[:4]
            self.operand_2 = instruction[-4:]
            self.operator = instruction[5]

def sol():

    start = time.perf_counter()

    monkeys = {}
    with open('inputs/input21.txt', 'r') as file:
        id = 0
        for line in file:
            name, instruction = line.split(":")
            monkeys[name] = Monkey(instruction)

    # First star
    def scream(name):
        monkey = monkeys[name]
        if monkey.scream != None:
            return monkey.scream
        
        m1 = scream(monkey.operand_1)
        m2 = scream(monkey.operand_2)

        monkey.scream = int(eval(str(m1) + monkey.operator + str(m2)))
        return monkey.scream

    score1 = scream("root")

    # Second star:
    score2 = 0

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
