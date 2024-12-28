from backtrack import backtrack_one
from piece import *
from itertools import product, combinations
from typing import List

__all__ = ["calc"]


class Block:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers

    def __repr__(self):
        return self.name


def three_product(board_count, block1, block2, block3):
    res = 0
    for i in range(board_count):
        for j in range(board_count):
            for k in range(board_count):
                if i == j or i == k or j == k:
                    continue
                res += block1.numbers[i] * block2.numbers[j] * block3.numbers[k]
    return res

def calc(boards: List[List[List[int]]]):
    pentomino_counts = []
    tetramino_counts = []
    for piece in pentomino:
        result = []
        for board in boards:
            # Solve
            solve = backtrack_one(board, piece)

            # Output the result
            result.append(solve)

        pentomino_counts.append(Block(piece.name, result))

    for piece in tetramino:
        result = []
        for board in boards:
            # Solve
            solve = backtrack_one(board, piece)

            # Output the result
            result.append(solve)

        tetramino_counts.append(Block(piece.name, result))

    result = {}
    for v in product(combinations(pentomino_counts, 2), tetramino_counts):
        x1, x2 = v[0]
        x3 = v[1]
        result[(x1, x2, x3)] = three_product(len(boards), x1, x2, x3)

    return result
