
import time

from queue import PriorityQueue


def route(terrain, startX, startY, endX, endY):
    n = len(terrain)
    m = len(terrain[0])

    q = PriorityQueue()

    q.put((0, startX, startY))

    totalCost = 0

    allCosts = {}

    while not q.empty():
        cost, x, y = q.get()
        if (x,y) in allCosts:
            assert(allCosts[(x,y)] <= cost)
            continue

        allCosts[(x,y)] = cost

        if x == endX and y == endY:
            totalCost = cost
            break
        
        if  x > 0 and (ord(terrain[y][x - 1]) - ord(terrain[y][x])) <= 1:
            q.put((cost + 1, x - 1, y))

        if x < m - 1 and (ord(terrain[y][x + 1]) - ord(terrain[y][x])) <= 1:
            q.put((cost + 1, x + 1, y))

        if y > 0 and (ord(terrain[y - 1][x]) - ord(terrain[y][x])) <= 1:
            q.put((cost + 1, x    , y - 1))

        if y < n - 1 and (ord(terrain[y + 1][x]) - ord(terrain[y][x])) <= 1:
            q.put((cost + 1, x    , y + 1))
    
    return totalCost


def routeDown(terrain, startX, startY, destinationLevel):
    n = len(terrain)
    m = len(terrain[0])

    q = PriorityQueue()

    q.put((0, startX, startY))

    totalCost = 0

    allCosts = {}

    while not q.empty():
        cost, x, y = q.get()
        if (x,y) in allCosts:
            assert(allCosts[(x,y)] <= cost)
            continue

        allCosts[(x,y)] = cost

        if destinationLevel == terrain[y][x]:
            totalCost = cost
            break
        
        if  x > 0 and (ord(terrain[y][x - 1]) - ord(terrain[y][x])) >= -1:
            q.put((cost + 1, x - 1, y))

        if x < m - 1 and (ord(terrain[y][x + 1]) - ord(terrain[y][x])) >= -1:
            q.put((cost + 1, x + 1, y))

        if y > 0 and (ord(terrain[y - 1][x]) - ord(terrain[y][x])) >= -1:
            q.put((cost + 1, x    , y - 1))

        if y < n - 1 and (ord(terrain[y + 1][x]) - ord(terrain[y][x])) >= -1:
            q.put((cost + 1, x    , y + 1))
    
    return totalCost

def sol():
    start = time.perf_counter()

    file = open('inputs/input12.txt', 'r')
    terrain = [line.strip() for line in file.readlines()]
    file.close()

    startX = None
    startY = None
    endX = None
    endY = None

    for i in range(len(terrain)):
        if startX == None:
            s = terrain[i].find('S')
            if s != -1:
                startX = s
                startY = i
                terrain[i] = "".join([c if c != 'S' else 'a' for c in terrain[i]])
        if endX == None:
            e = terrain[i].find('E')
            if e != -1:
                endX = e
                endY = i
                terrain[i] = "".join([c if c != 'E' else 'z' for c in terrain[i]])
        if startX != None and endX != None:
            break


    score1 = route(terrain, startX, startY, endX, endY)
    score2 = routeDown(terrain, endX, endY, 'a')

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
