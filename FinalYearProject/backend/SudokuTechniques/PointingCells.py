class PointingCells:
    '''
    This class is the implementation of the pointing pairs and triples
    techniques found in Sudoku. 
    '''

    def checkPointingCells(self, domain):
        '''
        Checks whether the pointing cells technique can be applies in a row or column.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        for i in range(0, 9):
            row, grid = self.pointingCellsRow(i//3, i%3, domain)
            if row is not None:
                return grid, row
            col, grid = self.pointingCellsColumn(i//3, i%3, domain)
            if col is not None:
                return grid, col
        return None, None

    def pointingCellsRow(self, row, col, domain):
        '''
        checks if pointing cells technique applies in any box.

        parameter:
        - the row and column of the box index.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        for num in range(1, 10):
            occur = []
            for i in range(row*3, (row*3)+3):
                for j in range(col*3, (col*3)+3):
                    if domain[i][j] != -1 and num in domain[i][j]:
                        occur.append(i)
            
            if len(set(occur)) == 1: 
                for i in range(9):
                    if domain[occur[0]][i] != -1 and not (i >= col*3 and i <= (col*3) + 3):
                        domain[occur[0]][i].discard(num)
                return ("pointing cells in row", set(occur), num), domain

        return None, None


    def pointingCellsColumn(self, row, col, domain):
        '''
        checks if pointing cells technique applies in any box.

        parameter:
        - the row and column of the box index.

        Returns:
        A tuple containing the technique used, the row, column and the actual number.
        '''
        for num in range(1, 10):
            occur = []
            for i in range(row*3, (row*3)+3):
                for j in range(col*3, (col*3)+3):
                    if domain[i][j] != -1 and num in domain[i][j]:
                        occur.append(j)
            
            if len(set(occur)) == 1: 
                for i in range(9):
                    if domain[occur[0]][i] != -1 and not (i >= row*3 and i <= (row*3) + 3):
                        domain[occur[0]][i].discard(num)
                return ("pointing cells in column", set(occur), num), domain

        return None, None