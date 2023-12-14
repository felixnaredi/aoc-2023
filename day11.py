# %% First Star
# ------------------------------------------------------------------------------

lines = input.splitlines()

empty_rows = []
for y, line in enumerate(lines):
    if all((c == "." for c in line)):
        empty_rows.append(y)

empty_columns = []
for x in range(len(lines[0])):
    if all((line[x] == "." for line in lines)):
        empty_columns.append(x)

galaxies = [(y, x) for y in range(len(lines)) for x in range(len(lines[0])) if lines[y][x] == "#"]
pairs = set((min(p1, p2), max(p1, p2)) for p1 in galaxies for p2 in galaxies if p1 != p2)

acc = 0
for (y1, x1), (y2, x2) in pairs:
    dy = abs(y2 - y1) + len([y for y in empty_rows if min(y1, y2) < y < max(y1, y2)])
    dx = abs(x2 - x1) + len([x for x in empty_columns if min(x1, x2) < x < max(x1, x2)])
    acc += dy + dx

print(acc)

# %% Second Star
# ------------------------------------------------------------------------------

lines = input.splitlines()

empty_rows = []
for y, line in enumerate(lines):
    if all((c == "." for c in line)):
        empty_rows.append(y)

empty_columns = []
for x in range(len(lines[0])):
    if all((line[x] == "." for line in lines)):
        empty_columns.append(x)

galaxies = [(y, x) for y in range(len(lines)) for x in range(len(lines[0])) if lines[y][x] == "#"]
pairs = set((min(p1, p2), max(p1, p2)) for p1 in galaxies for p2 in galaxies if p1 != p2)

acc = 0
for (y1, x1), (y2, x2) in pairs:
    dy = abs(y2 - y1) + len([y for y in empty_rows if min(y1, y2) < y < max(y1, y2)]) * 999999
    dx = abs(x2 - x1) + len([x for x in empty_columns if min(x1, x2) < x < max(x1, x2)]) * 999999
    acc += dy + dx

print(acc)
