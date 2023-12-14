# %% First Star
# ------------------------------------------------------------------------------

class Done(Exception):
    pass

def transpose(a):
    b = [[] for _ in range(len(a[0]))]
    for x in range(len(a[0])):
        for y, c in enumerate(a):
            b[x].append(c[x])
            # print(b)
    return ["".join(c) for c in b]

# u = 0
acc = 0
room = []
for line in input.splitlines():
    if line == "":
        try:
            for a, mul in ((room, 100), (transpose(room), 1)):
                old = a[0]
                for i, row in enumerate(a[1:]):
                    # print(i, a)
                    i += 1
                    if row == old:               
                        j = min(i, len(a) - i)
                        # print(len(row), i, j)
                        mirror = True
                        for k in range(j):
                            mirror &= a[i - k - 1] == a[i + k]
                            # print(i, i - k - 1, i + k)
                            # print(a[i - k - 1], a[i + k], a[i - k - 1] == a[i + k])
                        if mirror:
                            # print(i, j)
                            raise Done
                    old = row
        except Done:
            # u += 1
            acc += i * mul
        room.clear()
    else:
        room.append(line)

print(acc)

# %% Second Star
# ------------------------------------------------------------------------------

class Done(Exception):
    pass

def transpose(a):
    b = [[] for _ in range(len(a[0]))]
    for x in range(len(a[0])):
        for y, c in enumerate(a):
            b[x].append(c[x])
            # print(b)
    return ["".join(c) for c in b]

def diff(a, b):
    return len([0 for x, y in zip(a, b) if x != y])

acc = 0
room = []
for line in input.splitlines():
    if line == "":
        try:
            for a, mul in ((room, 100), (transpose(room), 1)):
                for i, x in enumerate(a):
                    for j, y in enumerate(a):
                        if diff(x, y) == 1 and (i + j) % 2 == 1:
                            ok = True
                            k1 = min(i, j) + 1
                            k2 = max(i, j) - 1
                            while k1 <= k2 and -1 < k1 < len(a) and -1 < k2 < len(a):
                                if a[k1] == a[k2]:
                                    k1 += 1
                                    k2 -= 1
                                else:
                                    ok = False
                                    break
                            if ok:
                                k1 = min(i, j) - 1
                                k2 = max(i, j) + 1
                                while -1 < k1 < len(a) and -1 < k2 < len(a):
                                    if a[k1] == a[k2]:
                                        k1 -= 1
                                        k2 += 1
                                    else:
                                        ok = False
                                        break
                            if ok:
                                # print(i, j)
                                acc += ((i + j) // 2 + 1) * mul
                                raise Done

        except Done:
            pass
        room.clear()
        # print()
    else:
        room.append(line)

print(acc)
