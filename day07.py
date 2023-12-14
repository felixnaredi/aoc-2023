# %% First Star
# ------------------------------------------------------------------------------

LABELS = "AKQJT98765432"
LABEL_KEY = { label: key for key, label in enumerate(LABELS) }

game = []

for line in input.splitlines():
    [hand, bet] = line.split(" ")
    count = { label: 0 for label in LABELS }
    keys = [LABEL_KEY[card] for card in hand]
    for card in hand:
        count[card] += 1
    if max(count.values()) == 5:
        game.append((0, keys, hand, bet))
    elif max(count.values()) == 4:
        game.append((1, keys, hand, bet))
    elif max(count.values()) == 3 and 2 in count.values():
        game.append((2, keys, hand, bet))
    elif max(count.values()) == 3:
        game.append((3, keys, hand, bet))
    elif max(count.values()) == 2 and len([x for x in count.values() if x != 0]) == 3:
        game.append((4, keys, hand, bet))
    elif max(count.values()) == 2:
        game.append((5, keys, hand, bet))
    else:
        game.append((6, keys, hand, bet))

acc = 0
for i, (type, keys, hand, bet) in enumerate(sorted(game, reverse=True)):    
    acc += (i + 1) * int(bet)
    # print(i + 1, acc, (type, keys, hand, bet))

print(acc)


# %% Second Star
# ------------------------------------------------------------------------------

LABELS = "AKQT98765432J"
LABEL_KEY = { label: key for key, label in enumerate(LABELS) }

game = []

for line in input.splitlines():
    [hand, bet] = line.split(" ")
    count = { label: 0 for label in LABELS }
    keys = [LABEL_KEY[card] for card in hand]
    for card in hand:
        count[card] += 1
    j = count["J"]
    count["J"] = 0

    if max(count.values()) + j == 5:
        game.append((0, keys, hand, bet))
    elif max(count.values()) + j == 4:
        game.append((1, keys, hand, bet))
    elif max(count.values()) == 3 and 2 in count.values():
        game.append((2, keys, hand, bet))
    elif max(count.values()) + j == 3 and len([x for x in count.values() if x == 2]) == 2:
        game.append((2, keys, hand, bet))
    elif max(count.values()) + j == 3:
        game.append((3, keys, hand, bet))
    elif max(count.values()) == 2 and len([x for x in count.values() if x != 0]) == 3:
        game.append((4, keys, hand, bet))
    elif max(count.values()) + j == 2:
        game.append((5, keys, hand, bet))
    else:
        game.append((6, keys, hand, bet))

acc = 0
for i, (type, keys, hand, bet) in enumerate(sorted(game, reverse=True)):    
    acc += (i + 1) * int(bet)
    # print(i + 1, acc, (type, keys, hand, bet), file=file)

print(acc)
