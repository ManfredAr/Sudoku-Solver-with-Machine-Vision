from SudokuSolver2 import SudokuSolver2
from SudokuSolver import SudokuSolver
from Sudoku import Sudoku
import time

a = SudokuSolver2(Sudoku([[0,9,0,8,0,0,0,6,0],
                          [6,0,7,0,2,0,1,0,0],
                          [0,3,0,0,0,7,0,0,0],
                          [8,0,4,0,0,9,0,1,0],
                          [0,0,0,5,0,0,2,0,0],
                          [0,6,0,0,0,0,0,0,0],
                          [0,0,0,0,9,0,0,0,4],
                          [0,0,3,0,0,0,0,0,0],
                          [7,0,1,0,0,4,0,8,0]]))
start = time.time()
print(a.solver())
end = time.time()
print(end - start)


b = SudokuSolver(Sudoku([[0,9,0,8,0,0,0,6,0],
                          [6,0,7,0,2,0,1,0,0],
                          [0,3,0,0,0,7,0,0,0],
                          [8,0,4,0,0,9,0,1,0],
                          [0,0,0,5,0,0,2,0,0],
                          [0,6,0,0,0,0,0,0,0],
                          [0,0,0,0,9,0,0,0,4],
                          [0,0,3,0,0,0,0,0,0],
                          [7,0,1,0,0,4,0,8,0]]))
start = time.time()
print(b.solver())
end = time.time()
print(end - start)
