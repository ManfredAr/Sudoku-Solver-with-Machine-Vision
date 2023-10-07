from collections import OrderedDict
import copy

class SudokuSolver2:
    '''
    A class which is used to solve sudoku grids.
    '''
    
    def __init__(self, grid):
        '''
        Constructor for the class
        
        Parameters:
        A sudoku object which contains the grid to be solved.
        '''
        self.sudoku = grid

    
    def solver(self):
        '''
        Tries to find a solution to the puzzle.

        Returns
        The completed grid if a solution was found, False otherwise.
        '''


        if self.solve(self.DomainQueue()) == True:
            return self.sudoku.grid
        return False


    def solve(self, queue):
        '''
        Recursively tries to add values into the grid to complete it.

        Returns:
        True if a solution was found, False otherwise
        '''

        if len(queue) == 0:
            return True
        
        # gets the cell with the lowest domain length
        row, col, val = queue.pop(0)

        domain = self.getDomain(row, col)

        for value in domain:
            self.sudoku.grid[row][col] = value
            if self.solve(queue) == True:
                return True
            self.sudoku.grid[row][col] = 0
            
        # if backtracking occurs then insert the cell and its values back into the queue
        # since it was the first element just it back in the first index.
        queue.insert(0, (row, col, val))
        return False

    

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
            if self.sudoku.grid[row][i] > 0:
                used.append(self.sudoku.grid[row][i])

            # get all values in the column
            if self.sudoku.grid[i][col] > 0:
                used.append(self.sudoku.grid[i][col])


        #get all values in the box
        box_row = (row // 3) * 3
        col_box = (col // 3) * 3

        for i in range(box_row, box_row + 3):
            for j in range(col_box, col_box + 3):
                used.append(self.sudoku.grid[i][j])

        # getting all unique values
        used = set(used)
        return set([1,2,3,4,5,6,7,8,9]) - used
    

    def DomainQueue(self):
        '''
        Gets the length of the domains for each empty cell. It then orders the array in 
        ascending order on the length of the domain.

        Returns:
        an array contain cells in order of length of domain.
        '''
        domains = []
        for i in range(9):
            for j in range(9):
                if self.sudoku.grid[i][j] == 0:
                    domains.append((i, j, len(self.getDomain(i, j))))
        domains = sorted(domains, key=lambda x: x[2])
        return domains
    