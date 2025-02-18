
import time

import utils

class Tree:
    def __init__(self, parent):
        self.parent = parent
        self.dirs = {}
        self.file_sizes = []

    # ignore the file name
    def addFile(self, file_size):
        assert(isinstance(file_size, int))
        self.file_sizes.append(file_size)

    def addFolder(self, folder_name):
        if folder_name not in self.dirs:
            self.dirs[folder_name] = Tree(self)

    def folder(self, folder_name):
        assert(folder_name in self.dirs)
        return self.dirs[folder_name]

    def fullsz(self):
        full_size = sum(self.file_sizes)
        for _, dir in self.dirs.items():
            full_size += dir.fullsz()

        return full_size
    
    def firstStar(self, star):
        sz = sum(self.file_sizes)

        for _, dir in self.dirs.items():
            sz += dir.firstStar(star)

        if (sz <= 100000):
            star[0] += sz
        return sz

    def secondStar(self, star, neededSpace):
        sz = sum(self.file_sizes)

        for _, dir in self.dirs.items():
            sz += dir.secondStar(star, neededSpace)

        if sz >= neededSpace and sz < star[0]:
            star[0] = sz
        return sz

def sol():
    start = time.perf_counter()

    disk = Tree(None)
    disk.addFolder(r"/")
    currentPos = disk
    with open('inputs/input07.txt', 'r') as file:
        for line in file:
            if line[:4] == '$ cd':
                folder_name = line[5:-1] #or just .strip() to remove also trailing spaces, if any
                if ".." == folder_name:
                    assert(currentPos != None)
                    currentPos = currentPos.parent
                else:
                    currentPos = currentPos.folder(folder_name)
            elif line[:4] == "$ ls":
                pass
            elif line[:3] == "dir":
                folder_name = line[4:-1]
                currentPos.addFolder(folder_name)
            elif not line.isspace():
                file_sz = utils.extractAllNumbers(line)
                currentPos.addFile(file_sz[0])

    score1 = [0]
    disk.firstStar(score1)

    freeSpace = 70000000 - disk.fullsz()
    neededSpace = 30000000 - freeSpace

    score2 = [70000000]
    disk.secondStar(score2, neededSpace)

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1[0])
    print("Second star: ", score2[0])
    return

if __name__ == "__main__":
    sol()
