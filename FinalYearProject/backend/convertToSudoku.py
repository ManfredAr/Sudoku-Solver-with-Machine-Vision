import copy
from backend.Sudoku import Sudoku
from backend.SudokuSolver2 import SudokuSolver2

class convertToSudoku:

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def validatePuzzle(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[0])):
                if self.puzzle[i][j] == "-" or self.puzzle[i][j] == 0:
                    self.puzzle[i][j] = 0
                else:
                    self.puzzle[i][j] = int(self.puzzle[i][j])

        temp = copy.deepcopy(self.puzzle)
        self.sudoku = Sudoku(temp)

        if self.sudoku.isValid() == False:
            return False, False
        
        self.solver = SudokuSolver2(self.sudoku)

        solution = self.solver.solver()
        print(self.puzzle)
        return self.puzzle, solution



