#
# NOTE:
#   Replace all \ in the input with J
#

# %% First Star
# ------------------------------------------------------------------------------

room = []
for line in input.splitlines():
    room.append("x" + line + "x")
room = ["x" * len(room[0])] + room + ["x" * len(room[0])]

visited = set()
energized = set()
beams = [((1, 1), (0, 1))]

while len(beams) != 0:
    (py, px), (dy, dx) = beams.pop()
    if ((py, px), (dy, dx)) not in visited:
        visited.add(((py, px), (dy, dx)))
        c = room[py][px]
        # print(c, (py, px), (dy, dx), len(energized), len(beams))
        if c == "x":
            continue
        elif c == "/":
            if (dy, dx) == (-1, 0):
                (dy, dx) = (0, 1)
            elif (dy, dx) == (1, 0):
                (dy, dx) = (0, -1)
            elif (dy, dx) == (0, -1):
                (dy, dx) = (1, 0)
            elif (dy, dx) == (0, 1):
                (dy, dx) = (-1, 0)
        elif c == "J":
            if (dy, dx) == (-1, 0):
                (dy, dx) = (0, -1)
            elif (dy, dx) == (1, 0):
                (dy, dx) = (0, 1)
            elif (dy, dx) == (0, -1):
                (dy, dx) = (-1, 0)
            elif (dy, dx) == (0, 1):
                (dy, dx) = (1, 0)
        elif c == "|":
            if dx != 0 and (py, px):
                (dy, dx) = (-1, 0)
                beams.append(((py + 1, px), (1, 0)))
        elif c == "-":
            if dy != 0 and (py, px):
                (dy, dx) = (0, -1)
                beams.append(((py, px + 1), (0, 1)))
        energized.add((py, px))
        beams.append(((py + dy, px + dx), (dy, dx)))

# for y, row in enumerate(room):
#     for x, c in enumerate(row):
#         if (y, x) in energized:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()

print(len(energized))

# %% Second Star
# ------------------------------------------------------------------------------

room = []
for line in input.splitlines():
    room.append("x" + line + "x")
room = ["x" * len(room[0])] + room + ["x" * len(room[0])]

acc = 0

def run(init):
    beams = [init]
    visited = set()
    energized = set()
    while len(beams) != 0:
        (py, px), (dy, dx) = beams.pop()
        if ((py, px), (dy, dx)) not in visited:
            visited.add(((py, px), (dy, dx)))
            c = room[py][px]
            # print(c, (py, px), (dy, dx), len(energized), len(beams))
            if c == "x":
                continue
            elif c == "/":
                if (dy, dx) == (-1, 0):
                    (dy, dx) = (0, 1)
                elif (dy, dx) == (1, 0):
                    (dy, dx) = (0, -1)
                elif (dy, dx) == (0, -1):
                    (dy, dx) = (1, 0)
                elif (dy, dx) == (0, 1):
                    (dy, dx) = (-1, 0)
            elif c == "J":
                if (dy, dx) == (-1, 0):
                    (dy, dx) = (0, -1)
                elif (dy, dx) == (1, 0):
                    (dy, dx) = (0, 1)
                elif (dy, dx) == (0, -1):
                    (dy, dx) = (-1, 0)
                elif (dy, dx) == (0, 1):
                    (dy, dx) = (1, 0)
            elif c == "|":
                if dx != 0 and (py, px):
                    (dy, dx) = (-1, 0)
                    beams.append(((py + 1, px), (1, 0)))
            elif c == "-":
                if dy != 0 and (py, px):
                    (dy, dx) = (0, -1)
                    beams.append(((py, px + 1), (0, 1)))
            energized.add((py, px))
            beams.append(((py + dy, px + dx), (dy, dx)))
    return len(energized)

for x in range(len(room[0]) - 2):
    acc = max(acc, run(((1, x + 1), (1, 0))))
for x in range(len(room[0]) - 2):
    acc = max(acc, run(((len(room) - 2, x + 1), (-1, 0))))
for y in range(len(room) - 2):
    acc = max(acc, run(((y + 1, 1), (1, 0))))
for y in range(len(room) - 2):
    acc = max(acc, run(((y + 1, len(room[0]) - 2), (0, -1))))

print(acc)