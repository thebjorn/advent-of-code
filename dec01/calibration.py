# https://adventofcode.com/2023/day/1

def first_digit(line):
    for c in line:
        if c.isdigit():
            return c
    raise ValueError(f'No digits in: {line}')

code = 0
for i, line in enumerate(open('input.txt'), start=1):
    if not line.strip():
        continue
    digits = first_digit(line) + first_digit(reversed(line))
    code += int(digits)

print(code)
