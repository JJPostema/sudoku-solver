# Custom sudoku solver

Grids can be initialised through `grid = List[List[int]]` or pulled from .txt files using the `pull()` function. The solver is based on a bruteforce search; more advanced algorithms are coming soon.
Additional constraints can be written into the `Constraint` class, such as all digits appearing uniquely on a diagonal, Kropki dots, renban lines, German/Dutch whispers and many more.

# In future updates:

1) More advanced solvers.
2) Benchmarks for the speed of the solvers.
3) Custom constraints can be written to and pulled from .txt files.
