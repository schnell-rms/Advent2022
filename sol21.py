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

        self.has_human_scream = False # aka it includes human input too

def revertOperator_Op1(operator, result, op2):
    match operator:
        case '+':
            return result - op2
        case '-':
            return result + op2
        case '/':
            return result * op2
        case '*':
            return result // op2
    return None

def revertOperator_Op2(operator, result, op1):
    match operator:
        case '+':
            return result - op1
        case '-':
            return op1 - result
        case '/':
            return op1 // result
        case '*':
            return result // op1
    return None

def sol():

    start = time.perf_counter()

    monkeys = {}
    with open('inputs/input21.txt', 'r') as file:
        id = 0
        for line in file:
            name, instruction = line.split(":")
            monkeys[name] = Monkey(instruction)

    monkeys["humn"].has_human_scream = True

    # First star
    def scream(name):
        monkey = monkeys[name]
        if monkey.scream != None:
            return monkey.scream, monkey.has_human_scream
        
        m1, is_human_1 = scream(monkey.operand_1)
        m2, is_human_2 = scream(monkey.operand_2)

        monkey.scream = int(eval(str(m1) + monkey.operator + str(m2)))
        monkey.has_human_scream = is_human_1 or is_human_2
        return monkey.scream, monkey.has_human_scream

    score1, _ = scream("root")

    # Second star:
    def setScream(monkey, value):
        # Set value to this name
        if not hasattr(monkey, "operator"):
            # The human scream:
            monkey.scream = value
            return

        # Has operator:
        if monkeys[monkey.operand_1].has_human_scream:
            fixed_value = monkeys[monkey.operand_2].scream
            needed_value = revertOperator_Op1(monkey.operator, value, fixed_value)
            setScream(monkeys[monkey.operand_1], needed_value)
        else:
            fixed_value = monkeys[monkey.operand_1].scream
            needed_value = revertOperator_Op2(monkey.operator, value, fixed_value)
            setScream(monkeys[monkey.operand_2], needed_value)

    root_monkey = monkeys["root"]

    needed_value = monkeys[root_monkey.operand_1].scream if not monkeys[root_monkey.operand_1].has_human_scream else monkeys[root_monkey.operand_2].scream
    human_monkey = monkeys[root_monkey.operand_1] if monkeys[root_monkey.operand_1].has_human_scream else monkeys[root_monkey.operand_2]

    setScream(human_monkey, needed_value)
    score2 = monkeys["humn"].scream

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
