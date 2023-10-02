class Sudoku:

    def __init__(self, grid):
        self.grid = grid


    def isValid(self):
        for i in range(9):
            if self.checkRow(i) == False or self.checkCol(i) == False or self.checkBox(i//3, i%3) == False:
                return False
        return True
    

    def checkRow(self, row):
        unique_values = {}
        for i in range(9):
            if self.grid[row][i] != 0 and self.grid[row][i] in unique_values:
                return False
            unique_values[self.grid[row][i]] = 1
        return True
    

    def checkCol(self, col):
        unique_values = {}
        for i in range(9):
            if self.grid[i][col] != 0 and self.grid[i][col] in unique_values:
                return False
            unique_values[self.grid[i][col]] = 1
        return True
    

    def checkBox(self, row, col):
        row = row * 3
        col = col * 3
        unique_values = {}
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] != 0 and self.grid[row+i][col+j] in unique_values:
                    return False
                unique_values[self.grid[row+i][col+j]] = 1
        return True