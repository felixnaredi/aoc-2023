# %% First Star
# ------------------------------------------------------------------------------

BROADCAST = 0
FLIPFLOP = 1
CONJUNCTION = 2

OFF = 0
ON = 1

LO = 1
HI = 2

conjs = []
modules = {}
for line in input.splitlines():
    label, outs = line.split(" -> ")
    outs = outs.split(", ")
    if label == "broadcaster":
        modules[label] = BROADCAST, outs, None
    elif label[0] == "%":
        modules[label[1:]] = FLIPFLOP, outs, OFF
    elif label[0] == "&":
        modules[label[1:]] = CONJUNCTION, outs, {}
        conjs.append(label[1:])
    else:
        raise SyntaxError(label)

for conj in conjs:
    _, _, outs1 = modules[conj]
    for label, (_, outs2, _) in modules.items():
        if conj in outs2:
            outs1[label] = LO

print(modules)

lo = 0
hi = 0
for _ in range(1000):
    queue = [(None, "broadcaster", LO)]
    lo += 1
    while len(queue) != 0:
        sender, receiver, sig = queue.pop(0)
        # print(sig, receiver, sender)
        if x := modules.get(receiver):
            t, outs, state = x
            if t == BROADCAST:
                for out in outs:
                    queue.append((receiver, out, LO))
                    lo += 1
            elif t == FLIPFLOP:
                if sig == LO:
                    if state == OFF:
                        for out in outs:
                            queue.append((receiver, out, HI))
                            hi += 1
                        modules[receiver] = FLIPFLOP, outs, ON
                    elif state == ON:
                        for out in outs:
                            queue.append((receiver, out, LO))
                            lo += 1
                        modules[receiver] = FLIPFLOP, outs, OFF
            elif t == CONJUNCTION:
                state[sender] = sig
                if all((s == HI for s in state.values())):
                    for out in outs:
                        queue.append((receiver, out, LO))
                        lo += 1
                else:
                    for out in outs:
                        queue.append((receiver, out, HI))
                        hi += 1

print(lo * hi)

# %% Second Star
# ------------------------------------------------------------------------------

