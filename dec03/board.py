from rich.console import Console
console = Console()


import re


class Board:
    def __init__(self, fname) -> None:
        with open(fname) as f:
            self.lines = f.read().splitlines()
        self.width = len(self.lines[0])
        self.height = len(self.lines)

    def numbers(self):
        for i, line in enumerate(self.lines):
            for number in re.finditer(r"\d+", line):
                yield (int(number.group()), i, number.start(), number.end())

    def gears(self):
        for i, line in enumerate(self.lines):
            for gear in re.finditer(r"[*]", line):
                yield (gear.group(), i, gear.start(), gear.end())

    def debug_token(self, line, start, end):
        halo = 'underline'
        numstyle = 'blink'

        if line > 0:
            # print(f'[{self.lines[line-1]}]')
            console.print(self.lines[line-1][:max(0, start-1)], end='')
            console.print(self.lines[line-1][max(0, start-1):end+1], style=halo, end="")
            console.print(self.lines[line-1][end+1:])

        # console.print(self.lines[line])
        # console.print(" " * start + "^" * (end - start))  # , "============================>", num)

        # print(f'[{self.lines[line]}]')
        console.print(self.lines[line][:max(0, start-1)], sep="", end="")
        console.print(self.lines[line][max(0, start-1):start], sep="", style=halo, end="")
        console.print(self.lines[line][start:end], sep="", style=numstyle, end="")
        console.print(self.lines[line][end:end+1], sep="", style=halo, end="")
        console.print(self.lines[line][end+1:])

        if line + 1 < len(self.lines):
            # print(f'[{self.lines[line+1]}]')

            console.print(self.lines[line+1][:max(0, start-1)], end="")
            console.print(self.lines[line+1][max(0, start-1):end+1], style=halo, end="")
            console.print(self.lines[line+1][end+1:])

        console.print(f'HALO\[{self.halo(line, start, end)}]')

    def halo_coords(self, y, x1, x2):
        xmin = max(0, x1 - 1)
        xmax = min(self.width, x2 + 1)
        ymin = max(0, y - 1)
        ymax = min(self.height, y + 1)
        return (xmin, ymin, xmax, ymax)

    def halo(self, y, x1, x2):
        xmin = max(0, x1 - 1)
        xmax = min(self.width, x2 + 1)
        ymin = max(0, y - 1)
        ymax = min(self.height, y + 1)
        res = ''
        if y > 0:
            res += self.lines[ymin][xmin:xmax]

        res += self.lines[y][xmin:x1]
        res += self.lines[y][x2:xmax]

        if y + 1 < self.height:
            res += self.lines[ymax][xmin:xmax]

        return res.replace('.', '')