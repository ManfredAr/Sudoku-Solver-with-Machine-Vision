import copy
from backend.KSudokuDomain import KillerSudokuDomain

class ruleOf45:

    def __init__(self, killerSudoku):
        self.killerSudoku = killerSudoku
        self.cageLayout = copy.deepcopy(killerSudoku.grid)
        for i in range(9):
            for j in range(9):
                self.cageLayout[i][j] = self.killerSudoku.cellCage[(i,j)]


    def checkRuleOf45(self, domain):
        for i in range(0, 9):
            row, grid = self.checkRuleOf45Row(i, domain)
            if row is not None:
                return grid, row
            col, grid = self.checkRuleOf45Column(i, domain)
            if col is not None:
                return grid, col
            box, grid = self.checkRuleOf45Box(i//3, i%3, domain)
            if box is not None:
                return grid, box
        return None, None


    def checkRuleOf45Row(self, row):
        total = 45
        uncontainedCageNum = -1
        uncontained = []
        contained = set()
        for i in range(9):
            cageNum = self.cageLayout[row][i]
            if cageNum in contained:
                continue
            if cageNum == uncontainedCageNum:
                uncontained.append((row,i))
                continue

            cage = self.killerSudoku.cages[cageNum]
            for cageSum, cells in cage.items():
                rows = set(row for row, col in cells)
                if len(rows) == 1:
                    total -= cageSum
                    contained.add(cageNum)
                else:
                    if uncontainedCageNum != -1:
                        return None
                    uncontained.append((row,i))
                    uncontainedCageNum = cageNum

        return uncontained


    def checkRuleOf45Column(self, column):
        total = 45
        uncontainedCageNum = -1
        uncontained = []
        contained = set()
        for i in range(9):
            cageNum = self.cageLayout[i][column]
            if cageNum in contained:
                continue
            if cageNum == uncontainedCageNum:
                uncontained.append((i,column))
                continue

            cage = self.killerSudoku.cages[cageNum]
            for cageSum, cells in cage.items():
                cols = set(col for row, col in cells)
                if len(cols) == 1:
                    total -= cageSum
                    contained.add(cageNum)
                else:
                    if uncontainedCageNum != -1:
                        return None
                    uncontained.append((i,column))
                    uncontainedCageNum = cageNum

        return uncontained

    def checkRuleOf45Box(self, row, col):
        total = 45
        uncontainedCageNum = -1
        uncontained = []
        contained = set()
        for i in range(row*3, row*3 + 3):
            for j in range(col*3, col*3 + 3):
                cageNum = self.cageLayout[i][j]
                if cageNum in contained:
                    continue
                if cageNum == uncontainedCageNum:
                    uncontained.append((i,j))
                    continue

                cage = self.killerSudoku.cages[cageNum]
                for cageSum, cells in cage.items():
                    boxes = set((row // 3, col // 3) for row, col in cells)
                    if len(boxes) == 1:
                        total -= cageSum
                        contained.add(cageNum)
                    else:
                        if uncontainedCageNum != -1:
                            return None
                        uncontained.append((i,j))
                        uncontainedCageNum = cageNum

        return uncontained

    def reduceDomains(self, inCagecells, cageNum, remainingSum, domain):
        cage = self.killerSudoku.cages[cageNum]
        notInCageCells = []
        nonSelectedSum = 0
        for cageSum, cells in cage.items():
            nonSelectedSum = cageSum - remainingSum
            for cell in cells:
                if cell not in inCagecells:
                    notInCageCells.append(cell)

        kdomain = KillerSudokuDomain(self.killerSudoku)
        inSelectedOptions = kdomain.getOptions(len(inCagecells), remainingSum)
        notSelectedOptions = kdomain.getOptions(len(notInCageCells), nonSelectedSum)

        for i in range(inCagecells):
            domain[i[0]][i[1]] = inSelectedOptions - domain[i[0]][i[1]]

        for i in range(notInCageCells):
            domain[i[0]][i[1]] = notSelectedOptions - domain[i[0]][i[1]]

        return domain


        