import copy
from backend.Sudoku import Sudoku
from backend.SudokuSolver2 import SudokuSolver2

from backend.KillerSudoku import KillerSudoku
from backend.killerSudokuSolver2 import KillerSudokuSolver2

class convertToPuzzle:

    def __init__(self, puzzle, cages):
        if cages == None:
            self.puzzle = puzzle
        else:
            self.puzzle = puzzle
            self.prevCages = cages

    def validateSudoku(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[0])):
                if self.puzzle[i][j] == "-" or self.puzzle[i][j] == 0:
                    self.puzzle[i][j] = 0
                else:
                    self.puzzle[i][j] = int(self.puzzle[i][j])
        print(self.puzzle)

        temp = copy.deepcopy(self.puzzle)
        self.sudoku = Sudoku(temp)

        if self.sudoku.isValid() == False:
            return False, False
        
        self.solver = SudokuSolver2(self.sudoku)

        solution = self.solver.solver()
        print(self.puzzle)
        return self.puzzle, solution


    def validateKSudoku(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[0])):
                if self.puzzle[i][j] == "-" or self.puzzle[i][j] == 0:
                    self.puzzle[i][j] = 0
                else:
                    self.puzzle[i][j] = int(self.puzzle[i][j])

        self.cages = {}

        for cage_number, inner_dict in self.prevCages.items():
            for key, values in inner_dict.items():
                new_arr = []
                for i in range(len(values)):
                    new_arr.append((values[i][0], values[i][1]))
                self.cages[int(cage_number)] = {int(key): new_arr}

        temp = copy.deepcopy(self.puzzle)
        self.Ksudoku = KillerSudoku(temp, copy.deepcopy(self.cages))

        if self.Ksudoku.checkValid() == False:
            return False, False, False
        
        self.solver = KillerSudokuSolver2(self.Ksudoku)

        solution = self.solver.solver()

        return self.puzzle, self.cages, solution