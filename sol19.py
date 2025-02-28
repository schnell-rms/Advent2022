import math
import time

import utils


from functools import cache

class myTuple(tuple):
    def __sub__(self, other):
        return  myTuple(x - y for x, y in zip(self,other))

    def __add__(self, other):
        return myTuple(x + y for x, y in zip(self, other))

    def __mul__(self, other:int):
        return myTuple(x * other for x in self)

class BluePrint:
    def __init__(self, nums):
        self.id = nums[0]
        self.cost_ore_robot         = myTuple((nums[1], 0,       0,          0))
        self.cost_clay_robot        = myTuple((nums[2], 0,       0,          0))
        self.cost_obsidian_robot    = myTuple((nums[3], nums[4], 0,          0))
        self.cost_geode_robot       = myTuple((nums[5], 0,       nums[6],    0))

        # Maximum robots of one kind to produce for collecting building materials:
        self.max_ore_robot      = max(nums[1],nums[2],nums[3], nums[5])
        self.max_clay_robot     = nums[4]
        self.max_obsidian_robot = nums[6]

        self.max_geodes_up_to_now = 0

    def waitTime(self,
                 available_resources: myTuple,
                 needed_resources: myTuple,
                 robots: myTuple):
        missing_resources = needed_resources - available_resources
        for i in range(3):
            if missing_resources[i] > 0 and robots[i] == 0:
                return math.inf
        return max( math.ceil(missing_resources[i] / robots[i]) if missing_resources[i] > 0 else 0 for i in range(0,3)) + 1

    @cache
    def solve(self, time, resources: myTuple, robots: myTuple):

        ret = resources[3] + robots[3] * time
        self.max_geodes_up_to_now = max(self.max_geodes_up_to_now, ret)

        if time == 0:
            return ret
        
        # What if creating at every next step a geode robot? 
        if ret + time * (time + 1) // 2 <= self.max_geodes_up_to_now:
            return ret
        
        oreRobotTime = self.waitTime(resources, self.cost_ore_robot, robots)
        if time >= oreRobotTime and robots[0] < self.max_ore_robot:
            ret = max(ret, self.solve(time - oreRobotTime, resources + robots * oreRobotTime - self.cost_ore_robot, robots + myTuple((1,0,0,0))))

        clayRobotTime = self.waitTime(resources, self.cost_clay_robot, robots)
        if time >= clayRobotTime and robots[1] < self.max_clay_robot:
            ret = max(ret,self.solve(time - clayRobotTime, resources + robots * clayRobotTime - self.cost_clay_robot, robots + myTuple((0,1,0,0))))

        obsidianRobotTime = self.waitTime(resources, self.cost_obsidian_robot, robots)
        if time >= obsidianRobotTime and robots[2] < self.max_obsidian_robot:
            ret = max(ret,self.solve(time - obsidianRobotTime, resources + robots * obsidianRobotTime - self.cost_obsidian_robot, robots + myTuple((0,0,1,0))))

        geodeRobotTime = self.waitTime(resources, self.cost_geode_robot, robots)
        if time >= geodeRobotTime:
            ret = max(ret,self.solve(time - geodeRobotTime, resources + robots * geodeRobotTime - self.cost_geode_robot, robots + myTuple((0,0,0,1))))

        self.max_geodes_up_to_now = max(self.max_geodes_up_to_now, ret)
        return ret

    def score(self, time):
        return self.id * self.solve(time, myTuple((0,0,0,0)), myTuple((1,0,0,0)))

def sol():
    start = time.perf_counter()

    blue_prints = []
    with open('inputs/input19.txt', 'r') as file:
        for line in file:
            blue_prints.append(BluePrint(utils.extractAllNumbers(line)))

    # First star
    score1 = sum(x.score(24) for x in blue_prints)

    # Second star:
    score2 = math.prod([x.solve(32,myTuple((0,0,0,0)), myTuple((1,0,0,0))) for x in blue_prints[:3]])

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
