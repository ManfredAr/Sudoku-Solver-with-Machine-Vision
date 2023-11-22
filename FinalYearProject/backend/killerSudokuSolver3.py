from killerSudokuHeap2 import KillerSudokuHeap2

class KillerSudokuSolver3:
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
        self.queue = KillerSudokuHeap2()
        

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
        priority, cageLength, cell, domain, cageSum = queue.pop_cell()
        if priority == None:
            return True
    
        if priority == 0 or cageLength == 0:
            queue.addToHeap((priority, cageLength, cell, domain, cageSum))
            return False
    
        for value in domain:
            if cageLength != 1 or (cageLength == 1 and value == cageSum):
                self.KSudoku.grid[cell[0]][cell[1]] = value
                updatedCells = self.decreaseKeys(cell, value)
                if self.solve(queue):
                    return True
                self.KSudoku.grid[cell[0]][cell[1]] = 0
                queue.increaseKey(updatedCells)

        # if backtracking occurs then insert the cell and its values back into the queue
        # since it was the first element just it back in the first index.
        queue.addToHeap((priority, cageLength, cell, domain, cageSum))
        return False
    



    def getDomain(self, row, col):
        '''
        For a given cell find the valid choices for this cell.

        Parameters:
        row - the row the cell is in.
        col - the column the cell is in.

        Returns:
        An array containing the possible values.
        '''
        used = set()
        cageCells = self.KSudoku.getCageCells(row, col)
        nonCageCells = self.KSudoku.getRelatedCells(row, col)
        cageSum = self.KSudoku.getCageSum(row, col)

        for i in nonCageCells:
            if self.KSudoku.grid[i[0]][i[1]] > 0:
                used.add(self.KSudoku.grid[i[0]][i[1]])

        for i in cageCells:
            if self.KSudoku.grid[i[0]][i[1]] != 0:
                cageSum = cageSum - self.KSudoku.grid[i[0]][i[1]]
                used.add(self.KSudoku.grid[i[0]][i[1]])

        upLim = self.upperLimit(len(cageCells), cageSum)
        lowLim = self.lowerLimit(len(cageCells), cageSum)
        validGuesses = set([1,2,3,4,5,6,7,8,9]) - used
        validGuesses = {i for i in validGuesses if i <= upLim and i >= lowLim}

        return validGuesses




    def upperLimit(self, numVariables, cageSum):
        lowSum = (0,1,3,6,10,15,21,28,36,45)
        upper = 9
        while True:
            if upper + lowSum[numVariables-1] > cageSum:
                upper -= 1
            else:
                break
        return upper
    



    def lowerLimit(self, numVariables, cageSum):
        highSum = (0,9,17,24,30,35,39,42,44,45)
        lower = 1
        while True:
            if lower + highSum[numVariables-1] < cageSum:
                lower += 1
            else:
                break
        return lower




    def setupHeap(self):
        '''
        Goes through the entire grid and inserts each empty cell into the priority queue.
        '''
        for cage_number, cage_dict in self.KSudoku.cages.items():
            for cage_sum, cells in cage_dict.items():
                values = self.getDomain(cells[0][0],cells[0][1])
                for cell in cells:
                    self.queue.addToHeap((len(values), len(self.KSudoku.getCageCells(cell[0], cell[1])), (cell[0],cell[1]), values, cage_sum))




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
                check = self.queue.decreaseCageKey(j, val)
                if check != None:
                    changed.append(check)

        return changed