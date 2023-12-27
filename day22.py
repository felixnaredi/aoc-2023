# %% First Star
# ------------------------------------------------------------------------------

class Found(Exception):
    pass

bricks = {}
ztable = {}
id = 1

z_max = 0
z_min = 99999999
for line in input.splitlines():
    w1, w2 = line.split("~")
    x1, y1, z1 = [int(w) for w in w1.split(",")]
    x2, y2, z2 = [int(w) for w in w2.split(",")]
    brick = []
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            for z in range(min(z1, z2), max(z1, z2) + 1):
                brick.append((x, y, z))
                z_max = max(z, z_max)
                z_min = min(z, z_min)
    bricks[id] = brick
    id += 1

for z in range(z_min, z_max + 1):
    ztable[z] = set()
for id, brick in bricks.items():
    for _, _, z in brick:
        ztable[z].add(id)


def falling(id):
    for x, y, z in bricks[id]:
        if z > 1:
            for id2 in ztable[z - 1]:
                if id2 != id:
                    for block2 in bricks[id2]:
                        if block2 == (x, y, z - 1):
                            return False
        else:
            return False
    return True

def lower(id):
    brick = bricks[id]
    for i, (x, y, z) in enumerate(brick):
        brick[i] = (x, y, z - 1)
    ztable[z].remove(id)
    ztable[z - 1].add(id)

def add(id, brick):
    bricks[id] = brick
    for _, _, z in brick:
        ztable[z].add(id)

def remove(id):
    brick = bricks.pop(id)
    for _, _, z in brick:
        if id in ztable[z]:
            ztable[z].remove(id)
    return brick



stable = False
while not stable:
    stable = True
    for id in bricks.keys():
        if falling(id):
            stable = False
            lower(id)

bricks2 = dict(bricks)
acc = 0
for id in bricks2.keys():
    acc += 1
    brick = remove(id)
    if not all((not falling(id2) for id2 in bricks.keys())):
        acc -= 1
    add(id, brick)

print(acc)


# %% Second Star
# ------------------------------------------------------------------------------

class Found(Exception):
    pass


bricks = {}
ztable = {}
id = 1

z_max = 0
z_min = 99999999
for line in input.splitlines():
    w1, w2 = line.split("~")
    x1, y1, z1 = [int(w) for w in w1.split(",")]
    x2, y2, z2 = [int(w) for w in w2.split(",")]
    brick = []
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            for z in range(min(z1, z2), max(z1, z2) + 1):
                brick.append((x, y, z))
                z_max = max(z, z_max)
                z_min = min(z, z_min)
    bricks[id] = brick
    id += 1

for z in range(z_min, z_max + 1):
    ztable[z] = set()
for id, brick in bricks.items():
    for _, _, z in brick:
        ztable[z].add(id)


def falling(id):
    for x, y, z in bricks[id]:
        if z > 1:
            for id2 in ztable[z - 1]:
                if id2 != id:
                    for block2 in bricks[id2]:
                        if block2 == (x, y, z - 1):
                            return False
        else:
            return False
    return True


def lower(id):
    brick = bricks[id]
    for i, (x, y, z) in enumerate(brick):
        brick[i] = (x, y, z - 1)
        if id in ztable[z]:
            ztable[z].remove(id)
            ztable[z - 1].add(id)


def add(id, brick):
    bricks[id] = brick
    for _, _, z in brick:
        ztable[z].add(id)


def remove(id):
    brick = bricks.pop(id)
    for _, _, z in brick:
        if id in ztable[z]:
            ztable[z].remove(id)
    return id, brick

stable = False
while not stable:
    stable = True
    for id in bricks.keys():
        if falling(id):
            stable = False
            lower(id)

s = sorted([(z, ids) for z, ids in ztable.items()])
queue = []
height = []
visited = set()
for z, ids in s:
    for id in ids:
        if id not in visited:
            visited.add(id)
            queue.append(id)
            height.append((z, id))

# print(bricks, ztable)

bricks_copy = {}
for id, blocks in bricks.items():
    bricks_copy[id] = [block for block in blocks]
ztable_copy = {}
for z, ids in ztable.items():
    ztable_copy[z] = set(ids)

acc = 0
while len(queue) != 0:
    id = queue.pop(0)
    fallen = set()
    stable = False
    remove(id)
    while not stable:
        stable = True
        for id1 in bricks.keys():
            if id1 != id and falling(id1):
                stable = False
                fallen.add(id1)
                lower(id1)
    # print(len(fallen))
    acc += len(fallen)
    bricks.clear()
    for id, blocks in bricks_copy.items():
        bricks[id] = [block for block in blocks]
    ztable.clear()
    for z, ids in ztable_copy.items():
        ztable[z] = set(ids)

print(acc)
