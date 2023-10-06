from backend.Sudoku import Sudoku


class KillerSudoku:
    '''
    Used to store the grid and the cages for a killer sudoku.
    '''

    def __init__(self, grid, cages):
        '''
        Initializes the grid and the cages. It also initializes a new dictionary which 
        maps the individual cells to the cage number.

        Parameters: 
        grid - the killer sudoku grid in a 2D array.
        cages - a dictionary with the cells within the cage in an array as the key and the sum of the cage as the value.
        '''
        self.grid = grid
        self.cages = cages
        self.cellCage = {}
        self.convertCageToCellCages()


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

        for cage_number, cage_dict in self.cages.items():
            for cage_sum in cage_dict.keys():
                total += cage_sum
        
        return total == 405 
    

    def convertCageToCellCages(self):
        '''
        Creates a new dictionary which maps an individual cell to its cage number.
        '''
        for cage_number, cage_dict in self.cages.items():
            for cage_sum, cells in cage_dict.items():
                for cell in cells:
                    self.cellCage[cell] = cage_number
        

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
