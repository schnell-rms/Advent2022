
import time

import utils


class Monkey:
    def __init__(self):
        self.worries = []
        self.add_term = None
        self.mul_term = None
        self.test_div = 1
        self.true_monkey = 0
        self.false_monkey = 0
        self.inspect_counter = 0

    def op(self, worry):
        if self.add_term != None:
            return worry + self.add_term
        elif self.mul_term != None:
            return worry * self.mul_term
        else:
            return worry * worry

    def test(self, worry):
        return worry % self.test_div == 0

    def receiveItem(self, worry):
        self.worries.append(worry)

    def process(self, allMonkeys):
        for worry in self.worries:
            worry = self.op(worry)
            worry //= 3
            if self.test(worry):
                allMonkeys[self.true_monkey].receiveItem(worry)
            else:
                allMonkeys[self.false_monkey].receiveItem(worry)

        self.inspect_counter += len(self.worries)
        self.worries.clear()

def sol():
    start = time.perf_counter()

    file = open('inputs/input11.txt', 'r')

# The file contains things like these:
#
# Monkey 0:
#   Starting items: 65, 78
#   Operation: new = old * 3
#   Test: divisible by 5
#     If true: throw to monkey 2
#     If false: throw to monkey 3

    monkey_line = ""
    while "Monkey" != monkey_line[0:6]:
        monkey_line = file.readline()

    monkeys = []
    while("Monkey" == monkey_line[0:6]):
        monkeys.append(Monkey())
        assert(utils.firstNumber(monkey_line) == len(monkeys) - 1)

        #Starting items:
        monkeys[-1].worries = utils.extractAllNumbers(file.readline())

        # Operation line:
        operation_line = file.readline()
        if '*' in operation_line:
            monkeys[-1].mul_term = utils.firstNumber(operation_line)
        else:
            monkeys[-1].add_term = utils.firstNumber(operation_line)

        # Test line
        monkeys[-1].test_div = utils.firstNumber(file.readline())
        # True line
        monkeys[-1].true_monkey = utils.firstNumber(file.readline())
        # False line
        monkeys[-1].false_monkey = utils.firstNumber(file.readline())

        monkey_line = file.readline()
        while monkey_line!= "" and "Monkey" != monkey_line[0:6]:
            monkey_line = file.readline()

    file.close()

    for i in range(20):
        for m in monkeys:
            m.process(monkeys)

    inpect_counts = [m.inspect_counter for m in monkeys]
    score1 = max(inpect_counts)
    inpect_counts.remove(score1)
    score1 *= max(inpect_counts)

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    return

if __name__ == "__main__":
    sol()
