# %% First Star
# ------------------------------------------------------------------------------

from heapq import heappop, heappush

class Done(Exception):
    pass

lines = ["#" + line + "#" for line in input.splitlines()]
lines = ["#" * len(lines[0])] + lines + ["#" * len(lines[0])]

start = (1, 2)
goal = (len(lines) - 2, len(lines[0]) - 3)

tree = {}
visited = set()
queue = [start]
while len(queue) != 0:
    (py, px) = queue.pop()
    if (py, px) not in visited:
        visited.add((py, px))
        tree[(py, px)] = []
        for (dy, dx) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            y, x = py + dy, px + dx
            if (y, x) not in visited:
                c = lines[y][x]
                if c == "#":
                    continue
                elif c == ".":
                    tree[(py, px)].append((y, x))
                    queue.append((y, x))
                elif c == "v" and dy == 1:
                    tree[(py, px)].append((y + 1, x))
                    queue.append((y + 1, x))
                elif c == "<" and dx == -1:
                    tree[(py, px)].append((y, x - 1))
                    queue.append((y, x - 1))
                elif c == ">" and dx == 1:
                    tree[(py, px)].append((y, x + 1))
                    queue.append((y, x + 1))

goal_distance = []
visited = set()
queue = [(0, start)]
try:
    while len(queue) != 0:
        distance, (py, px) = heappop(queue)
        if (py, px) not in visited:
            # visited.add((py, px))
            for y, x in tree[(py, px)]:
                if (y, x) == goal:
                    goal_distance.append(distance)
                # else:
                heappush(queue, (distance + abs(py - y) + abs(px - x), (y, x)))
except Done:
    pass

print(max(goal_distance) + 1)


# %% Second Star
# ------------------------------------------------------------------------------

