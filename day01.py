# %% First Star
# ------------------------------------------------------------------------------

sum = 0
for line in input.splitlines():
    for c in line:
        if c.isdecimal():
            d0 = int(c)
            break
    for c in reversed(line):
        if c.isdecimal():
            d1 = int(c)
            break
    sum += d0 * 10 + d1

print(sum)

# %% Second Star
# ------------------------------------------------------------------------------

sum = 0

digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

reverse_digits = {}
for k, v in digits.items():
    reverse_digits[k[::-1]] = v

print(reverse_digits)

for line in input.splitlines():
    i = 2**64
    for digit in digits:
        try:
            j = line.index(digit)
            if i > j:
                d0 = digits[digit]
                i = j
        except ValueError:
            pass

    for j, c in enumerate(line):
        if j > i:
            break
        if c.isdecimal():
            d0 = int(c)
            break

    print("d0", d0)
    i = 2**64
    for digit in reverse_digits:
        try:
            j = line[::-1].index(digit)
            if i > j:
                d1 = reverse_digits[digit]
                i = j
        except ValueError:
            pass

    for j, c in enumerate(line[::-1]):
        if j > i:
            break
        if c.isdecimal():
            d1 = int(c)
            break
    
    print("d1", d1)
    sum += d0 * 10 + d1

print(sum)