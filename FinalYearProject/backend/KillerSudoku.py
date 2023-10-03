from backend.Sudoku import Sudoku


class KillerSudoku:
    '''
    Used to store the grid and the cages for a killer sudoku.
    '''

    def __init__(self, grid, cages):
        '''
        Initializes the grid and the cages.

        Parameters: 
        grid - the killer sudoku grid in a 2D array.
        cages - a dictionary with the cells within the cage in an array as the key and the sum of the cage as the value.
        '''
        self.grid = grid
        self.cages = cages


    def checkValid(self):
        '''
        Checks whether the rows, columns and 3x3 box does not contain duplicates and checks the sum of all cages adds to 405.

        Returns:
        True if the grid is valid and false otherwise.
        '''
        sudoku = Sudoku(self.grid)
        if sudoku.isValid() == False:
            return False
        return self.checkSum()
        

    def checkSum(self):
        '''
        Checks whether the sum of the cages adds up to 405.

        Returns:
        True if sum of cages is correct and false otherwise.
        '''
        total = 0
        for i in self.cages.values():
            total += i
        return total == 405 
        

    def getCages(self):
        '''
        Getter method for the cages.
        Return:
        the cages
        '''
        return self.cages
    
    def getGrid(self):
        '''
        Getter method for the grid.
        Return:
        the grid
        '''
        return self.grid
