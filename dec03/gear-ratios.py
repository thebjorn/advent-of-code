# https://adventofcode.com/2023/day/3
# part 1
from dec03.board import Board
    

def main(fname):
    board = Board(fname)
    partnums = 0
    for n, line, x1, x2 in board.numbers():
        if board.halo(line, x1, x2):
            partnums += n

    return partnums


if __name__ == "__main__":
    print(main("input.txt"))  # 528799
