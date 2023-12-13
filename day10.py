# %% First Star
# ------------------------------------------------------------------------------

terrain = {}
for y, line in enumerate(input.splitlines()):
    for x, c in enumerate(line):
        terrain[(y, x)] = c
        if c == "S":
            p0 = y, x

pipes = [
    ("|", ( 1,  0), ("|", "L", "J")),
    ("|", (-1,  0), ("|", "7", "F")),
    ("-", ( 0, -1), ("-", "L", "F")),
    ("-", ( 0,  1), ("-", "7", "J")),
    ("L", (-1,  0), ("|", "7", "F")),
    ("L", ( 0,  1), ("-", "7", "J")),
    ("J", (-1,  0), ("|", "7", "F")),
    ("J", ( 0, -1), ("-", "L", "F")),
    ("7", ( 1,  0), ("|", "L", "J")),
    ("7", ( 0, -1), ("-", "L", "F")),
    ("F", ( 1,  0), ("|", "L", "J")),
    ("F", ( 0,  1), ("-", "7", "J")),
]

graph = {}
for (py, px), c in terrain.items():
    edges = []
    for _, (dy, dx), valid in (entry for entry in pipes if entry[0] == c):
        if terrain.get((py + dy, px + dx)) in valid:
            edges.append((py + dy, px + dx))
        graph[(py, px)] = edges

queue = [(p0[0] + 1, p0[1])]
goal = (p0[0] - 1, p0[1])
back = {}
distance = {(p0[0] + 1, p0[1]): 1}
visited = set()

while len(queue) > 0:
    py, px = queue.pop(0)
    # print(graph[(py, px)])
    if (py, px) not in visited:
        visited.add((py, px))
        if goal == (py, px):
            # print("FOUND")
            break
        for qy, qx in graph[(py, px)]:
            queue.append((qy, qx))
            if d := distance.get((qy, qx)):
                if d < distance[(py, px)] + 1:
                    pass
                else:
                    distance[(qy, qx)] = distance[(py, px)] + 1
                    back[(qy, qx)] = (py, px)
            else:
                distance[(qy, qx)] = distance[(py, px)] + 1
                back[(qy, qx)] = (py, px)

print(distance[goal] // 2 + 1)

# %% Second Star
# ------------------------------------------------------------------------------

lines = input.splitlines()
terrain = {}
for y, line in enumerate(["." * len(lines[0])] + lines + ["." * len(lines[0])]):
    for x, c in enumerate("." + line + "."):
        terrain[(y - 1, x - 1)] = c
        if c == "S":
            p0 = y - 1, x - 1

pipes = [
    ("|", ( 1,  0), ("|", "L", "J")),
    ("|", (-1,  0), ("|", "7", "F")),
    ("-", ( 0, -1), ("-", "L", "F")),
    ("-", ( 0,  1), ("-", "7", "J")),
    ("L", (-1,  0), ("|", "7", "F")),
    ("L", ( 0,  1), ("-", "7", "J")),
    ("J", (-1,  0), ("|", "7", "F")),
    ("J", ( 0, -1), ("-", "L", "F")),
    ("7", ( 1,  0), ("|", "L", "J")),
    ("7", ( 0, -1), ("-", "L", "F")),
    ("F", ( 1,  0), ("|", "L", "J")),
    ("F", ( 0,  1), ("-", "7", "J")),
]

graph = {}
for (py, px), c in terrain.items():
    edges = []
    for _, (dy, dx), valid in (entry for entry in pipes if entry[0] == c):
        if terrain.get((py + dy, px + dx)) in valid:
            edges.append((py + dy, px + dx))
        graph[(py, px)] = edges

start = (p0[0] + 1, p0[1])
goal = (p0[0] - 1, p0[1])
queue = [start]
back = {}
distance = {start: 1}
visited = set()

while len(queue) > 0:
    py, px = queue.pop(0)
    if (py, px) not in visited:
        visited.add((py, px))
        if goal == (py, px):
            # print("FOUND")
            break
        for qy, qx in graph[(py, px)]:
            queue.append((qy, qx))
            if d := distance.get((qy, qx)):
                if d < distance[(py, px)] + 1:
                    pass
                else:
                    distance[(qy, qx)] = distance[(py, px)] + 1
                    back[(qy, qx)] = (py, px)
            else:
                distance[(qy, qx)] = distance[(py, px)] + 1
                back[(qy, qx)] = (py, px)

terrain[p0] = "|"

loop = set()
loop.add(start)
loop.add(goal)
loop.add(p0)
node = back[goal]
while node != start:
    loop.add(node)
    node = back[node]

zoom = {
    "|": [
        ".*.",
        ".*.",
        ".*.",
    ],
    "-": [
        "...",
        "***",
        "...",
    ],
    "L": [
        ".*.",
        ".**",
        "...",
    ],
    "J": [
        ".*.",
        "**.",
        "...",
    ],
    "F": [
        "...",
        ".**",
        ".*.",
    ],
    "7": [
        "...",
        "**.",
        ".*.",
    ],
    ".": [
        "...",
        "...",
        "...",
    ]
}


graph = {}
for py, px in loop:
    pipe = terrain[(py, px)]
    for dy, line in enumerate(zoom[pipe]):
        for dx, c in enumerate(line):
            graph[(py * 3 + dy, px * 3 + dx)] = c

ys = [y for y, _ in terrain.keys()]
xs = [x for _, x in terrain.keys()]
for y in range(min(ys) * 3, max(ys) * 3):
    for x in range(min(xs) * 3, max(xs) * 3):
        if c := graph.get((y, x)):
            graph[(y, x)] = c
        else:
            graph[(y, x)] = "."

queue = [(-1, -1)]
visited = set()
while len(queue) > 0:
    py, px = queue.pop(0)
    if (py, px) not in visited:
        visited.add((py, px))
        for dy, dx in ((dy, dx) for dy in (-1, 0, 1) for dx in (-1, 0, 1) if (dy, dx) != (0, 0)):
            q = (py + dy, px + dx)
            if c := graph.get(q):
                if c == ".":
                    queue.append(q)

#
# Print graph and visited nodes.
# 
# for y in range(min(ys) * 3, max(ys) * 3):
#     for x in range(min(xs) * 3, max(xs) * 3):
#         if c := graph.get((y, x)):
#             print(c, end="")
#         else:
#             print(".", end="")
#     print()
# print()
# for y in range(min(ys) * 3, max(ys) * 3):
#     for x in range(min(xs) * 3, max(xs) * 3):
#         if (y, x) in visited:
#             print("x", end="")
#         else:
#             print(".", end="")
#     print()

reject = set()
for y, x in visited:
    reject.add((y // 3, x // 3))

enclosed = set(
    ((y, x) for y, x in terrain.keys()
     if y != min(ys) and y != max(ys) and x != min(xs) and x != max(xs))
).difference(reject)

print(len(enclosed))
