from count_cases import count_cases
from pieces import *
from itertools import product, combinations
from typing import List, Tuple

__all__ = ["calc"]


class Block:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers

    def __repr__(self):
        return self.name


def three_product(board_counts, block1, block2, block3):
    board_count = len(board_counts)
    res = 0
    for i in range(board_count):
        for j in range(board_count):
            for k in range(board_count):
                shapes = block1.numbers[i] * block2.numbers[j] * block3.numbers[k]
                if (i == j & j == k):
                    N = board_counts[i]
                    if N > 2:
                        res += N * (N - 1) * (N - 2) * shapes
                elif (i == j):
                    N = board_counts[i]
                    if N > 1:
                        res += N * (N - 1) * board_counts[k] * shapes
                elif (j == k):
                    N = board_counts[j]
                    if N > 1:
                        res += N * (N - 1) * board_counts[i] * shapes
                elif (i == k):
                    N = board_counts[i]
                    if N > 1:
                        res += N * (N - 1) * board_counts[j] * shapes
                else:
                    res += board_counts[i] * board_counts[j] * board_counts[k] * shapes

    return res

def calc(boards: List[List[List[int]]], board_counts: List[int] = None):
    pentomino_counts = []
    tetramino_counts = []

    if board_counts is None:
        board_counts = [1] * len(boards)

    for name, unique_shapes in pentomino_for_counting.items():
        result = [count_cases(board, unique_shapes) for board in boards]
        pentomino_counts.append(Block(name, result))

    for name, unique_shapes in tetramino_for_counting.items():
        result = [count_cases(board, unique_shapes) for board in boards]
        tetramino_counts.append(Block(name, result))

    result = {}
    for v in product(combinations(pentomino_counts, 2), tetramino_counts):
        x1, x2 = v[0]
        x3 = v[1]
        result[(x1, x2, x3)] = three_product(board_counts, x1, x2, x3)

    return result
