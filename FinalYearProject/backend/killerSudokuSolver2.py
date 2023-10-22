from KillerSudokuHeap import KillerSudokuHeap


class KillerSudokuSolver2:
    '''
    A class which deals with solving killer sudoku puzzles.
    '''

    def __init__(self, killerSudoku):
        '''
        The constructor method and takes a KillerSudoku object

        Parameter:
        A killerSudoku object
        '''
        self.KSudoku = killerSudoku
        self.queue = KillerSudokuHeap()
        

    def solver(self):
        '''
        It uses a range of techniques to solve a sudoku puzzle.

        Returns:
        the completed puzzle if a solution was found
        False if no solution was found.
        '''
        self.setupHeap()
        if self.solve(self.queue) == True:
            return self.KSudoku.grid
        return False
    

    def solve(self, queue):
        '''
        A backtracking method which recusively tries values for cells
        until the entire grid is complete or a solution is not possible. 

        Returns:
        boolean depending on if the puzzle was solved or not.
        '''
        
        # gets the cell with the lowest domain length
        priority, cell, domain = queue.pop_cell()
        if priority == None:
            return True
    
        if priority == 0:
            queue.addToHeap((priority, cell, domain))
            return False

        for value in domain:
            self.KSudoku.grid[cell[0]][cell[1]] = value
            updatedCells = self.decreaseKeys(cell, value)
            if self.solve(queue):
                return True
            self.KSudoku.grid[cell[0]][cell[1]] = 0
            queue.increaseKey(updatedCells)

        # if backtracking occurs then insert the cell and its values back into the queue
        # since it was the first element just it back in the first index.
        queue.addToHeap((priority, cell, domain))
        return False
    
    
    def getDomain(self, row, col):
        '''
        For a given cell find the valid choices for this cell.

        Parameters:
        row - the row the cell is in.
        col - the column the cell is in.

        Returns:
        An array containing the possiblle values.
        '''
        used = []
        cageCells = self.KSudoku.getCageCells(row, col)
        nonCageCells = self.KSudoku.getRelatedCells(row, col)
        cageSum = self.KSudoku.getCageSum(row, col)

        for i in nonCageCells:
            if self.KSudoku.grid[i[0]][i[1]] > 0:
                used.append(self.KSudoku.grid[i[0]][i[1]])

        count = 0
        for i in cageCells:
            if self.KSudoku.grid[i[0]][i[1]] != 0:
                cageSum = cageSum - self.KSudoku.grid[i[0]][i[1]]
                used.append(self.KSudoku.grid[i[0]][i[1]])
                count += 1

        if cageSum <= 0:
            return {}
        
        if count == len(cageCells) - 1:
            if cageSum > 9 or cageSum in set(used):
                return {}
            return {cageSum}


        used = set(used)
        validGuesses = set([1,2,3,4,5,6,7,8,9]) - used
        validGuesses = {i for i in validGuesses if i <= cageSum}
        return validGuesses


    

    def setupHeap(self):
        '''
        Goes through the entire grid and inserts each empty cell into the priority queue.
        '''
        for i in range(9):
            for j in range(9):
                if self.KSudoku.grid[i][j] == 0:
                    values = self.getDomain(i, j)
                    self.queue.addToHeap((len(values), (i,j), values))



    def decreaseKeys(self, cell, val):
        
        '''
        It updates the cells in the queue to reduce the domains due to a guess being made.

        Parameter:
        A tuple containing the row and column of a cell

        Returns:
        An array containing all changed cells.
        '''
        cageCells = set(self.KSudoku.getCageCells(cell[0], cell[1]))
        nonCageCells = self.KSudoku.getRelatedCells(cell[0], cell[1])

        nonCageCells -= cageCells
        changed = []
        for i in nonCageCells:
            if self.KSudoku.grid[i[0]][i[1]] == 0:
                ret = self.queue.decreaseNonCageKey(i, val)
                if ret != None:
                    changed.append(ret)

        for j in cageCells:
            if self.KSudoku.grid[j[0]][j[1]] == 0:
                values = self.getDomain(j[0], j[1])
                check = self.queue.decreaseCageKey(j, values)
                if check != None:
                    changed.append(check)
        return changed