import math
import time

from collections import defaultdict

from functools import cache

import re

def sol():
    start = time.perf_counter()

    rates = {}

    distance = defaultdict(lambda: defaultdict(lambda: math.inf))

    with open('inputs/input16.txt', 'r') as file:
        for line in file:
            valve = re.findall('[A-Z]{2}', line)
            assert(len(valve) > 1)
            m = re.search("rate=(\\d+)", line)
            assert(m != None)
            rates[valve[0]] = int(m.group(1))

            distance[valve[0]][valve[0]] = 0
            for tunnel  in valve[1:]:
                distance[valve[0]][tunnel] = 1

    to_activate = frozenset([key for key, rate in rates.items() if rate > 0])

    for t in rates:
        for a in rates:
            for b in rates:
                distance[a][b] = min(distance[a][b], distance[a][t] + distance[t][b])

    @cache
    def search(name, remaining_time, still_to_activate):
        flow = 0
        for tunnel in still_to_activate:
            cost = distance[name][tunnel] + 1
            if cost <= remaining_time:
                flow = max(flow, rates[tunnel] * (remaining_time - cost)  + search(tunnel, remaining_time - cost, still_to_activate - {tunnel}) )
        return flow

    score1 = search("AA", 30, to_activate)

    @cache
    def searchE(name, remaining_time, still_to_activate, isElephant):
        # Could the remaining ones be better activated by the human?
        flow = searchE("AA", 26, still_to_activate, False) if isElephant else 0
        # or by the elephant:
        for tunnel in still_to_activate:
            cost = distance[name][tunnel] + 1
            if cost <= remaining_time:
                flow = max(flow, rates[tunnel] * (remaining_time - cost)  + searchE(tunnel, remaining_time - cost, still_to_activate - {tunnel}, isElephant) )
        return flow

    # Too slow, many redundant calls name <-> name_E
    @cache
    def searchWithElephant(name, name_E, remaining_time, remaining_time_E, still_to_activate):
        flow = 0
        for tunnel in still_to_activate:
            # Who goes into this tunnel: the human?
            cost = distance[name][tunnel] + 1
            if cost <= remaining_time:
                flow = max(flow, rates[tunnel] * (remaining_time - cost)  + searchWithElephant(tunnel, name_E, remaining_time - cost, remaining_time_E, still_to_activate - {tunnel}) )

            # Or the elephant?
            cost_E = distance[name_E][tunnel] + 1
            if cost_E <= remaining_time_E:
                flow = max(flow, rates[tunnel] * (remaining_time_E - cost_E)  + searchWithElephant(name, tunnel, remaining_time, remaining_time_E - cost_E, still_to_activate - {tunnel}) )
        return flow
    # Too slow:
    # score2 = searchWithElephant("AA", "AA", 26, 26, to_activate)

    score2 = searchE("AA", 26, to_activate, True)

    end = time.perf_counter()

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return

if __name__ == "__main__":
    sol()
