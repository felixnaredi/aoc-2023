# %% First Star
# ------------------------------------------------------------------------------

acc = 0
k = 0
for c in input:
    if c != ",":
        # print(c, end="")
        k += ord(c)
        k *= 17
        k %= 256
    else:
        # print()
        # print(k)
        acc += k
        k = 0

print(acc)

# %% Second Star
# ------------------------------------------------------------------------------

h = [[] for _ in range(256)]
cs = ""
op = None
for c in input:
    if op:
        k = 0
        for x in cs:
            k += ord(x)
            k *= 17
            k %= 256

        box = h[k]
               
        if op == "=":
            n = int(c)    
            # print(cs, k, op, n)        
            hit = False
            for i, (l, v) in enumerate(box):
                if l == cs:
                    box[i] = (l, n)
                    hit = True
            if not hit:
                box.append((cs, n))
        else:
            # print(cs, k, op)
            for i, (l, _) in enumerate(box):
                if l == cs:
                    box.pop(i)
        # print(h)
        cs = ""
        op = None
    elif c == "=":
        op = "="
    elif c == "-":
        op = "-"
    elif c == ",":
        pass
    else:
        cs += c

acc = 0
for i, box in enumerate(h):
    for j, (_, p) in enumerate(box):
        acc += (i + 1) * (j + 1) * p

print(acc)
