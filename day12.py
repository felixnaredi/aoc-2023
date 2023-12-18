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

import re

acc = 0

for line in input.splitlines():
    records, groups = line.split(" ")
    records = "." + "?".join([records] * 5) + "."
    groups = [int(c) for c in groups.split(",")]
    groups *= 5
    # print(records, groups)

    m = {}
    def opt(i, j0, j, recs):
        if not (i, j0, j) in m.keys():
            # print(i, j0, j, recs)
            size = groups[i]
            if (j + size < len(recs)
                and recs[j - 1] in (".", "?")
                and recs[j + size] in (".", "?")
                and all((c in ("#", "?") for c in recs[j : j + size]))
            ):
                recs1 = recs[:]
                for k in range(size):
                    recs1[j + k] = "#"
                s = "".join(recs1[: j + size + 1])
                s = re.split("\.|\?", s)
                s = [len(g) for g in s if g != ""]
                if s == groups[: i + 1]:
                    if len(groups) == i + 1:
                        s = "".join(recs1)
                        s = re.split("\.|\?", s)
                        s = [len(g) for g in s if g != ""]
                        if s == groups:
                            m[(i, j0, j)] = 1
                        else:
                            m[(i, j0, j)] = 0
                    else:
                        m[(i, j0, j)] = sum((opt(i + 1, j, k, recs1)
                                             for k in range(j + size + 1, len(recs1))))
                else:
                    m[(i, j0, j)] = 0
            else:
                m[(i, j0, j)] = 0
        return m[(i, j0, j)]
    
    k = sum((opt(0, 0, j + 1, list(records)) for j in range(len(records))))
    acc += k
    # print(k, acc)

#     for j in range(len(records) - 1):
#         print(opt(0, j + 1, list(records)), m)

print(acc)