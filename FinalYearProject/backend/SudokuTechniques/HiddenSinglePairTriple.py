class HiddenSinglePairTriple:
    '''
    This class is the implementation of the hidden singles, pairs and triples
    techniques found in Sudoku. 
    '''

    def checkHiddenSingles(self, domain):
        '''
        Checks whether the hidden singles technique can be implemented within the row, column or box
        of the grid.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        for i in range(0, 9):
            row, grid = self.hiddenSingleRow(i, domain)
            if row is not None:
                return grid, row
            col, grid = self.hiddenSingleColumn(i, domain)
            if col is not None:
                return grid, col
            box, grid = self.hiddenSingleBox(i//3, i%3, domain)
            if box is not None:
                return grid, box
        return None, None


    def hiddenSingleRow(self, row, domain):
        '''
        checks if hidden single technique applies in any row.

        parameter:
        - row of the grid to check.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        for num in range(1, 10):
            occurrence = 0
            at = -1
            for i in range(0, 9):
                if domain[row][i] != -1 and num in domain[row][i]:
                    occurrence += 1
                    at = (row, i)
                    if occurrence > 1:
                        break
            if occurrence == 1:
                domain[at[0]][at[1]] = set([num])
                message = f"{num} is a hidden single in row {row} in cell {at}"
                return message, domain
            
        return None, None
    
    def hiddenSingleColumn(self, column, domain):
        '''
        checks if hidden singles technique applies in any column.

        parameter:
        - column of the grid to check.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        for num in range(1, 10):
            occurrence = 0
            at = -1
            for i in range(0, 9):
                if domain[i][column] != -1 and num in domain[i][column]:
                    occurrence += 1
                    at = (i, column)
                    if occurrence > 1:
                        break
            if occurrence == 1:
                domain[at[0]][at[1]] = set([num])
                message = f"{num} is a hidden single in column {column} in cell {at}"
                return message, domain
            
        return None, None


    def hiddenSingleBox(self, row, column, domain):
        '''
        checks if hidden single technique applies in any box

        parameter:
        - the row and column of the box index.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        for num in range(1, 10):
            occurrence = 0
            at = -1
            for i in range(row*3, (row*3)+3):
                for j in range(column*3, (column*3)+3):
                    if domain[i][j] != -1 and num in domain[i][j]:
                        at = (i, j)
                        occurrence += 1
            if occurrence == 1:
                domain[at[0]][at[1]] = set([num])
                message = f"{num} is a hidden single in box {(row, column)} in cell {at}"
                return message, domain
            
        return None, None
    

    def checkHiddenPair(self, domain):
        '''
        Checks whether the hidden pairs technique can be implemented within the row, column or box
        of the grid.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        for i in range(0, 9):
            row, grid = self.hiddenPairRow(i, domain)
            if row is not None:
                return grid, row
            col, grid = self.hiddenPairColumn(i, domain)
            if col is not None:
                return grid, col
            box, grid = self.hiddenPairBox(i//3, i%3, domain)
            if box is not None:
                return grid, box
        return None, None
    

    def hiddenPairRow(self, row, domain):
        '''
        checks if hidden pairs technique applies in any row.

        parameter:
        - row of the grid to check.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        double = {}
        for num in range(1, 10):
            at = []
            for i in range(0, 9):
                if domain[row][i] != -1 and num in domain[row][i]:
                    at.append((row, i))
            if len(at) == 2:
                if tuple(at) in double:
                    for a in at:
                        domain[a[0]][a[1]] = {double[tuple(at)], num}
                    message = f"{double[tuple(at)], num} are hidden pairs in row {row} in cells {at[0], at[1]}"
                    return message, domain
                else: 
                    double[tuple(at)] = num
        return None, None


    def hiddenPairColumn(self, col, domain):
        '''
        checks if hidden pairs technique applies in any column

        parameter:
        - column of the grid to check.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        double = {}
        for num in range(1, 10):
            at = []
            for i in range(0, 9):
                if domain[i][col] != -1 and num in domain[i][col]:
                    at.append((i, col))
            if len(at) == 2:
                if tuple(at) in double:
                    for a in at:
                        domain[a[0]][a[1]] = {double[tuple(at)], num}
                    message = f"{double[tuple(at)], num} are hidden pairs in column {col} in cells {at[0], at[1]}"
                    return message, domain
                else: 
                    double[tuple(at)] = num
        return None, None


    def hiddenPairBox(self, row, col, domain):
        '''
        checks if hidden pair technique applies in any box

        parameter:
        - the row and column of the box index.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        double = {}
        for num in range(1, 10):
            at = []
            for i in range(row*3, (row*3)+3):
                for j in range(col*3, (col*3)+3):
                    if domain[i][j] != -1 and num in domain[i][j]:
                        at.append((i, j))          
            if len(at) == 2:
                if tuple(at) in double:
                    for a in at:
                        domain[a[0]][a[1]] = {double[tuple(at)], num}
                    message = f"{double[tuple(at)], num} are hidden pairs in box {(row, col)} in cells {at[0], at[1]}"
                    return message, domain
                else: 
                    double[tuple(at)] = num
        return None, None
    

    def checkHiddenTriple(self, domain):
        '''
        Checks whether the hidden triples technique can be implemented within the row, column or box
        of the grid.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        for i in range(0, 9):
            row, grid = self.hiddenTripleRow(i, domain)
            if row is not None:
                return grid, row
            col, grid = self.hiddenTripleColumn(i, domain)
            if col is not None:
                return grid, col
            box, grid = self.hiddenTripleBox(i//3, i%3, domain)
            if box is not None:
                return grid, box
        return None, None


    def hiddenTripleRow(self, row, domain):
        '''
        checks if hidden triples technique applies in any row.

        parameter:
        - row of the grid to check.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        triplesCells = []
        tripleNums = []
        for num in range(1, 10):
            at = []
            for j in range(9):
                if domain[row][j] != -1 and num in domain[row][j]: 
                    at.append((row, j))
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

        return self.find_triples(triplesCells, tripleNums, "row", domain)


    def hiddenTripleColumn(self, col, domain):
        '''
        checks if hidden triples technique applies in any column.

        parameter:
        - column of the grid to check.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        triplesCells = []
        tripleNums = []
        for num in range(1, 10):
            at = []
            for j in range(9):
                if domain[j][col] != -1 and num in domain[j][col]: 
                    at.append((j, col))
            if len(at) <= 3 and len(at) > 0:
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

        return self.find_triples(triplesCells, tripleNums, "column", domain)
    

    def hiddenTripleBox(self, row, col, domain):
        '''
        checks if hidden triple technique applies in any box.

        parameter:
        - the row and column of the box index.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        triplesCells = []
        tripleNums = []
        for num in range(1, 10):
            at = []
            for i in range(row*3, (row*3)+3):
                for j in range(col*3, (col*3)+3):
                    if domain[i][j] != -1 and num in domain[i][j]: 
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

        return self.find_triples(triplesCells, tripleNums, "box", domain)
    

    def find_triples(self, triplesCells, tripleNums, unit, domain):
        '''
        Checks whether an obious triple existion within a row, column or box.

        parameters:
        triplesCells - an array containing a set of cells which may contain a hidden triple.
        tripleNums - the numbers which only appear in the corresponing groups of cells.
        unit - whether its checking thre "row", "column" or "box".

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        for a in range(len(triplesCells)):
            numbers = tripleNums[a]
            for b in range(a+1, len(triplesCells)):
                if triplesCells[a] == triplesCells[b]:
                    numbers = numbers.union(tripleNums[b])
            if len(triplesCells[a]) == 3 and len(numbers) == 3:
                difference = {1,2,3,4,5,6,7,8,9} - numbers
                for cell in triplesCells[a]:
                    domain[cell[0]][cell[1]] = domain[cell[0]][cell[1]] - difference
                message = f"{numbers} are hidden triples in {unit} in cells {list(triplesCells[a])}"
                return message, domain
        
        return None, None