import copy
from backend.cageCombinations import CageCombinations

class KillerSudokuDomain:

    def __init__(self, killerSudoku):
        self.killerSudoku = killerSudoku
        self.grid = killerSudoku.grid
        self.cages = killerSudoku.cages
        self.combinations = CageCombinations()


#    def getAllDomains(self):
#        domainGrid = copy.deepcopy(self.grid.copy())
#        for i in range(len(domainGrid)):
#            for j in range(len(domainGrid[0])):
#                numVar = len(self.killerSudoku.getCageCells(i, j))
#                cageSum = self.killerSudoku.getCageSum(i, j)
#                domain = self.combinations.getDomain(numVar, cageSum)
#                used = self.getUsedValues(i, j)
#                domainGrid[i][j] = domain - used
#
#        return domain
    

    def getDomain(self, row, col):
        cageCells = self.killerSudoku.getCageCells(row, col)
        numVar = len(cageCells)
        cageSum = self.killerSudoku.getCageSum(row, col)
        domain = self.combinations.getDomain(numVar, cageSum)
        used = self.getUsedValues(row, col)

        RemainingCells = numVar
        RemainingTotal = cageSum

        for i in cageCells:
            if self.killerSudoku.grid[i[0]][i[1]] != 0:
                RemainingCells -= 1
                RemainingTotal -= self.killerSudoku.grid[i[0]][i[1]]

        if RemainingCells == numVar:
            return domain - used, RemainingCells, RemainingTotal    

        combinations = self.combinations.getDomain(RemainingCells, RemainingTotal)

        return combinations - used, RemainingCells, RemainingTotal  
    


    def getUsedValues(self, row, col):
        '''
        For a given cell find values which acnnot appear in this cell.

        Parameters:
        row - the row the cell is in.
        col - the column the cell is in.

        Returns:
        An array containing the used values.
        '''
        used = set()
        cageCells = self.killerSudoku.getCageCells(row, col)
        nonCageCells = self.killerSudoku.getRelatedCells(row, col)
        cageSum = self.killerSudoku.getCageSum(row, col)

        for i in nonCageCells:
            if self.killerSudoku.grid[i[0]][i[1]] > 0:
                used.add(self.killerSudoku.grid[i[0]][i[1]])

        for i in cageCells:
            if self.killerSudoku.grid[i[0]][i[1]] != 0:
                cageSum = cageSum - self.killerSudoku.grid[i[0]][i[1]]
                used.add(self.killerSudoku.grid[i[0]][i[1]])

        return used