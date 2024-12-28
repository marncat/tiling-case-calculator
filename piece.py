from typing import List


class Piece:
    def __init__(self, name, cells):
        self.name: str = name
        self.cells_2d: List[List[int]] = cells

    @property
    def cells(self):
        return [(x, y) for x, row in enumerate(self.cells_2d) for y, value in enumerate(row) if value == 1]

    def __str__(self):
        return self.name

pentomino = [
    Piece("V", [
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1]
    ]),
    Piece("T", [
        [1, 1, 1],
        [0, 1, 0],
        [0, 1, 0]
    ]),
    Piece("F", [
        [0, 1, 1],
        [1, 1, 0],
        [0, 1, 0]
    ]),
    Piece("W", [
        [1, 1, 0],
        [0, 1, 1],
        [0, 0, 1]
    ]),
    Piece("U", [
        [1, 1],
        [1, 0],
        [1, 1]
    ]),
    Piece("X", [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]),
    Piece("I", [[1, 1, 1, 1, 1]]),
    Piece("Y", [
        [1, 1, 1, 1],
        [0, 0, 1, 0]
    ]),
    Piece("L", [
        [1, 1, 1, 1],
        [0, 0, 0, 1]
    ]),
    Piece("P", [
        [1, 1, 1],
        [1, 1, 0]
    ]),
    Piece("Z", [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ]),
    Piece("N", [
        [1, 1, 1, 0],
        [0, 0, 1, 1]
    ])
]

tetramino = [
    Piece("o", [
        [1, 1],
        [1, 1]
    ]),
    Piece("i", [
        [1, 1, 1, 1]
    ]),
    Piece("s", [
        [0, 1, 1],
        [1, 1, 0]
    ]),
    Piece("t", [
        [0, 1, 0],
        [1, 1, 1]
    ]),
    Piece("l", [
        [1, 1, 1],
        [1, 0, 0] 
    ])
]