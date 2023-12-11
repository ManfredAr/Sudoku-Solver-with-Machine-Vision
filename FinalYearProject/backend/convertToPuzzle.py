import copy
from backend.Sudoku import Sudoku
from backend.SudokuSolver2 import SudokuSolver2

from backend.KillerSudoku import KillerSudoku
from backend.killerSudokuSolver3 import KillerSudokuSolver3

class convertToPuzzle:
    '''
    Converts frontend data into the correct form and returns 
    the solved puzzle if available.
    '''

    def __init__(self, puzzle, cages):
        '''
        constructor for the class
        
        Parameters:
        - puzzle: the puzzle grid in a 2d array
        - the dictionary containing the cages (only applicable to killer sudoku)
        '''
        if cages == None:
            self.puzzle = puzzle
            self.prevCages = None
        else:
            self.puzzle = puzzle
            self.prevCages = cages


    def validateSudoku(self):
        '''
        Covents frontend sudoku data to the correct form, validates if the puzzle is solvable and returns the solution.

        Returns:
        - 2d array containing the corrected puzzle grid
        - 2d array containing the solution, false if no solution is found. 
        '''
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
        return self.puzzle, solution


    def validateKSudoku(self):
        '''
        Converts the killer sudoku data into the correct form, and validates if a solution is possible.

        Returns:
        -The correct form of the puzzle and cages 
        - The solution to the problem (2D array)
        - False if no solution was found, or puzzle is not solvable.
        '''
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
        
        self.solver = KillerSudokuSolver3(self.Ksudoku)

        solution = self.solver.solver()

        return self.puzzle, self.cages, solution