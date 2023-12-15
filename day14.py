# %% First Star
# ------------------------------------------------------------------------------

lines = input.splitlines()

acc = 0
for x in range(len(lines[0])):
    u = len(lines)
    for y, cs in enumerate(lines):
        c = cs[x]
        if c == "O":
            acc += u
            # print(u, acc)
            u -= 1
        elif c == "#":
            u = len(lines) - y - 1
            # print("#", y, u)

print(acc)


# %% Second Star
# ------------------------------------------------------------------------------

room = input.splitlines()
room = [[c for c in cs] for cs in room]

# print(len([c for cs in room for c in cs if c == "O"]))
# for row in room:
#     print("".join(row))

for i in range(1000):
    # North
    for x in range(len(room[0])):
        u = 0
        for y, cs in enumerate(room):
            c = cs[x]
            if c == "O":
                room[y][x] = "."
                room[u][x] = "O"
                u += 1
            elif c == "#":
                u = y + 1
    # print()
    # print(len([c for cs in room for c in cs if c == "O"]))
    # for row in room:
    #     print("".join(row))

    # West
    for y in range(len(room)):
        u = 0
        for x, c in enumerate(room[y]):
            if c == "O":
                room[y][x] = "."
                room[y][u] = "O"
                u += 1
            elif c == "#":
                u = x + 1
    # print()
    # print(len([c for cs in room for c in cs if c == "O"]))
    # for row in room:
    #     print("".join(row))

    # South
    for x in range(len(room[0])):
        u = len(room) - 1
        for y, cs in reversed(list(enumerate(room))):
            c = cs[x]
            if c == "O":
                room[y][x] = "."
                room[u][x] = "O"
                u -= 1
            elif c == "#":
                u = y - 1
    # print()
    # print(len([c for cs in room for c in cs if c == "O"]))
    # for row in room:
    #     print("".join(row))

    # East
    for y in range(len(room)):
        u = len(room[0]) - 1
        for x, c in reversed(list(enumerate(room[y]))):
            if c == "O":
                room[y][x] = "."
                room[y][u] = "O"
                u -= 1
            elif c == "#":
                u = x - 1
    # print()
    # print(len([c for cs in room for c in cs if c == "O"]))
    # for row in room:
    #     print("".join(row))

    load = 0
    for y, row in enumerate(room):
        load += len([c for c in row if c == "O"]) * (len(room) - y)
    print(i + 1, load)

"""
This code will print the load of the first 1000 cycles. Looking at the printed values a pattern will
emerge.

In my case, from cycle 109 and onwards the same 9 values was repeating. Thus, I could calculate the
value of cycle one billion by `(1000000000 - 109) % 9`. The result of the equation is the "index" of
the repeated value in the pattern.
"""
