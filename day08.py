# %% First Star
# ------------------------------------------------------------------------------

lines = input.splitlines()
directions = lines[0]
graph = {}
for line in lines[2:]:
    key = line[0:3]
    lft = line[7:10]
    rgt = line[12:15]
    graph[key] = {"L": lft, "R": rgt}

run = True
steps = 0
key = "AAA"
while run:
    for d in directions:
        # print(key, d)
        steps += 1
        key = graph[key][d]
        if key == "ZZZ":
            run = False
            break

print(steps)

# %% Second Star
# ------------------------------------------------------------------------------

lines = input.splitlines()
directions = lines[0]

graph = {}
for line in lines[2:]:
    key = line[0:3]
    lft = line[7:10]
    rgt = line[12:15]
    graph[key] = {"L": lft, "R": rgt}

keys = [key for key in graph.keys() if key[2] == "A"]
steps = []

for key in keys:
    print(key)
    run = True
    step = 0
    while run:
        for d in directions:
            step += 1
            if run:
                key = graph[key][d]
                if key[2] == "Z":
                    steps.append(step)
                    run = False
                    break

print(steps)

# The actual value can be calculated from the list of steps.
