# %% First Star
# ------------------------------------------------------------------------------

acc = 0
for line in input.splitlines():
    words = [w for w in line.split(" ") if w != ""]
    i = words.index("|")
    win, own = words[2:i], words[i + 1:]
    k = 0
    for x in own:
        if x in win:
            if k == 0:
                k = 1
            else:
                k *= 2
    acc += k

print(acc)

# %% Second Star
# ------------------------------------------------------------------------------

cards = { i + 1: 1 for i in list(range(len(input.splitlines()))) }

for i, line in enumerate(input.splitlines()):
    i += 1
    words = [w for w in line.split(" ") if w != ""]
    j = words.index("|")
    win, own = words[2:j], words[j + 1:]
    k = 0
    for x in own:
        if x in win:
            k += 1
    for c in range(k):
        cards[i + 1 + c] += 1 * cards[i]

print(sum(cards.values()))
