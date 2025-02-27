import time

from itertools import cycle

kSTONES = [
    {0 + 0j, 1 + 0j, 2 + 0j, 3 + 0j},
    {1 + 2j, 0 + 1j, 1 + 1j, 2 + 1j, 1 + 0j},
    {2 + 2j, 2 + 1j, 0 + 0j, 1 + 0j, 2 + 0j},
    {0 + 3j, 0 + 2j, 0 + 1j, 0 + 0j},
    {0 + 1j, 1 + 1j, 0 + 0j, 1 + 0j}]


def sol():
    start = time.perf_counter()

    file = open('inputs/input17.txt', 'r')
    wind_directions = file.readline()
    file.close()


    stones = cycle(kSTONES)
    winds = cycle(wind_directions)


    hall = set([x - 0j for x in range(7)])

    for i in range(2022):
        height = max(n.imag for n in hall)
        curr_stone = { 2 + (height  + 4) * 1j + rock for rock in next(stones)}

        # print(curr_stone)
        # Fall and windblow:
        while (True):
            # Wind blows:
            windDir =  -1 if next(winds) == '<' else 1
            new_stone = { rock + windDir for rock in curr_stone}

            if not new_stone & hall and all(rock.real >=0 and rock.real <= 6 for rock in new_stone):
                curr_stone = new_stone

            # Rock falls:
            new_stone = { rock - 1j for rock in curr_stone}
            if not new_stone & hall:
                curr_stone = new_stone
            else:
                hall |= curr_stone
                break

    score1 = int(max(n.imag for n in hall))
    score2 = 0

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
