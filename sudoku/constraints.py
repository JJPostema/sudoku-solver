# Sudoku solver v0.1.0
# Written by J.J. Postema

from typing import List, Tuple, Callable

# Type aliases for specific objects
Coord = Tuple[int, int]
Grid = List[List[int]]

def nextEmptySquare(grid: Grid) -> Tuple:
    '''
    Finds the next empty square on a grid
    '''
    n = len(grid)

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                return r, c
    return 0, 0

def allEmptySquares(grid: Grid) -> List[Tuple]:
    '''
    Finds all empty squares on a grid
    '''
    n = len(grid)
    squares = list()

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                squares += [(r, c)]
    return squares

# (Custom) constraints
ConstraintFunc = Callable[[Grid, Coord, int], bool]

class Constraint:
    def __init__(self, name: str, coords: List[Coord], check: ConstraintFunc):
        self.name = name
        self.coords = coords
        self.check = check

    # ---------------------------
    # Standard sudoku constraints
    # ---------------------------
    @staticmethod
    def row_constraint(grid, coord, digit):
        r, _ = coord
        return digit not in grid[r]

    @staticmethod
    def col_constraint(grid, coord, digit):
        _, c = coord
        return all(grid[i][c] != digit for i in range(len(grid)))

    @staticmethod
    def region_constraint(grid, coord, digit):
        if len(grid) == 4:
            r1, r2 = 2, 2
        elif len(grid) == 9:
            r1, r2 = 3, 3
        elif len(grid) == 6:
            r1, r2 = 2, 3
        elif len(grid) == 8:
            r1, r2 = 2, 4
        else:
            r1, r2 = 1, 1
            
        r, c = coord
        start_r = (r // r1) * r1
        start_c = (c // r2) * r2
        for i in range(start_r, start_r + r1):
            for j in range(start_c, start_c + r2):
                if grid[i][j] == digit:
                    return False
        return True
    
    # ------------------
    # Custom constraints
    # ------------------
    @staticmethod
    def diagonal_constraint(grid, coord, digit):
        r, c = coord
        n = len(grid)
        
        if r == c:
            for i in range(n):
                if grid[i][i] == digit:
                    return False
                
        return True
    # IS IT NOT BETTER TO TEST FOR 1 to 9 UNIQUE HERE INSTEAD OF CHECKING REPEATS?

    @staticmethod
    def antidiagonal_constraint(grid, coord, digit):
        r, c = coord
        n = len(grid)
        
        if r + c == n - 1:
            for i in range(n):
                if grid[i][n - 1 - i] == digit:
                    return False
                
        return True
    
    @staticmethod
    def arrow_constraint(grid, coords, root_digit):
        '''
        Digits along the arrow sum to the digit in the root.
        The first digit in the `coord` list is the root of the arrow.
        '''
        arrow = [(0,0), (0,1), (0,2)]
        root = arrow[0]
        arrow_cells = arrow[1:]

        r, c = coords

        # Temporarily place a digit
        grid[r][c] = root_digit

        root_val = grid[root[0]][root[1]]

        total = 0
        filled = True

        for ar, ac in arrow_cells:
            val = grid[ar][ac]
            if val == 0:
                filled = False
            total += val

        grid[r][c] = 0

        if root_val != 0:
            if total > root_val:
                return False
            if filled and total != root_val:
                return False

        return True

def isValidDigit(grid: Grid, digit: int, coord: Coord, custom_constraints: Constraint) -> bool:
    '''
    Checks if a proposed digit is valid according to a list of constraints.
    '''
    n = len(grid)
    constraints = [
        Constraint("row",       [(r, 0) for r in range(n)],                     Constraint.row_constraint),
        Constraint("col",       [(0, c) for c in range(n)],                     Constraint.col_constraint),
        Constraint("region",    [(r, c) for r in range(n) for c in range(n)],   Constraint.region_constraint),
        *(custom_constraints or [])
    ]

    for constraint in constraints:
        if not constraint.check(grid, coord, digit):
            return False
    return True

# def _isValidGrid(grid: Grid) -> bool:
#     '''
#     Checks if a solution is valid
#     '''
#     n = len(grid[0])
#     conj_grid = list(np.array(grid).transpose())

#     # Only true for 4*4 grids  
#     r1 = 2
#     r2 = 2
#     all_digits = set(range(1, r1 * r2 + 1))

#     for i in range(n):
#         row = {grid[i]}
#         col = {conj_grid[i]}
#         if row != all_digits or col != all_digits:
#             return False

#     for i in range(0, n, r1):
#         for j in range(0, n, r2):
#             region = {grid[x][y]
#                         for x in range(i, i + r1)
#                         for y in range(j, j + r2)}
#             if region != all_digits:
#                 return False
#     return True