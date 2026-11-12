# Sudoku solver v0.1.0
# Written by J.J. Postema

from sudoku.constraints import *

def solveBackTrack(grid, custom_constraints = None) -> list[list[int]]:
    solution = [row[:] for row in grid]
    backlog = allEmptySquares(solution)
    
    num_empty = len(backlog)
    current = 0

    while True:
        r, c = backlog[current]
        temp_digit = solution[r][c]

        found = False
        for num in range(temp_digit + 1, len(grid[0]) + 1):
            if isValidDigit(solution, num, (r, c), custom_constraints):
                solution[r][c] = num
                found = True
                break

        if found:
            if current == num_empty - 1:
                return solution
            current += 1
        else:
            solution[r][c] = 0
            current -= 1
            if current < 0:
                raise IndexError("No solution found!")
            
def solveConstraintPropagation(grid) -> list[list[int]]:
    pass

def solveHeuristic(grid) -> list[list[int]]:
    pass

this is deliberately broken!!!
