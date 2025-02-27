import time
import sys
import utils

def neighbours(xyz):
    x , y, z = xyz
    return {(x,y,z-1),(x,y,z+1),(x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z)}

def countFaces(shape):
    nbFaces = len(shape) * 6
    for cube in shape:
        nbFaces -= len(shape & neighbours(cube))
    return nbFaces

def sol():
    start = time.perf_counter()

    droplet = set()
    with open('inputs/input18.txt', 'r') as file:
        for line in file:
            droplet.add(tuple(utils.extractAllNumbers(line)))

    # First star
    score1 = countFaces(droplet)

    # Second star:
    x_min = min([cube[0] for cube in droplet]) - 1
    x_max = max([cube[0] for cube in droplet]) + 1
    y_min = min([cube[1] for cube in droplet]) - 1
    y_max = max([cube[1] for cube in droplet]) + 1
    z_min = min([cube[2] for cube in droplet]) - 1
    z_max = max([cube[2] for cube in droplet]) + 1

    empty_space = set()
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            for z in range(z_min, z_max + 1):
                empty_space.add((x,y,z))
    empty_space -= droplet

    sys.setrecursionlimit(15000)

    def findInnerSpace(cube, space: set):
        if cube not in space:
            return

        space.remove(cube)  
        nei = neighbours(cube) & space

        for other in nei:
            findInnerSpace(other, space)

    findInnerSpace((0,0,0), empty_space)
    score2 = score1 - countFaces(empty_space)

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
