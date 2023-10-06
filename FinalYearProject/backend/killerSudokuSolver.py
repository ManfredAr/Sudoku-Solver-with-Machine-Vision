class KillerSudokuSolver:

    def __init__(self, killerSudoku):
        self.KSudoku = killerSudoku


    def getNextEmptyCell(self):
        for i in range(9):
            for j in range(9):
                if self.KSudoku.grid[i][j] == 0:
                    return i, j
        
        return None, None
    
    
    def getDomain(self, row, col):
        used = []
        cageNum = self.KSudoku.cellCage.get((row,col))
        cageSum = next(iter(self.KSudoku.cages.get(cageNum)))

        for i in range(9):
            #get all values in the row
            if self.KSudoku.grid[row][i] > 0:
                used.append(self.KSudoku.grid[row][i])

            # get all values in the column
            if self.KSudoku.grid[i][col] > 0:
                used.append(self.KSudoku.grid[i][col])

        #get all values in the box
        box_row = (row // 3) * 3
        col_box = (col // 3) * 3

        for i in range(box_row, box_row + 3):
            for j in range(col_box, col_box + 3):
                if self.KSudoku.grid[i][j] > 0:
                    used.append(self.KSudoku.grid[i][j])

        # getting all the values in the cage
        cells = next(iter(self.KSudoku.cages.get(cageNum).values()))
        count = 0
        for i in range(0, len(cells)):
            if self.KSudoku.grid[cells[i][0]][cells[i][1]] != 0:
                # updating the remaining cage sum.
                cageSum = cageSum - self.KSudoku.grid[cells[i][0]][cells[i][1]]
                used.append(self.KSudoku.grid[cells[i][0]][cells[i][1]])
                count += 1
        
        # condition to check if this is the last cell to be filled in the cage.
        # the second part makes sure that the remaining sum of the cage hasnt been used yet.
        if count == len(cells) - 1 and cageSum not in used:
            return set([cageSum])

        # getting all unique values
        used = set(used)
        return set([1,2,3,4,5,6,7,8,9]) - used