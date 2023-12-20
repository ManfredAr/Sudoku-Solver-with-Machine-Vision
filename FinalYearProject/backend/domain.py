import copy

class Domain:
    '''
    This class is responsible for finding the domains for sudoku and killer sudoku.
    '''

    def __init__(self, grid):
        '''
        constructor for the class

        parameters:
        grid - a 2D array containing the puzzle. 
        '''
        self.grid = grid


    def getAllDomains(self):
        '''
        Finds the possible domains for each empty cell within a puzzle.

        Returns:
        A 2d array where each cell is replaced with the domain of the cell. 
        -1 is placed if a cell is already filled. 
        '''
        domainGrid = copy.deepcopy(self.grid.copy())
        for i in range(9):
            for j in range(9):
                if domainGrid[i][j] == 0:
                    domainGrid[i][j] = self.getDomain(i, j)
                else:
                    domainGrid[i][j] = -1
        return domainGrid


    
    def getDomain(self, row, col):
        '''
        Returns all the values which do not break any constraint rules for the cell.

        Parameters:
        row - the row of the cell
        col - the column of the cell

        Returns:
        A set containing the possible valid numbers
        '''
        used = []

        for i in range(9):
            #get all values in the row
            if self.grid[row][i] > 0:
                used.append(self.grid[row][i])

            # get all values in the column
            if self.grid[i][col] > 0:
                used.append(self.grid[i][col])


        #get all values in the box
        box_row = (row // 3) * 3
        col_box = (col // 3) * 3

        for i in range(box_row, box_row + 3):
            for j in range(col_box, col_box + 3):
                used.append(self.grid[i][j])

        # getting all unique values
        used = set(used)
        return set([1,2,3,4,5,6,7,8,9]) - used