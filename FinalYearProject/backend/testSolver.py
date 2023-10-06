from SudokuSolver import SudokuSolver
from Sudoku import Sudoku
import time



a = SudokuSolver(Sudoku([[0,8,0,1,3,0,0,4,0],
                        [0,0,0,5,9,8,0,1,6],
                        [0,1,2,0,0,0,0,5,0],
                        [0,0,0,4,0,7,0,9,0],
                        [0,4,0,0,0,5,0,6,0],
                        [0,0,0,0,0,0,0,2,0],
                        [6,0,0,0,0,0,0,0,0],
                        [1,5,0,0,0,0,6,0,2],
                        [0,7,0,0,0,0,0,8,9]]))
start = time.time()
print(a.solver())
end = time.time()
print(end - start)