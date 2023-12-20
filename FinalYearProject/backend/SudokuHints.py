from backend.domain import Domain

class SudokuHints:
    '''
    This class applies different techniques within Sudoku to find the answer 
    to a cell.  
    '''

    def __init__(self, grid):
        '''
        Constructor for the class. 

        Paramaters:
        grid - a 2D array containing the puzzle. 
        '''
        self.grid = grid

        # converts the puzzle into the correct form.
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == '-':
                    self.grid[i][j] = 0
                else:
                    self.grid[i][j] = int(self.grid[i][j])

        domain = Domain(self.grid)
        self.domains = domain.getAllDomains()
    

    def checkObviousSingle(self):
        '''
        Checks every cell in the puzzle to find any cell which qualifies for the 
        obvious single

        Returns:
        A tuple containing the technique used, the row, column and the actually number.
        '''
        for i in range(9):
            for j in range(9):
                if len(self.domains[i][j]) == 1:
                    return ("Obvious single", i, j, next(iter(self.domains[i][j])))
        return None
    

    def checkObviousPairs(self):
        for i in range(0, 9):
            row = self.checkPairsInRow(i)
            if row is not None:
                return row
            col = self.checkPairsInColumn(i)
            if col is not None:
                return col
            box = self.checkPairsInBox(i//3, i%3)
            if box is not None:
                return box
        return None
            

    def checkPairsInBox(self, row, col):
        singleCells = []

        for i in range(row*3, row*3 + 3):
            for j in range(col*3, col*3 + 3):
                if self.domains[i][j] != -1 and len(self.domains[i][j]) == 2:
                    if self.domains[i][j] in singleCells:
                        cells = []
                        for a in range(row*3, row*3 + 3):
                            for b in range(col*3, col*3 + 3):
                                if self.domains[a][b] != -1 and self.domains[a][b] != self.domains[i][j]:
                                    self.domains[a][b] = self.domains[a][b] - self.domains[i][j]
                                if self.domains[a][b] != -1 and self.domains[a][b] == self.domains[i][j]:
                                    cells.append((a,b))
                        return ("Obvious Pairs in box", cells, self.domains[i][j])
                    else:
                        singleCells.append(self.domains[i][j])

        return None
    
    def checkPairsInRow(self, row):
        singleCells = []

        for i in range(9):
            if self.domains[row][i] != -1 and len(self.domains[row][i]) == 2:
                if self.domains[row][i] in singleCells:
                    cells = []
                    for j in range(9):
                        if self.domains[row][j] != -1 and self.domains[row][j] != self.domains[row][i]:
                            self.domains[row][j] = self.domains[row][j] - self.domains[row][i]
                        if self.domains[row][j] != -1 and self.domains[row][j] == self.domains[row][i]:
                            cells.append((row,j))
                    return ("Obvious Pairs in row", cells, self.domains[row][i])
                else:
                    singleCells.append(self.domains[row][i])
        return None



    def checkPairsInColumn(self, col):
        singleCells = []

        for i in range(9):
            if self.domains[i][col] != -1 and len(self.domains[i][col]) == 2:
                if self.domains[i][col] in singleCells:
                    cells = []
                    for j in range(9):
                        if self.domains[j][col] != -1 and self.domains[j][col] != self.domains[i][col]:
                            self.domains[j][col] = self.domains[j][col] - self.domains[i][col]
                        if self.domains[j][col] != -1 and self.domains[j][col] == self.domains[i][col]:
                            cells.append((j,col))
                    return ("Obvious Pairs in column", cells, self.domains[i][col])
                else:
                    singleCells.append(self.domains[i][col])
        
        return None


    def checkHiddenSingles(self):

        for i in range(0, 9):
            row = self.hiddenSingleRow(i)
            if row is not None:
                return row
            col = self.hiddenSingleColumn(i)
            if col is not None:
                return col
            box = self.hiddenSingleBox(i//3, i%3)
            if box is not None:
                return box
        return None

    def hiddenSingleRow(self, row):
        for num in range(1, 10):
            occurrence = 0
            at = -1
            for i in range(0, 9):
                if self.domains[row][i] != -1 and num in self.domains[row][i]:
                    occurrence += 1
                    at = (row, i)
                    if occurrence > 1:
                        break
            if occurrence == 1:
                return ("Hidden single in row", at, num)
            
        return None
    
    def hiddenSingleColumn(self, column):
        for num in range(1, 10):
            occurrence = 0
            at = -1
            for i in range(0, 9):
                if self.domains[i][column] != -1 and num in self.domains[i][column]:
                    occurrence += 1
                    at = (i, column)
                    if occurrence > 1:
                        break
            if occurrence == 1:
                return ("Hidden single in column", at, num)
            
        return None


    def hiddenSingleBox(self, row, column):
        for num in range(1, 10):
            occurrence = 0
            at = -1
            for i in range(row*3, (row*3)+3):
                for j in range(column*3, (column*3)+3):
                    if self.domains[i][j] != -1 and num in self.domains[i][j]:
                        at = (i, j)
                        occurrence += 1
            if occurrence == 1:
                return ("Hidden single in box", at, num)
            
        return None



                



        