# https://adventofcode.com/2023/day/3
# part 2
from dec03.board import Board


def intersect(a, b):
    return max(0, min(a[2], b[2]) - max(a[0], b[0])) * max(0, min(a[3], b[3]) - max(a[1], b[1]))


def main(fname):
    board = Board(fname)
    numbers = [board.halo_coords(line, start, end) for _, line, start, end in board.numbers()]
    gears = [board.halo_coords(line, start, end) for _, line, start, end in board.gears()]

    for gear in gears:
        for number in numbers:
            print(f"gear: {gear} number: {number} intersect: {intersect(gear, number)}")


    for n, line, x1, x2 in board.gears():
        board.debug_token(line, x1, x2)


if __name__ == "__main__":
    print(main("sample.txt"))  # 528799
    # print(main("input.txt"))  # 528799
