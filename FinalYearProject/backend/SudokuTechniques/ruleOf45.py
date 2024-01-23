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

        for i in range(1, 8):
            for j in range(9):
                if j+i < 9:
                    grid, message = self.checkRuleOfKRow(j, j+i, domain)
                    if message is not None:
                        m = "rule of k in rows ", j, " to ", j+i
                        return grid, m
                    grid, message = self.checkRuleOfKRow(j, j+i, domain)
                    if message is not None:
                        m = "rule of k in col ", j, " to ", j+i
                        return grid, message


        for i in range(0, 9):
            grid, message = self.checkRuleOf45Box(i//3, i%3, domain)
            if message is not None:
                return grid, message
        return None, None


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
                    outArea = 0
                    outFilledArea = 0
                    outAmount = 0
                    for cell in cells:
                        boxed.add((cell[0] // 3, cell[1] // 3))
                        if self.killerSudoku.grid[cell[0]][cell[1]] != 0 and cell[0] // 3 == row and cell[1] // 3 == col:
                            total += self.killerSudoku.grid[cell[0]][cell[1]]
                            inAreaFilled.append(cell)
                        if cell[0] // 3 != row or cell[1] // 3 != col:
                            outArea += 1
                            if self.killerSudoku.grid[cell[0]][cell[1]] != 0:
                                outFilledArea += 1
                                outAmount += self.killerSudoku.grid[cell[0]][cell[1]]
                    if outArea != 0 and outArea == outFilledArea:
                        total -= cageSum - outAmount
                        contained.add(cageNum)
                    if len(boxed) == 1:
                        total -= cageSum
                        contained.add(cageNum)
                    else:
                        uncontained += inAreaFilled
                        if uncontainedCageNum != -1:
                            return None, None
                        uncontained.append((i,j))
                        uncontainedCageNum = cageNum
        if len(uncontained) == 0 or total == 0:
            return None, None
        message = "rule of 45 in box", (row, col)
        return self.reduceDomains(uncontained, uncontainedCageNum, total, domain), message


    def checkRuleOfKRow(self, row1, row2, domain):
        '''
        Tries to apply the rule of 45 to the row.

        parameters:
        row - the row to apply the rule
        domain - a 2d array with the domains for each cell.

        returns:
        none if technique isnt used. 
        A new domain which is changed to reflect the technique usage.  
        '''
        total = 45 * ((row2 - row1) + 1) 
        uncontainedCageNum = -1
        uncontained = []
        contained = set()
        for row in range(row1, row2+1):
            for i in range(0, 9):
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
                    outArea = 0
                    outFilledArea = 0
                    outAmount = 0
                    for cell in cells:
                        if not (cell[0] >= row1 and cell[0] <= row2):
                            width.add(cell[0])
                        if self.killerSudoku.grid[cell[0]][cell[1]] != 0 and (cell[0] >= row1 and cell[0] <= row2):
                            total += self.killerSudoku.grid[cell[0]][cell[1]]
                            inAreaFilled.append(cell)
                        if not (cell[0] < row1 and cell[0] > row2):
                            outArea += 1
                            if self.killerSudoku.grid[cell[0]][cell[1]] != 0:
                                outFilledArea += 1
                                outAmount += self.killerSudoku.grid[cell[0]][cell[1]]
                    if outArea != 0 and outArea == outFilledArea:
                        total -= cageSum - outAmount
                        contained.add(cageNum)
                    elif len(width) == 0:
                        total -= cageSum
                        contained.add(cageNum)
                    else:
                        uncontained += inAreaFilled
                        if uncontainedCageNum != -1:
                            return None, None
                        uncontained.append((row,i))
                        uncontainedCageNum = cageNum
        if len(uncontained) == 0 or total == 0:
            return None, None
        message = "rule of k in row", row
        return self.reduceDomains(uncontained, uncontainedCageNum, total, domain), message
    

    def checkRuleOfKColumn(self, column1, column2, domain):
        '''
        Tries to apply the rule of 45 to the column.

        parameters:
        column - the column to apply the rule
        domain - a 2d array with the domains for each cell.

        returns:
        none if technique isnt used. 
        A new domain which is changed to reflect the technique usage.  
        '''
        total = 45 * ((column2 - column1) + 1) 
        uncontainedCageNum = -1
        uncontained = []
        contained = set()
        for column in range(column1, column2+1):
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
                    outArea = 0
                    outFilledArea = 0
                    outAmount = 0
                    for cell in cells:
                        if not (cell[1] >= column1 and cell[1] <= column2):
                            height.add(cell[1])
                        if self.killerSudoku.grid[cell[0]][cell[1]] != 0 and (cell[1] >= column1 and cell[1] <= column2):
                            total += self.killerSudoku.grid[cell[0]][cell[1]]
                            inAreaFilled.append(cell)
                        if not (cell[1] < column1 and cell[1] > column2):
                            outArea += 1
                            if self.killerSudoku.grid[cell[0]][cell[1]] != 0:
                                outFilledArea += 1
                                outAmount += self.killerSudoku.grid[cell[0]][cell[1]]
                    if outArea != 0 and outArea == outFilledArea:
                        total -= cageSum - outAmount
                        contained.add(cageNum)
                    elif len(height) == 0:
                        total -= cageSum
                        contained.add(cageNum)
                    else:
                        uncontained += inAreaFilled
                        if uncontainedCageNum != -1:
                            return None, None
                        uncontained.append((i,column))
                        uncontainedCageNum = cageNum
        if len(uncontained) == 0 or total == 0:
            return None, None
        message = "rule of k in column", column
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
        inArea = []
        inAreaSum = remainingSum
        notInArea = []
        notInAreaSum = 0
        for cageSum, cells in cage.items():
            notInAreaSum = cageSum - remainingSum
            for cell in cells:
                if tuple(cell) in inCagecells or cell in inCagecells:
                    if self.killerSudoku.grid[cell[0]][cell[1]] != 0:
                        inAreaSum -= self.killerSudoku.grid[cell[0]][cell[1]]
                    else:
                        inArea.append(cell)
                else:
                    if self.killerSudoku.grid[cell[0]][cell[1]] != 0:
                        notInAreaSum -= self.killerSudoku.grid[cell[0]][cell[1]]
                    else:
                        notInArea.append(cell)

        kdomain = KillerSudokuDomain(self.killerSudoku)
        inSelectedOptions = kdomain.getOptions(len(inCagecells), remainingSum)
        for i in inCagecells:
            if self.killerSudoku.grid[i[0]][i[1]] == 0:
                domain[i[0]][i[1]] = domain[i[0]][i[1]].intersection(inSelectedOptions)

        if len(notInArea) != 0:
            notSelectedOptions = kdomain.getOptions(len(notInArea), notInAreaSum)
            for i in notInArea:
                if self.killerSudoku.grid[i[0]][i[1]] == 0:
                    domain[i[0]][i[1]] = domain[i[0]][i[1]].intersection(notSelectedOptions)
 

        return domain
