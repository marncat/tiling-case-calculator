from itertools import product
from typing import List, Tuple

__all__ = ["backtrack"]

def normalize(shape):
    """Generate normalized shape for uniqueness."""
    shape.sort()
    min_x, min_y = shape[0]
    return [(x - min_x, y - min_y) for x, y in shape]


def generate_transformations(shape):
    """Generate all transformations (rotations and flips)."""
    unique_shapes = set()

    # Generate rotations
    for _ in range(4):
        shape = normalize(shape)
        unique_shapes.add(tuple(shape))
        shape = [(-y, x) for x, y in shape]  # 90-degree rotation

    # Flip horizontally and check rotations again
    shape = [(x, -y) for x, y in shape]
    for _ in range(4):
        shape = normalize(shape)
        unique_shapes.add(tuple(shape))
        shape = [(-y, x) for x, y in shape]  # 90-degree rotation

    return unique_shapes


def can_place(x, y, shape, board):
    """Check if a piece can be placed."""
    for dx, dy in shape:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[0]) or board[nx][ny] != 1:
            return False
    return True


def place_piece(x, y, shape, board, value):
    """Place or remove a piece."""
    for dx, dy in shape:
        nx, ny = x + dx, y + dy
        board[nx][ny] = value


def backtrack(piece_index, board, pieces: List[List[Tuple[int, int]]], solution_count):
    """Backtracking algorithm."""
    if piece_index == len(pieces):
        solution_count[0] += 1
        if solution_count[0] >= 10_000_000:
            solution_count[1] = True
        return

    piece = pieces[piece_index]
    unique_shapes = generate_transformations(piece)

    for shape in unique_shapes:
        for x, y in product(range(len(board)), range(len(board[0]))):
            if can_place(x, y, shape, board):
                place_piece(x, y, shape, board, 2)  # Mark placement
                backtrack(piece_index + 1, board, pieces, solution_count)
                if solution_count[1]:
                    return
                place_piece(x, y, shape, board, 1)  # Remove placement

def backtrack_one(board: List[List[int]], piece: List[List[int]]):
    solution_count = [0, False]  # [count, max_check]
    
    piece_for_backtrack: List[Tuple[int, int]] = []
    for x, y in product(range(len(piece)), range(len(piece[0]))):
        if piece[x][y] == 1:
            piece_for_backtrack.append((x, y))

    backtrack(0, board, [piece_for_backtrack], solution_count)
    return solution_count[0]