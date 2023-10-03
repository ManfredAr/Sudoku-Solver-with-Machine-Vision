class Sudoku:
    '''
    Used to store the grid for the sudoku puzzle.
    '''

    def __init__(self, grid):
        '''
        initializes the class and the grid.
        '''
        self.grid = grid


    def isValid(self):
        '''
        Checks whether the rows, columns and 3x3 box does not contain duplicates.

        Returns:
        True if no duplicates and false otherwise.
        '''
        for i in range(9):
            if self.checkRow(i) == False or self.checkCol(i) == False or self.checkBox(i//3, i%3) == False:
                return False
        return True
    

    def checkRow(self, row):
        '''
        Checks that no duplicates appear in a row.
        Parameters:
        row - the row to be checked.

        Returns:
        True if no duplicates and false otherwise.
        '''
        unique_values = {}
        for i in range(9):
            if self.grid[row][i] != 0 and self.grid[row][i] in unique_values:
                return False
            unique_values[self.grid[row][i]] = 1
        return True
    

    def checkCol(self, col):
        '''
        Checks that no duplicates appear in a column.
        Parameters:
        col - the column to be checked.
        
        Returns:
        True if no duplicates and false otherwise.
        '''
        unique_values = {}
        for i in range(9):
            if self.grid[i][col] != 0 and self.grid[i][col] in unique_values:
                return False
            unique_values[self.grid[i][col]] = 1
        return True
    

    def checkBox(self, row, col):
        '''
        Checks that no duplicates appear in a 3x3 box.
        Parameters:
        col - the column of the box in the 3x3 grid.
        row - the row of the box in the 3x3 grid.

        Returns:
        True if no duplicates and false otherwise.
        '''
        row = row * 3
        col = col * 3
        unique_values = {}
        for i in range(3):
            for j in range(3):
                if self.grid[row+i][col+j] != 0 and self.grid[row+i][col+j] in unique_values:
                    return False
                unique_values[self.grid[row+i][col+j]] = 1
        return True
    

    def getGrid(self):
        '''
        Getter method for the grid.
        Return
        the grid.
        '''
        return self.grid