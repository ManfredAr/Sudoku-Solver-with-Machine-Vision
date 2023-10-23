from backend.heap import heap

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
        self.heap = heap()
        self.removed = {}
    
    def solver(self):
        '''
        Tries to find a solution to the puzzle.

        Returns
        The completed grid if a solution was found, False otherwise.
        '''
        self.setupHeap()
        if self.solve(self.heap) == True:
            return self.sudoku.grid
        return False


    def solve(self, pq):
        '''
        Recursively tries to add values into the grid to complete it.

        Returns:
        True if a solution was found, False otherwise
        '''

        # getting the cell with the smallest domain
        length, count, cell, domain = pq.pop_cell()
        self.removed[cell] = (length, cell, domain)

        # if the length of the queue is empty it means that all the cells have a value
        # inserted and since no incorrect choice has been made it is the correct solution so we can return True.
        if length == None:
            return True
        
        # if the length is 0 it means a mistake was made in a previous cell leaving no valid options for 
        # the current cell. Therefore we need to backtrack.
        if length == 0:
            pq.addToHeap(self.removed[(cell[0], cell[1])])
            return False

        for value in domain:
            self.sudoku.grid[cell[0]][cell[1]] = value
            # updating domains for affected cells.
            updatedCells = pq.decreaseKey(cell[0], cell[1], value)

            if self.solve(pq) == True:
                return True
            # reseting the grid and queue to before a value was assigned.
            self.sudoku.grid[cell[0]][cell[1]] = 0
            pq.increaseKey(updatedCells)
            updatedCells = []
        
        pq.addToHeap(self.removed[(cell[0], cell[1])])
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
    

    def setupHeap(self):
        '''
        Goes through the entire grid and inserts each empty cell into the priority queue.
        '''
        for i in range(9):
            for j in range(9):
                if self.sudoku.grid[i][j] == 0:
                    values = self.getDomain(i, j)
                    self.heap.addToHeap((len(values), (i,j), values))
