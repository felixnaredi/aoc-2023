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

