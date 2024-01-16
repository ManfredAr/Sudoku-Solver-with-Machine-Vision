import copy
from backend.KSudokuDomain import KillerSudokuDomain

class ruleOf45:
    '''
    This class is an implementation of the rule for 45 killer sudoku technique. 
    '''

    def __init__(self, killerSudoku):
        '''
        A constructor for the class

        parameters:
        killerSudoku - a killerSudoku object containing the puzzle
        '''
        self.killerSudoku = killerSudoku
        self.cageLayout = copy.deepcopy(killerSudoku.grid)
        for i in range(9):
            for j in range(9):
                self.cageLayout[i][j] = self.killerSudoku.cellCage[(i,j)]


    def checkRuleOf45(self, domain):
        '''
        Tries to apply the rule of 45 to every column, row and box in the puzzle.

        parameter:
        domain - a 2d array with the domains for each cell.
        '''
        for i in range(0, 9):
            grid, message = self.checkRuleOf45Row(i, domain)
            if message is not None:
                return grid, message
            grid, message = self.checkRuleOf45Column(i, domain)
            if message is not None:
                return grid, message
            grid, message = self.checkRuleOf45Box(i//3, i%3, domain)
            if message is not None:
                return grid, message
        return None, None


    def checkRuleOf45Row(self, row, domain):
        '''
        Tries to apply the rule of 45 to the row.

        parameters:
        row - the row to apply the rule
        domain - a 2d array with the domains for each cell.

        returns:
        none if technique isnt used. 
        A new domain which is changed to reflect the technique usage.  
        '''
        total = 45
        uncontainedCageNum = -1
        uncontained = []
        contained = set()
        for i in range(9):
            cageNum = self.cageLayout[row][i]
            if self.killerSudoku.grid[row][i] != 0:
                total -= self.killerSudoku.grid[row][i]
                continue
            if cageNum in contained:
                continue
            if cageNum == uncontainedCageNum:
                uncontained.append((row,i))
                continue

            cage = self.killerSudoku.cages[cageNum]
            for cageSum, cells in cage.items():
                width = set()
                inAreaFilled = []
                for cell in cells:
                    width.add(cell[0])
                    if self.killerSudoku.grid[cell[0]][cell[1]] != 0 and cell[0] == row:
                        total += self.killerSudoku.grid[cell[0]][cell[1]]
                        inAreaFilled.append(cell)
                if len(width) == 1:
                    total -= cageSum
                    contained.add(cageNum)
                else:
                    uncontained += inAreaFilled
                    if uncontainedCageNum != -1:
                        return None, None
                    uncontained.append((row,i))
                    uncontainedCageNum = cageNum
        message = "rule of 45 in row", row
        return self.reduceDomains(uncontained, uncontainedCageNum, total, domain), message


    def checkRuleOf45Column(self, column, domain):
        '''
        Tries to apply the rule of 45 to the column.

        parameters:
        column - the column to apply the rule
        domain - a 2d array with the domains for each cell.

        returns:
        none if technique isnt used. 
        A new domain which is changed to reflect the technique usage.  
        '''
        total = 45
        uncontainedCageNum = -1
        uncontained = []
        contained = set()
        for i in range(9):
            cageNum = self.cageLayout[i][column]
            if self.killerSudoku.grid[i][column] != 0:
                total -= self.killerSudoku.grid[i][column]
                continue
            if cageNum in contained:
                continue
            if cageNum == uncontainedCageNum:
                uncontained.append((i,column))
                continue

            cage = self.killerSudoku.cages[cageNum]
            for cageSum, cells in cage.items():
                height = set()
                inAreaFilled = []
                for cell in cells:
                    height.add(cell[1])
                    if self.killerSudoku.grid[cell[0]][cell[1]] != 0 and cell[1] == column:
                        total += self.killerSudoku.grid[cell[0]][cell[1]]
                        inAreaFilled.append(cell)
                if len(height) == 1:
                    total -= cageSum
                    contained.add(cageNum)
                else:
                    uncontained += inAreaFilled
                    if uncontainedCageNum != -1:
                        return None, None
                    uncontained.append((i,column))
                    uncontainedCageNum = cageNum

        message = "rule of 45 in column", column
        return self.reduceDomains(uncontained, uncontainedCageNum, total, domain), message
    


    def checkRuleOf45Box(self, row, col, domain):
        '''
        Tries to apply the rule of 45 to the box.

        parameters:
        row, col - the index of the box to apply the rule.
        domain - a 2d array with the domains for each cell.

        returns:
        none if technique isnt used. 
        A new domain which is changed to reflect the technique usage.  
        '''
        total = 45
        uncontainedCageNum = -1
        uncontained = []
        contained = set()
        for i in range(row*3, row*3 + 3):
            for j in range(col*3, col*3 + 3):
                cageNum = self.cageLayout[i][j]
                if self.killerSudoku.grid[i][j] != 0:
                    total -= self.killerSudoku.grid[i][j]
                    continue
                if cageNum in contained:
                    continue
                if cageNum == uncontainedCageNum:
                    uncontained.append((i,j))
                    continue

                cage = self.killerSudoku.cages[cageNum]
                for cageSum, cells in cage.items():
                    boxed = set()
                    inAreaFilled = []
                    for cell in cells:
                        boxed.add((cell[0] // 3, cell[1] // 3))
                        if self.killerSudoku.grid[cell[0]][cell[1]] != 0 and cell[0] // 3 == row and cell[1] // 3 == col:
                            total += self.killerSudoku.grid[cell[0]][cell[1]]
                            inAreaFilled.append(cell)
                    if len(boxed) == 1:
                        total -= cageSum
                        contained.add(cageNum)
                    else:
                        uncontained += inAreaFilled
                        if uncontainedCageNum != -1:
                            return None, None
                        uncontained.append((i,j))
                        uncontainedCageNum = cageNum

        message = "rule of 45 in box", (row, col)
        return self.reduceDomains(uncontained, uncontainedCageNum, total, domain), message


    def reduceDomains(self, inCagecells, cageNum, remainingSum, domain):
        '''
        Reduces the domain of cell which are affected for the use of the rule of 45.

        parameters:
        inCageCell - an array of cells which are in the selected region but where the cage in not contained in the region.
        cageNum - the cage number of the cells.
        remainingSum - the amount the cells to sum up to.
        domain - a 2d array with the domains for each cell.

        returns
        a new domain which is reduced to reflect the use of the technique.
        '''
        cage = self.killerSudoku.cages[cageNum]
        notInCageCells = []
        nonSelectedSum = 0
        for cageSum, cells in cage.items():
            nonSelectedSum = cageSum - remainingSum
            for cell in cells:
                if self.killerSudoku.grid[cell[0]][cell[1]] != 0:
                    nonSelectedSum -= self.killerSudoku.grid[cell[0]][cell[1]]
                    continue
                if cell not in inCagecells:
                    notInCageCells.append(cell)

        kdomain = KillerSudokuDomain(self.killerSudoku)

        inSelectedOptions = kdomain.getOptions(len(inCagecells), remainingSum)
        for i in inCagecells:
            if self.killerSudoku.grid[i[0]][i[1]] == 0:
                domain[i[0]][i[1]] = domain[i[0]][i[1]].intersection(inSelectedOptions)

        if len(notInCageCells) != 0:
            notSelectedOptions = kdomain.getOptions(len(notInCageCells), nonSelectedSum)
            for i in notInCageCells:
                if self.killerSudoku.grid[i[0]][i[1]] == 0:
                    domain[i[0]][i[1]] = domain[i[0]][i[1]].intersection(notSelectedOptions)
 

        return domain


        