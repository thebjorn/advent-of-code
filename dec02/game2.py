# https://adventofcode.com/2018/day/1
# part 2
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Colors:
    red: int
    green: int
    blue: int

    def __le__(self, other):
        return self.red <= other.red and self.green <= other.green and self.blue <= other.blue

    def __abs__(self):
        return self.red * self.green * self.blue

@dataclass
class Game:
    id: int
    colors: list[Colors] = field(default_factory=list)

    def mincubes(self):
        return Colors(
            red=max(c.red for c in self.colors),
            green=max(c.green for c in self.colors),
            blue=max(c.blue for c in self.colors)
        )


def parse_color(rgb_text):
    res = {}
    for color in rgb_text.split(','):
        value, color = color.split()
        res[color] = int(value)
    return res.get('red', 0), res.get('green', 0), res.get('blue', 0)


def parse_colors(colors):
    for rgb_text in colors.split(';'):
        r, g, b = parse_color(rgb_text)
        yield Colors(
            red=r,
            green=g,
            blue=b
        )


def parse(line):
    game, colors = line.split(':')
    gameid = int(game[len('Game '):])
    return Game(id=gameid, colors=list(parse_colors(colors)))


def read_input(fname):
    for line in open(fname):
        if not line.strip():
            continue
        yield parse(line)
    

fname = 'input.txt'
print(sum(abs(game.mincubes()) for game in read_input(fname)))  # 78669
