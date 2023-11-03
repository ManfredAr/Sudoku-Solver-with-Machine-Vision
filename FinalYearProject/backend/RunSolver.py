from SudokuSolver2 import SudokuSolver2
from SudokuSolver import SudokuSolver
from Sudoku import Sudoku
import time


easy = [[6,0,0,0,0,9,0,0,4],
        [0,8,9,5,0,0,0,1,6],
        [5,0,0,0,6,0,3,0,9],
        [8,3,1,0,0,0,7,0,5],
        [0,2,0,0,0,0,0,6,0],
        [9,0,7,0,0,0,8,4,2],
        [2,0,6,0,1,0,0,0,8],
        [3,7,0,0,0,6,9,2,0],
        [1,0,0,3,0,0,0,0,7]]

medium = [[3,4,0,0,6,0,2,0,9],
        [2,0,8,4,9,0,0,0,6],
        [0,0,0,0,0,0,0,0,0],
        [0,2,0,3,1,0,0,0,0],
        [0,0,4,0,0,0,1,0,0],
        [0,0,0,0,2,5,0,4,0],
        [0,0,0,0,0,0,0,0,0],
        [9,0,0,0,5,1,4,0,3],
        [4,0,3,0,7,0,0,6,8]]

hard = [[0,0,6,5,0,0,0,0,8],
        [0,9,5,0,0,0,0,2,0],
        [7,0,0,9,0,0,3,0,0],
        [0,0,0,0,4,0,2,7,0],
        [0,0,0,8,7,3,0,0,0],
        [0,7,9,0,5,0,0,0,0],
        [0,0,2,0,0,8,0,0,9],
        [0,5,0,0,0,0,8,1,0],
        [3,0,0,0,0,5,4,0,0]]


#a = SudokuSolver(Sudoku(hard))
#start = time.time()
#print(a.solver())
#end = time.time()
#print(end - start)


b = SudokuSolver(Sudoku(hard))
start = time.time()
print(b.solver())
end = time.time()
print(end - start)
