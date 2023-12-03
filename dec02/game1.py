# https://adventofcode.com/2018/day/1
# part 1
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Colors:
    red: int
    green: int
    blue: int

    def __le__(self, other):
        return self.red <= other.red and self.green <= other.green and self.blue <= other.blue


@dataclass
class Game:
    id: int
    colors: list[Colors] = field(default_factory=list)


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


def read_input():
    for line in open("input.txt"):
        if not line.strip():
            continue
        yield parse(line)
    

maxcolors = Colors(red=12, green=13, blue=14)

success = 0
for i, game in enumerate(read_input(), start=1):
    if all(c <= maxcolors for c in game.colors):
        success += game.id

print(success)  # 2283        
