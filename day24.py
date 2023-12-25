# %% First Star
# ------------------------------------------------------------------------------

points = []
eqs = []
for line in input.splitlines():
    pos, vel = line.split("@")
    pos = [int(p) for p in pos.split(", ")]
    vel = [int(v) for v in vel.split(", ")]
    x1, y1 = pos[0], pos[1]
    x2, y2 = x1 + vel[0], y1 + vel[1]
    m = (y2 - y1) / (x2 - x1)
    b = y1 - x1 * m
    points.append(((x1, y1), (vel[0], vel[1])))
    eqs.append((m, b))
    # print((x1, y1), (m, b))

# min_x, max_x = 7, 27
# min_y, max_y = 7, 27
min_x, max_x = 200000000000000, 400000000000000
min_y, max_y = 200000000000000, 400000000000000

acc = 0
for i, (a, c) in enumerate(eqs):
    for j, (b, d) in enumerate(eqs[i + 1:]):
        j += i + 1
        if a - b != 0:
            x = (d - c) / (a - b)
            y = a * x + c
            # print(points[i], points[j], x, y)
            if min_x <= x <= max_x and min_y <= y <= max_y:
                k = 0
                for (px, py), (vx, vy) in (points[i], points[j]):
                    # print((px, py), (vx, vy))
                    if vx < 0 and vy < 0:
                        if x <= px and y <= py:
                            k += 1
                    elif vx < 0 and vy > 0:
                        if x <= px and y >= py:
                            k += 1
                    elif vx > 0 and vy < 0:
                        if x >= px and y <= py:
                            k += 1
                    elif vx > 0 and vy > 0:
                        if x >= px and y >= py:
                            k += 1
                    # print(k)
                if k == 2:
                    acc += 1

print(acc)


# %% Second Star
# ------------------------------------------------------------------------------

