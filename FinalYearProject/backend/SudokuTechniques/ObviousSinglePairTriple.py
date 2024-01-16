class ObviousSinglePairTriple:
    '''
    This class is the implementation of the obvious singles, pairs and triples
    techniques found in Sudoku. 
    '''

    def checkObviousSingle(self, domain):
        '''
        Checks every cell in the puzzle to find any cell which qualifies for the 
        obvious single

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        for i in range(9):
            for j in range(9):
                if domain[i][j] != -1 and len(domain[i][j]) == 1:
                    value = next(iter(domain[i][j]))
                    print(i, j, value)
                    message = f"{value} is an obvious single in cell {(i, j)}"
                    return self.reduceDomain(i, j, value, domain), (i, j, value), message
        return None, None, None
    

    def reduceDomain(self, row, col, value, domain):
        '''
        Removes the values set from the row, column and box. 

        parameters:
        row, col - the row and column of the cell
        value - the value set to the cell
        domain - the domain of each cell in a 2d array

        returns:
        A new domain which is reduced.
        '''
        for i in range(9):
            if domain[row][i] != -1:
                domain[row][i].discard(value)
            if domain[i][col] != -1:
                domain[i][col].discard(value)

        for i in range(((row//3)*3), ((row//3)*3)+3):
            for j in range(((col//3)*3), ((col//3)*3)+3):
                if domain[i][j] != -1:
                    domain[i][j].discard(value)

        return domain

    
    
    def checkObviousPairs(self, domain):
        '''
        Checks whether the obvious pairs technique can be implemented within the row, column or box
        of the grid.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        for i in range(0, 9):
            row, grid = self.checkPairsInRow(i, domain)
            if row is not None:
                return grid, row
            col, grid = self.checkPairsInColumn(i, domain)
            if col is not None:
                return grid, col
            box, grid = self.checkPairsInBox(i//3, i%3, domain)
            if box is not None:
                return grid, box
        return None, None
            

    def checkPairsInBox(self, row, col, domain):
        '''
        checks if obvious pairs applies in any box

        parameter:
        - the row and column of the box index.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        singleCells = []

        for i in range(row*3, row*3 + 3):
            for j in range(col*3, col*3 + 3):
                if domain[i][j] != -1 and len(domain[i][j]) == 2:
                    if domain[i][j] in singleCells:
                        cells = []
                        for a in range(row*3, row*3 + 3):
                            for b in range(col*3, col*3 + 3):
                                if domain[a][b] != -1 and domain[a][b] != domain[i][j]:
                                    domain[a][b] = domain[a][b] - domain[i][j]
                                if domain[a][b] != -1 and domain[a][b] == domain[i][j]:
                                    cells.append((a,b))
                        message = f"{domain[i][j]} are obvious pairs box {row, col} in cells {cells[0], cells[1]}"
                        return message, domain
                    else:
                        singleCells.append(domain[i][j])

        return None, None
    
    
    def checkPairsInRow(self, row, domain):
        '''
        checks if obvious pairs applies in any row

        parameter:
        - row of the grid to check.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        singleCells = []

        for i in range(9):
            if domain[row][i] != -1 and len(domain[row][i]) == 2:
                if domain[row][i] in singleCells:
                    cells = []
                    for j in range(9):
                        if domain[row][j] != -1 and domain[row][j] != domain[row][i]:
                            domain[row][j] = domain[row][j] - domain[row][i]
                        if domain[row][j] != -1 and domain[row][j] == domain[row][i]:
                            cells.append((row,j))
                    message = f"{domain[row][i]} are obvious pairs row {row} in cells {cells[0], cells[1]}"
                    return message, domain
                else:
                    singleCells.append(domain[row][i])
        return None, None



    def checkPairsInColumn(self, col, domain):
        '''
        checks if obvious pairs applies in any column

        parameter:
        - column of the grid to check.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        singleCells = []

        for i in range(9):
            if domain[i][col] != -1 and len(domain[i][col]) == 2:
                if domain[i][col] in singleCells:
                    cells = []
                    for j in range(9):
                        if domain[j][col] != -1 and domain[j][col] != domain[i][col]:
                            domain[j][col] = domain[j][col] - domain[i][col]
                        if domain[j][col] != -1 and domain[j][col] == domain[i][col]:
                            cells.append((j,col))
                    message = f"{domain[i][col]} are obvious pairs column {col} in cells {cells[0], cells[1]}"
                    return message, domain
                else:
                    singleCells.append(domain[i][col])
        
        return None, None
    
    def checkObviousTriples(self, domain):
        '''
        Checks whether the obvious triples technique can be implemented within the row, column or box
        of the grid.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        for i in range(0, 9):
            row, grid = self.checkTriplesInRow(i, domain)
            if row is not None:
                return grid, row
            col, grid = self.checkTriplesInColumn(i, domain)
            if col is not None:
                return grid, col
            box, grid = self.checkTriplesInBox(i//3, i%3, domain)
            if box is not None:
                return grid, box
        return None, None
    

    def checkTriplesInRow(self, row, domain):
        '''
        checks if obvious triples applies in any row

        parameter:
        - row of the grid to check.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        for i in range(9):
            triples = []
            ints = set()
            for j in range(i, 9):
                if domain[row][j] != -1 and len(domain[row][j]) <= 3:
                    if len(ints.union(domain[row][j])) <= 3:
                        triples.append((row,j))
                        ints = ints.union(domain[row][j])
            if len(triples) == 3:
                for a in range(i, 9):
                    if domain[row][a] != -1 and (row,a) not in triples:
                        domain[row][a] = domain[row][a] - ints
                message = f"{ints} are obvious triples in row {row} in cells {triples}"
                return message, domain

        return None, None
    
    
    def checkTriplesInColumn(self, col, domain):
        '''
        checks if obvious triples applies in any column

        parameter:
        - column of the grid to check.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        for i in range(9):
            triples = []
            ints = set()
            for j in range(i, 9):
                if domain[j][col] != -1 and len(domain[j][col]) <= 3:
                    if len(ints.union(domain[j][col])) <= 3:
                        triples.append((j, col))
                        ints = ints.union(domain[j][col])
            if len(triples) == 3:
                for a in range(i, 9):
                    if domain[a][col] != -1 and (a,col) not in triples:
                        domain[a][col] = domain[a][col] - ints
                message = f"{ints} are obvious triples in column {col} in cells {triples}"
                return message, domain

        return None, None
    

    def checkTriplesInBox(self, row, col, domain):    
        '''
        checks if obvious triples applies in any box

        parameter:
        - the row and column of the box index.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        for i in range(row*3, (row*3)+3):
            for j in range(col*3, (col*3)+3):
                triples = []
                ints = set()
                for a in range(row*3, (row*3)+3):
                    for b in range(col*3, (col*3)+3):
                        if domain[a][b] != -1 and len(domain[a][b]) <= 3:
                            if len(ints.union(domain[a][b])) <= 3:
                                triples.append((a, b))
                                ints = ints.union(domain[a][b])
                if len(triples) == 3:
                    for c in range(row*3, (row*3)+3):
                        for d in range(col*3, (col*3)+3):
                            if domain[c][d] != -1 and (c,d) not in triples:
                                domain[c][d] = domain[c][d] - ints
                    message = f"{ints} are obvious triples in box {row, col} in cells {triples}"
                    return message, domain
                
        return None, None