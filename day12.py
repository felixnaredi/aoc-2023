# %% First Star
# ------------------------------------------------------------------------------

import re

acc = 0

for line in input.splitlines():
    conditions, groups = line.split(" ")
    groups = [int(size) for size in groups.split(",")]
    # print(conditions, groups)
    a1 = [(0, conditions)]
    patterns = set()
    for g, size in enumerate(groups):
        a2 = []
        # print(size, a1)
        for bgn, cs1 in a1:
            for i in range(bgn, len(cs1)):
                # print(bgn, i, cs1, a2)
                fit = True
                cs = [c for c in cs1]
                for j in range(i, i + size):
                    if j < len(cs) and cs[j] != ".":
                        cs[j] = "#"
                    else:
                        fit = False
                if fit:
                    cs = "".join(cs)
                    j = cs[i:].find("#" * size)
                    j = j + i if j > -1 else j
                    # print(i, j, cs)
                    xs = [len(c) for c in re.split("\.|\?", cs) if c != ""]
                    if xs[g] == size:
                        if j == i:
                            a2.append((i + size + 1, cs))
                            if xs == groups:
                                patterns.add(cs)
                                # print(patterns)
        a1 = a2
    # print(a1)
    print("patterns:", len(patterns))
    acc += len(patterns)

print(acc)

# %% Second Star
# ------------------------------------------------------------------------------

