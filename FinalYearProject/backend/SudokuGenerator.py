import copy
from backend.SudokuSolver2 import SudokuSolver2
from backend.Sudoku import Sudoku
import random

class SudokuGenerator:
    '''
    This class is responsible for generating Sudoku puzzles,
    of varying difficulty which are all valid.
    '''
    def __init__(self):
        '''
        constructor method for the class, instantiates an empty grid as well as difficulties.
        '''
        self.grid = [[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0]]
        self.easy = [40,41,42,43,44,45]
        self.medium = [46,47,48,49]
        self.hard = [50,51,52,53]
        self.expert = [54,55,56,57,58]

    
    def generate(self, difficulty):
        '''
        Generates a unique Sudoku puzzle with a sepcific difficulty.

        parameters:
        difficulty - an array containing numbers which is how many cells should be empty.

        returns:
        A 2D array containing the unque Sudoku puzzle.
        '''
        self.filledGrid()
        solution = copy.deepcopy(self.grid)
        if difficulty == "easy":
            self.removeNumbers(self.easy)
        elif difficulty == "medium":
            self.removeNumbers(self.medium)
        elif difficulty == "hard":
            self.removeNumbers(self.hard)
        elif difficulty == "expert":
            self.removeNumbers(self.expert)
        else:
            return None, None
        
        return self.grid, solution
        
            
        

    def filledGrid(self):
        '''
        Generates a completed Sudoku grid. Uses randomisation to generate
        different solutions each time.
        '''
        options = [1,2,3,4,5,6,7,8,9]
        random.shuffle(options)
        
        for i in range(0, 3):
            for j in range(0, 3):
                self.grid[i][j] = options[(i*3)+j]
        
        random.shuffle(options)
        for i in range(3, 6):
            for j in range(3, 6):
                self.grid[i][j] = options[((i-3)*3)+(j-3)]

        random.shuffle(options)
        for i in range(6, 9):
            for j in range(6, 9):
                self.grid[i][j] = options[((i-6)*3)+(j-6)]

        sudoku = Sudoku(self.grid)
        self.sudokuSolver = SudokuSolver2(sudoku)
        self.grid = self.sudokuSolver.solver()
    


    def removeNumbers(self, difficulty):
        '''
        Given a range of cells to be removed, It generates a unique Sudoku puzzle.

        parameters:
        difficulty: A 2D array containing the number of cells to be removed. 
        '''
        random.shuffle(difficulty)
        emptyCells = difficulty[0]
        
        for i in range(emptyCells):
            while True:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                if self.grid[x][y] == 0:
                    continue
                else:
                    removed_value = self.grid[x][y]
                    self.grid[x][y] = 0

                    # Check for unique solution after each removal
                    self.sudokuSolver.sudoku.grid = copy.deepcopy(self.grid)
                    solutions = self.sudokuSolver.SolutionFinder()

                    if solutions == 1:
                        break
                    else:
                        # if not a unique solution, revert the change
                        self.grid[x][y] = removed_value