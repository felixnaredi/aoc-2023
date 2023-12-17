# %% First Star
# ------------------------------------------------------------------------------

from heapq import heappush, heappop

class Done(Exception):
    pass

city = [[0] + [int(c) for c in line] + [0] for line in input.splitlines()]
city = [[0] * len(city[0])] + city + [[0] * len(city[0])]

result = -1
visited = set()
distance = {}
queue = [(0, (1, 1), (1, 0), None), (0, (1, 1), (0, 1), None)]
goal = len(city) - 2, len(city[0]) - 2

try:
    while len(queue) != 0:
        dist, (py0, px0), (dy0, dx0), prev = heappop(queue)
        # print(dist, (py0, px0), (dy0, dx0), prev)
        if ((py0, px0), prev) not in visited:
            if (py0, px0) == goal:
                result = dist
                raise Done
            for dy, dx in ((dx0, dy0), (-dx0, -dy0)):
                py, px = py0, px0
                cost = 0
                for _ in range(3):
                    py, px = py + dy, px + dx
                    # print("  ", (py, px), (dy, dx))
                    if city[py][px] == 0:
                        break
                    cost += city[py][px]
                    key = (py0, px0), (py, px)
                    if key not in distance.keys() or distance[key] > dist + cost:
                        distance[key] = dist + cost
                        heappush(queue, (dist + cost, (py, px), (dy, dx), (py0, px0)))
except Done:
    pass

print(result)

# %% Second Star
# ------------------------------------------------------------------------------

from heapq import heappush, heappop

class Done(Exception):
    pass

city = [[0] + [int(c) for c in line] + [0] for line in input.splitlines()]
city = [[0] * len(city[0])] + city + [[0] * len(city[0])]

visited = set()
distance = {}
queue = [(0, (1, 1), (1, 0), None), (0, (1, 1), (0, 1), None)]
goal = len(city) - 2, len(city[0]) - 2

try:
    while len(queue) != 0:
        dist, (py0, px0), (dy0, dx0), prev = heappop(queue)
        # print(dist, (py0, px0), (dy0, dx0), prev)
        if ((py0, px0), prev) not in visited:
            if (py0, px0) == goal:
                result = dist
                raise Done
            for dy, dx in ((dx0, dy0), (-dx0, -dy0)):
                py, px = py0, px0
                cost = 0
                for i in range(1, 11):
                    py, px = py + dy, px + dx
                    # print("  ", (py, px), (dy, dx))
                    if city[py][px] == 0:
                        break
                    cost += city[py][px]
                    if i > 3:
                        key = (py0, px0), (py, px)
                        if key not in distance.keys() or distance[key] > dist + cost:
                            distance[key] = dist + cost
                            heappush(queue, (dist + cost, (py, px), (dy, dx), (py0, px0)))
except Done:
    pass

print(result)
