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
    

    def checkObviousTriples(self):
        for i in range(0, 9):
            row = self.checkTriplesInRow(i)
            if row is not None:
                return row
            col = self.checkTriplesInColumn(i)
            if col is not None:
                return col
            box = self.checkTriplesInBox(i//3, i%3)
            if box is not None:
                return box
        return None

    def checkTriplesInRow(self, row):
        for i in range(9):
            triples = []
            ints = set()
            for j in range(i, 9):
                if self.domains[row][j] != -1 and len(self.domains[row][j]) <= 3:
                    if len(ints.union(self.domains[row][j])) <= 3:
                        triples.append((row,j))
                        ints = ints.union(self.domains[row][j])
            if len(triples) == 3:
                return ("obvious triples in row", triples, ints)

        return None
    
    
    def checkTriplesInColumn(self, col):
        for i in range(9):
            triples = []
            ints = set()
            for j in range(i, 9):
                if self.domains[j][col] != -1 and len(self.domains[j][col]) <= 3:
                    if len(ints.union(self.domains[j][col])) <= 3:
                        triples.append((j, col))
                        ints = ints.union(self.domains[j][col])
            if len(triples) == 3:
                return ("obvious triples in column", triples, ints)

        return None
    

    def checkTriplesInBox(self, row, col):    
        for i in range(row*3, (row*3)+3):
            for j in range(col*3, (col*3)+3):
                triples = []
                ints = set()
                for a in range(row*3, (row*3)+3):
                    for b in range(col*3, (col*3)+3):
                        if self.domains[a][b] != -1 and len(self.domains[a][b]) <= 3:
                            if len(ints.union(self.domains[a][b])) <= 3:
                                triples.append((a, b))
                                ints = ints.union(self.domains[a][b])
                if len(triples) == 3:
                    return ("obvious triples in box", triples, ints)
                
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
    

    def checkHiddenPair(self):

        for i in range(0, 9):
            row = self.hiddenPairColumn(i)
            if row is not None:
                return row
            col = self.hiddenPairColumn(i)
            if col is not None:
                return col
            box = self.hiddenPairColumn(i//3, i%3)
            if box is not None:
                return box
        return None
    

    def hiddenPairRow(self, row):
        double = {}
        for num in range(1, 10):
            at = []
            for i in range(0, 9):
                if self.domains[row][i] != -1 and num in self.domains[row][i]:
                    at.append((row, i))
            if len(at) == 2:
                if tuple(at) in double:
                    for a in at:
                        self.domains[a[0]][a[1]] = {double[tuple(at)], num}
                    return ("hidden pair in row", at, double[tuple(at)], num)
                else: 
                    double[tuple(at)] = num
        return None


    def hiddenPairColumn(self, col):
        double = {}
        for num in range(1, 10):
            at = []
            for i in range(0, 9):
                if self.domains[i][col] != -1 and num in self.domains[i][col]:
                    at.append((i, col))
            if len(at) == 2:
                if tuple(at) in double:
                    for a in at:
                        self.domains[a[0]][a[1]] = {double[tuple(at)], num}
                    return ("hidden pair in column", at, double[tuple(at)], num)
                else: 
                    double[tuple(at)] = num
        return None


    def hiddenPairBox(self, row, col):
        double = {}
        for num in range(1, 10):
            at = []
            for i in range(row*3, (row*3)+3):
                for j in range(col*3, (col*3)+3):
                    if self.domains[i][j] != -1 and num in self.domains[i][j]:
                        at.append((i, j))          
            if len(at) == 2:
                if tuple(at) in double:
                    for a in at:
                        self.domains[a[0]][a[1]] = {double[tuple(at)], num}
                    return ("hidden pair in box", at, double[tuple(at)], num)
                else: 
                    double[tuple(at)] = num
        return None
    

    def checkHiddenTriple(self):

        for i in range(0, 9):
            row = self.hiddenTripleRow(i)
            if row is not None:
                return row
            col = self.hiddenTripleColumn(i)
            if col is not None:
                return col
            box = self.hiddenTripleBox(i//3, i%3)
            if box is not None:
                return box
        return None


    def hiddenTripleRow(self, row):
        triplesCells = []
        tripleNums = []
        for num in range(1, 10):
            at = []
            for j in range(9):
                if self.domains[row][j] != -1 and num in self.domains[row][j]: 
                    at.append((row, j))
            if len(at) <= 3 and len(at) != 0:
              if len(at) <= 3 and len(at) != 0:
                if len(triplesCells) != 0:
                    change = False
                    for i in range(len(triplesCells)):
                        if triplesCells[i].issubset(set(at)) or set(at).issubset(triplesCells[i]):
                            triplesCells[i] = triplesCells[i].union(set(at))
                            tripleNums[i] = tripleNums[i].union(set([num]))
                            change = True
                            
                    if change == False:
                        triplesCells.append(set(at))
                        tripleNums.append(set([num]))
                else:
                    triplesCells.append(set(at))
                    tripleNums.append(set([num]))

        return self.find_triples(triplesCells, tripleNums, "row")


    def hiddenTripleColumn(self, col):
        triplesCells = []
        tripleNums = []
        for num in range(1, 10):
            at = []
            for j in range(9):
                if self.domains[j][col] != -1 and num in self.domains[j][col]: 
                    at.append((j, col))
            if len(at) <= 3 and len(at) != 0:
                if len(triplesCells) != 0:
                    change = False
                    for i in range(len(triplesCells)):
                        if triplesCells[i].issubset(set(at)) or set(at).issubset(triplesCells[i]):
                            triplesCells[i] = triplesCells[i].union(set(at))
                            tripleNums[i] = tripleNums[i].union(set([num]))
                            change = True
                            
                    if change == False:
                        triplesCells.append(set(at))
                        tripleNums.append(set([num]))
                else:
                    triplesCells.append(set(at))
                    tripleNums.append(set([num]))

        return self.find_triples(triplesCells, tripleNums, "column")
    

    def hiddenTripleBox(self, row, col):
        triplesCells = []
        tripleNums = []
        for num in range(1, 10):
            at = []
            for i in range(row*3, (row*3)+3):
                for j in range(col*3, (col*3)+3):
                    if self.domains[i][j] != -1 and num in self.domains[i][j]: 
                        at.append((i, j))
            if len(at) <= 3 and len(at) != 0:
                if len(triplesCells) != 0:
                    change = False
                    for i in range(len(triplesCells)):
                        if triplesCells[i].issubset(set(at)) or set(at).issubset(triplesCells[i]):
                            triplesCells[i] = triplesCells[i].union(set(at))
                            tripleNums[i] = tripleNums[i].union(set([num]))
                            change = True
                            
                    if change == False:
                        triplesCells.append(set(at))
                        tripleNums.append(set([num]))
                else:
                    triplesCells.append(set(at))
                    tripleNums.append(set([num]))

        return self.find_triples(triplesCells, tripleNums, "box")
    

    def find_triples(self, triplesCells, tripleNums, unit):
        for a in range(len(triplesCells)):
            numbers = tripleNums[a]
            for b in range(a+1, len(triplesCells)):
                if triplesCells[a] == triplesCells[b]:
                    numbers = numbers.union(tripleNums[b])
            if len(triplesCells[a]) == 3 and len(numbers) == 3:
                difference = {1,2,3,4,5,6,7,8,9} - numbers
                for cell in triplesCells[a]:
                    self.domains[cell[0]][cell[1]] = self.domains[cell[0]][cell[1]] - difference
                reponse = "hidden triple in " + unit
                return (reponse, triplesCells[a], numbers)
        
        return None
    

    def checkPointingCells(self):
        for i in range(0, 9):
            row = self.pointingCellsRow(i//3, i%3)
            if row is not None:
                return row
            col = self.pointingCellsColumn(i//3, i%3)
            if col is not None:
                return col
        return None

    def pointingCellsRow(self, row, col):
        for num in range(1, 10):
            occur = []
            for i in range(row*3, (row*3)+3):
                for j in range(col*3, (col*3)+3):
                    if self.domains[i][j] != -1 and num in self.domains[i][j]:
                        occur.append(i)
            
            if len(set(occur)) == 1: 
                for i in range(9):
                    if self.domains[occur[0]][i] != -1 and i > col*3 and i < (col*3) + 3:
                        self.domains[occur[0]][i] = self.domains[occur[0]][i].remove(num)
                return ("pointing cells in row", set(occur), num)

        return None


    def pointingCellsColumn(self, row, col):
        for num in range(1, 10):
            occur = []
            for i in range(row*3, (row*3)+3):
                for j in range(col*3, (col*3)+3):
                    if self.domains[i][j] != -1 and num in self.domains[i][j]:
                        occur.append(j)
            
            if len(set(occur)) == 1: 
                for i in range(9):
                    if self.domains[i][occur[0]] != -1 and i > col*3 and i < (col*3) + 3:
                        self.domains[occur[0]][i] = self.domains[i][occur[0]].remove(num)
                return ("pointing cells in column", set(occur), num)

        return None