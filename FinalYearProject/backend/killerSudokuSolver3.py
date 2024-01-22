from backend.killerSudokuHeap2 import KillerSudokuHeap2
import time

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
    
        if priority <= 0 or cageLength <= 0:
            queue.addToHeap((priority, cageLength, cell, domain, cageSum))
            return False
    
        for value in domain:
            self.KSudoku.grid[cell[0]][cell[1]] = value
            updatedCells, backtrack = self.decreaseKeys(cell, value, cageLength, cageSum)
            if backtrack == True:
                queue.increaseKey(updatedCells)
                self.KSudoku.grid[cell[0]][cell[1]] = 0
                continue

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
        nonZeroCageCells = 0

        for i in nonCageCells:
            if self.KSudoku.grid[i[0]][i[1]] > 0:
                used.add(self.KSudoku.grid[i[0]][i[1]])

        for i in cageCells:
            if self.KSudoku.grid[i[0]][i[1]] != 0:
                cageSum = cageSum - self.KSudoku.grid[i[0]][i[1]]
                used.add(self.KSudoku.grid[i[0]][i[1]])
                nonZeroCageCells += 1

        upLim = self.upperLimit(len(cageCells) - nonZeroCageCells, cageSum)
        lowLim = self.lowerLimit(len(cageCells) - nonZeroCageCells, cageSum)
        validGuesses = set([1,2,3,4,5,6,7,8,9]) - used
        validGuesses = {i for i in validGuesses if i <= upLim and i >= lowLim}

        return validGuesses


    def SolutionFinder(self):
        '''
        Tries to find the number of solution to the puzzle.

        Returns
        The number of solutions
        '''
        self.setupHeap()
        return self.NumberOfSolutions(self.queue)


    def NumberOfSolutions(self, queue):
        '''
        Recursively tries to add values into the grid to complete it.

        Returns:
        - The number of solutions found.
        '''  

        # gets the cell with the lowest domain length
        priority, cageLength, cell, domain, cageSum = queue.pop_cell()
        if priority is None:
            return 1  # solution found so try find other solutions.

        if priority <= 0 or cageLength <= 0:
            queue.addToHeap((priority, cageLength, cell, domain, cageSum))
            return 0  # solution not found so backtrack

        total_solutions = 0
        for value in domain:
            self.KSudoku.grid[cell[0]][cell[1]] = value
            updated_cells, backtrack = self.decreaseKeys(cell, value, cageLength, cageSum)

            if backtrack == True:
                queue.increaseKey(updated_cells)
                self.KSudoku.grid[cell[0]][cell[1]] = 0
                continue

            total_solutions += self.NumberOfSolutions(queue)
            # resetting the grid and queue to before a value was assigned.
            self.KSudoku.grid[cell[0]][cell[1]] = 0
            queue.increaseKey(updated_cells)

        # putting cell back into the queue        
        queue.addToHeap((priority, cageLength, cell, domain, cageSum))
        return total_solutions



    def upperLimit(self, numVariables, cageSum):
        '''
        Finds the upper limit of the cage depending on the number of variables and cage sum.

        parameters:
        numVariable - int containing the number of variables in the cage.
        cageSum - int containt the sum of the cage.

        returns:
        the upper limit the cell can contain.
        '''
        lowSum = (0,1,3,6,10,15,21,28,36,45)
        upper = 9
        while True:
            if upper + lowSum[numVariables-1] > cageSum:
                upper -= 1
            else:
                break
        return upper
    



    def lowerLimit(self, numVariables, cageSum):
        '''
        Finds the lower limit of the cage depending on the number of variables and cage sum.

        parameters:
        numVariable - int containing the number of variables in the cage.
        cageSum - int containt the sum of the cage.

        returns:
        the lower limit the cell can contain.
        '''
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
        for i in range(9):
            for j in range(9):
                if self.KSudoku.grid[i][j] == 0:
                    values = self.getDomain(i, j)
                    cageCells = self.KSudoku.getCageCells(i, j)
                    sumRem = self.KSudoku.getCageSum(i,j)
                    cellRem = len(cageCells)
                    for k in cageCells:
                        if self.KSudoku.grid[k[0]][k[1]] != 0:
                            cellRem -= 1
                            sumRem -= self.KSudoku.grid[k[0]][k[1]]

                    # adding each cell and its information into the queue.
                    self.queue.addToHeap((len(values), cellRem, (i,j), values, sumRem))


    def decreaseKeys(self, cell, val, cageLength, cageSum):
        '''
        It updates the cells in the queue to reduce the domains due to a guess being made.

        Parameter:
        cell - A tuple containing the row and column of a cell
        val - the value assigned to the cell
        cageLength - the number of unfilled cells in the cage
        cageSum - the remaining cage sum
        
        Returns:
        An array containing all changed cells.
        Also true to trigger a backtrack, false otherwise.
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
                upLim = self.upperLimit(cageLength-1, cageSum-val)
                lowLim = self.lowerLimit(cageLength-1, cageSum-val)
                check = self.queue.decreaseCageKey(j, val, lowLim, upLim)
                if check != None:
                    changed.append(check)

        # checks whether the domains can be reduced. 
        # during this process if the domain is empty then a backtrack is necessary.
        if self.queue.reduceDomain(cageCells, self.KSudoku) == False:
            return changed, True
        
        return changed, False