# %% First Star
# ------------------------------------------------------------------------------

import re

X, M, A, S = 0, 1, 2, 3

parse_workflow = True
workflows = {}
parts = []

for line in input.splitlines():
    if parse_workflow:
        if line == "":
            parse_workflow = False
        else:
            lbl, stm = re.match("(.+){(.+)}", line).groups()
            workflows[lbl] = stm
    else:
        part = []
        for y in line[1:-1].split(","):
            part.append(int(y.split("=")[1]))
        parts.append(part)

# print(*workflows.values(), sep="\n")

acc = 0
for part in parts:
    w = "in"
    while w != "A" and w != "R":
        stm = workflows[w]
        while m := re.match("(x|m|a|s)(<|>)(\d+):([^,]+),(.+)", stm):
            prop, cmp, val, t, f = m.groups()
            # print(prop, cmp, val, t, f)
            if prop == "x":
                v = part[X]
            elif prop == "m":
                v = part[M]
            elif prop == "a":
                v = part[A]
            elif prop == "s":
                v = part[S]
            else:
                raise SyntaxError(f"Invalid prop '{prop}'")

            if cmp == "<":
                b = v < int(val)
            elif cmp == ">":
                b = v > int(val)
            else:
                SyntaxError(f"Invalid comparator '{cmp}'")

            stm = t if b else f
        w = stm
    # print(part, w)
    if w == "A":
        acc += sum(part)

print(acc)


# %% Second Star
# ------------------------------------------------------------------------------

import re

prop_index = {
    "x": 0,
    "m": 1,
    "a": 2,
    "s": 3,
}

workflows = {}
for line in input.splitlines():
    if line == "":
        break
    else:
        lbl, stm = re.match("(.+){(.+)}", line).groups()
        workflows[lbl] = stm

acc = 0
queue = [("in", [(1, 4000), (1, 4000), (1, 4000), (1, 4000)])]
while len(queue) != 0:
    stm, props = queue.pop()
    # print(stm, props)
    if m := re.match("(x|m|a|s)(<|>)(\d+):([^,]+),(.+)", stm):
        prop, cmp, val, t, f = m.groups()
        prop = prop_index[prop]
        val = int(val)
        lo, hi = props[prop]
        if cmp == "<":
            props_t, props_f = props[:], props[:]
            props_t[prop] = lo, min(hi, val - 1)
            queue.append((t, props_t))
            props_f[prop] = max(lo, val), hi
            queue.append((f, props_f))
        elif cmp == ">" and val > lo:
            props_t, props_f = props[:], props[:]
            props_t[prop] = max(lo, val + 1), hi
            queue.append((t, props_t))
            props_f[prop] = lo, min(hi, val)
            queue.append((f, props_f))
        else:
            raise SyntaxError(f"Invalid comparator '{cmp}'")
    elif stm == "A":
        k = 1
        if all((hi >= lo) for lo, hi in props):
            for lo, hi in props:
                k *= hi - lo + 1
            acc += k
        # print(k, acc)
    elif stm == "R":
        # print("reject")
        pass
    elif stm := workflows.get(stm):
        queue.append((stm, props))
    else:
        raise SyntaxError(f"Invalid statement '{stm}'")
    
print(acc)
