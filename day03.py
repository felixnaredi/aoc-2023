# %% First Star
# ------------------------------------------------------------------------------

class Done(Exception):
    pass

lines = input.splitlines()
pad = ["." * (len(lines[0]) + 2)]
for line in lines:
    pad.append("." + line + ".")
pad.append("." * (len(lines[0]) + 2))

acc = 0

for y in range(1, len(pad) - 1):
    x = 1
    while x < len(pad[0]) - 1:
        if pad[y][x].isdigit():
            n = 0
            x0 = x
            while pad[y][x].isdigit():
                n *= 10
                n += int(pad[y][x])
                x += 1
            try:
                for yn in range(y - 1, y + 2):
                    for xn in range(x0 - 1, x + 1):
                        if pad[yn][xn] != "." and not pad[yn][xn].isdigit():
                            raise Done
            except Done:
                acc += n
            # print(n, acc)
        else:
            x += 1

print(acc)

# %% Second Star
# ------------------------------------------------------------------------------

class Done(Exception):
    pass

lines = input.splitlines()
pad = ["." * (len(lines[0]) + 2)]
for line in lines:
    pad.append("." + line + ".")
pad.append("." * (len(lines[0]) + 2))

acc = 0

for y in range(1, len(pad) - 1):
    for x in range(1, len(pad[0]) - 1):
        if pad[y][x] == "*":
            nums = {}
            for yn in (y - 1, y, y + 1):
                for xn in (x - 1, x, x + 1):
                    if pad[yn][xn].isdigit():
                        xm = xn
                        while pad[yn][xm].isdigit():
                            xm -= 1
                        xm += 1
                        n = 0
                        while pad[yn][xm].isdigit():
                            n *= 10
                            n += int(pad[yn][xm])
                            xm += 1
                        nums[(yn, xm)] = n
            if len(nums) > 1:
                nums = list(nums.values())
                acc += nums[0] * nums[1]


print(acc)