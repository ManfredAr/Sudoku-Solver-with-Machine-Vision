from backend.SudokuHeap import SudokuHeap
from backend.domain import Domain

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
        self.heap = SudokuHeap()
        self.removed = {}
        self.domain = Domain(grid.grid)
    
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


    def setupHeap(self):
        '''
        Goes through the entire grid and inserts each empty cell into the priority queue.
        '''
        for i in range(9):
            for j in range(9):
                if self.sudoku.grid[i][j] == 0:
                    values = self.domain.getDomain(i, j)
                    self.heap.addToHeap((len(values), (i,j), values))
