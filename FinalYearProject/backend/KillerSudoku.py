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
                    #print(cell)
                    self.cellCage[(cell[0],cell[1])] = cage_number
        

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
    

    def getRelatedCells(self, row, col):
        '''
        Gets all the cells related to the given cell not including the cage cells

        Parameter:
        the row and column of the cell

        Returns:
        A set of cells in the row, column and box of the requested cell 
        '''
        connectCells = set()

        for i in range(9):
            connectCells.add((row, i))
            connectCells.add((i, col))

        box_row = (row // 3) * 3
        col_box = (col // 3) * 3

        for i in range(box_row, box_row + 3):
            for j in range(col_box, col_box + 3):
                connectCells.add((i, j))

        return connectCells
    

    def getCageCells(self, row, col):
        '''
        Returns all the cells in the given cells cage

        Parameter:
        the row and column of the cell

        Returns:
        An array of cells in the cage
        '''
        cageNum = self.cellCage.get((row,col))
        cells = next(iter(self.cages.get(cageNum).values()))
        return cells
    
    
    def getCageSum(self, row, col):
        '''
        Returns the sum that a cage should add up to.

        Parameter:
        the row and column of the cell

        Returns:
        The total sum of a cage.
        '''
        cageNum = self.cellCage.get((row,col))
        return next(iter(self.cages.get(cageNum)))
