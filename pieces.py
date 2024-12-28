from itertools import product
from typing import List, Tuple

pentomino = {
    "V":  [
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1]
    ],
    "T":  [
        [1, 1, 1],
        [0, 1, 0],
        [0, 1, 0]
    ],
    "F":  [
        [0, 1, 1],
        [1, 1, 0],
        [0, 1, 0]
    ],
    "W":  [
        [1, 1, 0],
        [0, 1, 1],
        [0, 0, 1]
    ],
    "U":  [
        [1, 1],
        [1, 0],
        [1, 1]
    ],
    "X":  [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],
    "I": [
        [1, 1, 1, 1, 1]
    ],
    "Y": [
        [1, 1, 1, 1],
        [0, 0, 1, 0]
    ],
    "L": [
        [1, 1, 1, 1],
        [0, 0, 0, 1]
    ],
    "P": [
        [1, 1, 1],
        [1, 1, 0]
    ],
    "Z": [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ],
    "N": [
        [1, 1, 1, 0],
        [0, 0, 1, 1]
    ]
}

tetramino = {
    "o": [
        [1, 1],
        [1, 1]
    ],
    "i": [
        [1, 1, 1, 1]
    ],
    "s": [
        [0, 1, 1],
        [1, 1, 0]
    ],
    "t": [
        [0, 1, 0],
        [1, 1, 1]
    ],
    "l": [
        [1, 1, 1],
        [1, 0, 0] 
    ]
}

class Shape:
    def __init__(self, width: int, height: int, cells: List[Tuple[int, int]]) -> None:
        self.width = width
        self.height = height
        cells.sort()
        self.cells = tuple(cells)

    def rotate(self):
        return Shape(self.height, self.width, [(self.height - y - 1, x) for x, y in self.cells])
    
    def flip(self):
        return Shape(self.width, self.height, [(self.width - x - 1, y) for x, y in self.cells])
    
    def __hash__(self) -> int:
        return hash(self.cells)

    def __eq__(self, value: object, /) -> bool:
        return hash(self) == hash(value)

def generate_transformations(shape: Shape):
    """Generate all transformations (rotations and flips)."""
    unique_shapes = set()

    # Generate rotations
    for _ in range(4):
        unique_shapes.add(shape)
        shape = shape.rotate()

    # Flip horizontally and check rotations again
    shape = shape.flip()
    for _ in range(4):
        unique_shapes.add(shape)
        shape = shape.rotate()

    return unique_shapes

pentomino_for_counting = {
    k: generate_transformations(Shape(len(v), len(v[0]), [(x, y) for x, y in product(range(len(v)), range(len(v[0]))) if v[x][y] == 1])) for k, v in pentomino.items()    
}

tetramino_for_counting = {
    k: generate_transformations(Shape(len(v), len(v[0]), [(x, y) for x, y in product(range(len(v)), range(len(v[0]))) if v[x][y] == 1])) for k, v in tetramino.items()    
}