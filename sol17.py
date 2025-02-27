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

    def findHeight(nbStones, useHistory):
        stones = cycle(enumerate(kSTONES))
        winds = cycle(enumerate(wind_directions))

        history = {}
        hall = set([x - 0j for x in range(7)])
        def maxHeightNow():
            return max(n.imag for n in hall)

        i = 0
        isCycleFound = False
        while i < nbStones:
            height = maxHeightNow()
            stone_idx, currStone = next(stones)
            curr_stone = { 2 + (height  + 4) * 1j + rock for rock in currStone}

            # print(curr_stone)
            # Fall and windblow:
            while (True):
                # Wind blows:
                wind_idx, wind_dir = next(winds)
                wind_dir = -1 if wind_dir == '<' else 1
                new_stone = { rock + wind_dir for rock in curr_stone }

                if not new_stone & hall and all(rock.real >=0 and rock.real <= 6 for rock in new_stone):
                    curr_stone = new_stone

                # Rock falls:
                new_stone = { rock - 1j for rock in curr_stone}
                if not new_stone & hall:
                    curr_stone = new_stone
                else:
                    hall |= curr_stone
                    break

            if useHistory and not isCycleFound:
                current_heights = [max([rock.imag for rock in hall if rock.real == x]) for x in range(0,7)]
                min_current_height = min(current_heights)
                height_profile = tuple([h - min_current_height for h in current_heights])

                if (stone_idx, wind_idx, height_profile) in history:
                    oldi, max_height_than = history[stone_idx, wind_idx, height_profile]
                    delta_i = i - oldi
                    ncycles = (nbStones - i) // delta_i
                    i += delta_i * ncycles
                    delta_height = maxHeightNow() - max_height_than
                    hall = set([x + delta_height*ncycles * 1j + h*1j for x,h in enumerate(current_heights)])
                    isCycleFound = True
                else:
                    history[stone_idx, wind_idx, height_profile] = i, maxHeightNow()

            i += 1
        return int(max(n.imag for n in hall))

    score1 = findHeight(2022, False)
    score2 = findHeight(1000000000000, True)

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
