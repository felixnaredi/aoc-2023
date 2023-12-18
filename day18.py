# %% First Star
# ------------------------------------------------------------------------------

SIZE = 1000
ground = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
py, px = 250, 250
for line in input.splitlines():
    d, w, _ = line.split(" ")
    w = int(w)
    if d == "U":
        for _ in range(w):
            ground[py][px] = 1
            py -= 1
    if d == "D":
        for _ in range(w):
            ground[py][px] = 1
            py += 1
    if d == "L":
        for _ in range(w):
            ground[py][px] = 1
            px -= 1
    if d == "R":
        for _ in range(w):
            ground[py][px] = 1
            px += 1

i = 1
while all((c == 0 for c in ground[i])):
    i += 1
j = 1
while ground[i][j] != 1:
    j += 1

i += 1
j += 1
queue = [(i, j)]

while len(queue) != 0:
    y, x = queue.pop()
    if ground[y][x] == 0:
        ground[y][x] = 1
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            queue.append((y + dy, x + dx))

# for row in ground:
#     print("".join(("." if c == 0 else "#" for c in row)))
#     print(row)

print(sum((sum(row) for row in ground)))


# %% Second Star
# ------------------------------------------------------------------------------

points = []
py, px = 0, 0
for line in input.splitlines():
    _, _, hex = line.split(" ")
    w = int(hex[2 : -2], 16)
    d = int(hex[-2], 16)
    if d == 0:
        points.append(((py, px), (py, px + w)))
        py, px = py, px + w
    if d == 1:
        points.append(((py, px), (py + w, px)))
        py, px = py + w, px
    if d == 2:
        points.append(((py, px), (py, px - w)))
        py, px = py, px - w
    if d == 3:
        points.append(((py, px), (py - w, px)))
        py, px = py - w, px

# Trapezoid formula
# https://en.wikipedia.org/wiki/Shoelace_formula#Trapezoid_formula_2
a = 0
for (y0, x0), (y1, x1) in points:
    a += (y0 + y1) * (x0 - x1)
    a += abs(y0 - y1) + abs(x0 - x1)

print(a // 2 + 1)
