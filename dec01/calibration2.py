# https://adventofcode.com/2023/day/1
# Part 2
import regex as re  # regex can match overlapping patterns

DIGITS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
VALUES = {d: i + 1 for i, d in enumerate(DIGITS)} | {str(i): i for i in range(10)}
DIGIT = re.compile(r'(\d|%s)' % '|'.join(DIGITS))


def find_first_and_last_digit(line):
    tmp = [VALUES[v] for v in DIGIT.findall(line, overlapped=True)]
    return tmp[0] * 10 + tmp[-1]

code = 0
for i, line in enumerate(open('input.txt'), start=1):
    if not line.strip():
        continue
    digits = find_first_and_last_digit(line)
    code += digits

print(code)  # 53340
