# %% First Star
# ------------------------------------------------------------------------------

garden = ["#" + line + "#" for line in input.splitlines()]
garden = ["#" * len(garden[0])] + garden + ["#" * len(garden[0])]

py0, px0 = 1, 1
while py0 < len(garden):
    if "S" in garden[py0]:
        while px0 < len(garden[0]):
            if garden[py0][px0] == "S":
                break
            px0 += 1
        break
    py0 += 1

acc = 0
limit = 64
# distances = {(py0, px0): 0}
queue = [(0, py0, px0)]
visited = set()
while len(queue) != 0:
    distance, py, px = queue.pop(0)
    if (py, px) not in visited:
        visited.add((py, px))
        if distance % 2 == 0:
            acc += 1
        if distance < limit:
            for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                py1, px1 = py + dy, px + dx
                if garden[py1][px1] == ".":
                    queue.append((distance + 1, py1, px1))

print(acc)


# %% Second Star
# ------------------------------------------------------------------------------

# I had to look up the solution for this star :(

class Done(Exception):
    pass

garden = input.splitlines()
start = None
n, m = len(garden), len(garden[0])
try:
    for y in range(n):
        for x in range(m):
            if garden[y][x] == "S":
                start = y, x
                garden[y] = garden[y].replace("S", ".")
                raise Done
except Done:
    pass

steps = 26501365
modulo_counts = []
d = 0
boundry = [start]
res = None

while True:
    if d == steps:
        res = len(boundry)
        break
    if len(modulo_counts) == 3:
        a0, a1, a2 = modulo_counts
        b0 = a0
        b1 = a1 - a0
        b2 = a2 - a1
        c = steps // n
        res = b0 + b1 * c + (c * (c - 1) // 2) * (b2 - b1)
        break
    d += 1
    new_boundry = set()
    for y, x in boundry:
        new_boundry.add((y - 1, x))
        new_boundry.add((y + 1, x))
        new_boundry.add((y, x - 1))
        new_boundry.add((y, x + 1))
    boundry = [(y, x) for y, x in new_boundry if garden[y % n][x % m] != "#"]
    if d % n == steps % n:
        modulo_counts.append(len(boundry))

print(res)
