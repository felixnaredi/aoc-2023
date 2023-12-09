# %% First Star
# ------------------------------------------------------------------------------

s = 0
for line in input.splitlines():
    last = []
    ys = [int(s) for s in line.split(" ")]
    xs = [x for x in ys]
    while not all((x == 0 for x in xs)):
        xs = [x2 - x1 for x1, x2 in zip(xs, xs[1:])]
        last.append(xs[-1])
    s += ys[-1] + sum(last)

print(s)

# %% Second Star
# ------------------------------------------------------------------------------

s = 0
for line in input.splitlines():
    ys = [int(s) for s in line.split(" ")]
    xs = [x for x in ys]
    first = [xs[0]]
    while not all((x == 0 for x in xs)):
        xs = [x2 - x1 for x1, x2 in zip(xs, xs[1:])]
        first.append(xs[0])
    print(first)
    x = 0
    for y in reversed(first):
        x = y - x
    s += x

print(s)
