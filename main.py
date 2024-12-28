from backtrack import count_cases
from piece import *
from itertools import product, combinations

boards = list(map(lambda x: x.cells_2d, pentomino)) * 3


class Block:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers

    def __repr__(self):
        return self.name

pentomino_counts = []
tetramino_counts = []
for piece in pentomino:
    result = []
    for board in boards:
        # Solve
        solve = count_cases(board, piece)

        # Output the result
        result.append(solve)
    
    pentomino_counts.append(Block(piece.name, result))

for piece in tetramino:
    result = []
    for board in boards:
        # Solve
        solve = count_cases(board, piece)

        # Output the result
        result.append(solve)
    
    tetramino_counts.append(Block(piece.name, result))

def three_product(block1, block2, block3):
    res = 0
    for i in range(len(boards)):
        for j in range(len(boards)):
            for k in range(len(boards)):
                if (i == j or i == k or j == k):
                    continue
                res += block1.numbers[i] * block2.numbers[j] * block3.numbers[k]
    return res

result = {}
for v in product(combinations(pentomino_counts, 2), tetramino_counts):
    x1, x2 = v[0]
    x3 = v[1]
    result[(x1, x2, x3)] = three_product(x1, x2, x3)

from collections import Counter

result_counter = Counter(result.values())
print(result_counter)