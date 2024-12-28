from itertools import product
from typing import List, Set
from pieces import Shape

__all__ = ["count_cases"]

def can_place(x: int, y: int, shape: Shape, board: List[List[int]]):
    """Check if a piece can be placed."""
    for dx, dy in shape.cells:
        nx, ny = x + dx, y + dy
        if board[nx][ny] != 1:
            return False
    return True

def count_cases(board: List[List[int]], unique_shapes: Set[Shape]):
    solution_count = 0

    for shape in unique_shapes:
        for x, y in product(range(len(board) - shape.width + 1), range(len(board[0]) - shape.height + 1)):
            if can_place(x, y, shape, board):
                solution_count += 1

    return solution_count