# Sudoku solver v0.1.0
# Written by J.J. Postema

from sudoku.constraints import *
from sudoku.solvers import *
from sudoku.utils import *

if __name__ == "__main__":
    # Pull a grid from a .txt file
    grid = pull("Example 1", filename = "puzzles/4x4.txt")

    # Solve and time
    @timer(enabled = True)
    def solve(grid):
        return solveBackTrack(grid)
    
    # Print the solution
    print(solve(grid))