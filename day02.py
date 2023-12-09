# %% First Star
# ------------------------------------------------------------------------------

sum = 0
for p, line in enumerate(input.splitlines()):
    p += 1
    i = 0
    while line[i] != ":":
        i += 1
    i += 2
    xs = line[i:].split(" ")
    for n, c in zip(xs[0::2], xs[1::2]):
        n = int(n)
        if "red" in c and n > 12:
            # print(n, c)
            p = 0
        if "green" in c and n > 13:
            # print(n, c)
            p = 0
        if "blue" in c and n > 14:
            # print(n, c)
            p = 0
    sum += p

print(sum)

# %% Second Star
# ------------------------------------------------------------------------------

sum = 0
for p, line in enumerate(input.splitlines()):
    p += 1
    i = 0
    while line[i] != ":":
        i += 1
    i += 2
    xs = line[i:].split(" ")
    r, g, b = 0, 0, 0
    for n, c in zip(xs[0::2], xs[1::2]):
        n = int(n)
        if "red" in c:
            r = max(r, n)
        if "green" in c:
            g = max(g, n)
        if "blue" in c:
            b = max(b, n)
    sum += r * g * b

print(sum)