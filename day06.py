# %% First Star and Second Star
# ------------------------------------------------------------------------------

lines = input.splitlines()

times = [word for word in lines[0].split(" ") if word != ""][1:]
times = [int(time) for time in times]
distances = [word for word in lines[1].split(" ") if word != ""][1:]
distances = [int(distance) for distance in distances]


acc = 1
for time, distance in zip(times, distances):
    k = 0
    for t in range(time):
        if t * (time - t) > distance:
            k += 1
    acc *= k

print(acc)
