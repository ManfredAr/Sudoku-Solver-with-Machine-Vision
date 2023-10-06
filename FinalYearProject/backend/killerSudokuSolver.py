class KillerSudokuSolver:

    def __init__(self, killerSudoku):
        self.KSudoku = killerSudoku


    def getNextEmptyCell(self):
        for i in range(9):
            for j in range(9):
                if self.KSudoku.grid[i][j] == 0:
                    return i, j
        
        return None, None