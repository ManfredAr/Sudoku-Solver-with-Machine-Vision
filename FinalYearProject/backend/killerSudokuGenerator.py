from backend.SudokuGenerator import SudokuGenerator
from backend.killerSudokuSolver3 import KillerSudokuSolver3
from backend.KillerSudoku import KillerSudoku
import random
import copy

class killerSudokuGenerator:

    def __init__(self):
        self.easy = {"3" : [5,6,7], "4" : [1,2,3], "5" : [0]}
        self.medium = {"3" : [8,9], "4" : [2,3,4], "5" : [0]}
        self.hard = {"3" : [6,7,8], "4" : [4,5], "5" : [1,2]}
        self.expert = {"3" : [4,5], "4" : [3,4,5], "5" : [3,4]}
        self.cages = {}
        self.sudokuGen = SudokuGenerator()
        self.sudokuGen.filledGrid()
        self.originalGrid = self.sudokuGen.grid
        self.grid = copy.deepcopy(self.sudokuGen.grid)
        self.count = 0
        self.difficulty = None

    def generate(self, difficulty):
        while True:
            if difficulty == "easy":
                self.difficulty = "easy"
                self.generateCages(self.easy)
            elif difficulty == "medium":
                self.difficulty = "medium"
                self.generateCages(self.medium)
            elif difficulty == "hard":
                self.difficulty = "hard"
                self.generateCages(self.hard)
            elif difficulty == "expert":
                self.difficulty = "expert"
                self.generateCages(self.expert)
            else:
                return None, None
            
            grid = [[0 for _ in range(9)] for _ in range(9)]
            kSudoku = KillerSudokuSolver3(KillerSudoku(grid, self.cages))
            if kSudoku.SolutionFinder() != 1:
                self.cages = {}
                self.grid = copy.deepcopy(self.sudokuGen.grid)
            else:
                break
        
        return self.originalGrid, self.cages


    def generateCages(self, difficulty):
        cells = [(i, j) for i in range(9) for j in range(9)]  

        three = random.choice(difficulty["3"])
        four = random.choice(difficulty["4"])
        five = random.choice(difficulty["5"])
        appearance = [five, four, three]

        for i in range(len(appearance)):
            if appearance[i] != 0:
                count = 0
                while appearance[i] != 0:
                    if count > 10:
                        break
                    x, y = random.choice(cells)
                    cage = self.findConnectCells(5-i, (x,y), [])
                    if cage != -1 and len(cage) == 5-i:
                        cells = self.addCage(list(cage), cells)
                    else:
                        count += 1
                        continue
                    appearance[i] = appearance[i] - 1
        
        self.fillRemainingCells(cells)



    def fillRemainingCells(self, cells):
        '''
        fills the remaining cells into sizes of 1 or 2.

        parameters:
        cells - the cells not already in cages. 
        '''
        while len(cells) != 0:
            if self.difficulty == "expert":
                triple = self.findConnectCells(3, cells[0], [])
                if triple != -1 and len(triple) == 3:
                    cells = self.addCage(triple, cells)
            pairs = self.findConnectCells(2, cells[0], [])
            if pairs != -1 and len(pairs) == 2:
                cells = self.addCage(pairs, cells)
            else:
                cells = self.addCage([cells[0]], cells)
            


    def addCage(self, cells, allCells):
        '''
        Givens a list of cells it sets up a cage for those cells with the cage sum.

        parameters:
        cells - an array of cells
        '''
        count = 0
        for i in cells:
            count += self.grid[i[0]][i[1]]
            self.grid[i[0]][i[1]] = -1
            allCells.remove((i[0], i[1]))

        cells = sorted(cells, key=lambda point: (point[0], point[1]))
        self.cages[self.count] = {count : cells}
        self.count += 1

        return allCells
    

    def findConnectCells(self, num, cell, visited):
        '''
        Tries to find cells to form a cage of specific lengths

        parameters:
        num - the lwngth of the cage
        cell - the starting cell
        visited - an empty array

        returns:
        a set of cells or -1
        '''
        if num == 0:
            return set()
        
        if cell[0] < 0 or cell[0] > 8 or cell [1] < 0 or cell[1] > 8 or self.grid[cell[0]][cell[1]] == -1 or self.grid[cell[0]][cell[1]] in visited:
            return -1
        
        current_cells = set([cell])
        visited.append(self.grid[cell[0]][cell[1]])
        nextCell = random.choice([0, 1, 2, 3])
        
        response = None
        for i in range(4):
            if nextCell == 0:
                response =  self.findConnectCells(num-1, (cell[0]+1, cell[1]), visited)
            if nextCell == 1:
                response = self.findConnectCells(num-1, (cell[0], cell[1]+1), visited)
            if nextCell == 2:
                response = self.findConnectCells(num-1, (cell[0]-1, cell[1]), visited)
            if nextCell == 3:
                response = self.findConnectCells(num-1, (cell[0], cell[1]-1), visited)

            if response == -1:
                nextCell = (nextCell + 1) % 4
            elif len(response) != num - 1:
                num = num - len(response)
                current_cells = current_cells.union(response)
                nextCell = (nextCell + 1) % 4
            else:
                break

        if response != -1:
            return current_cells.union(response)
        else:
            return current_cells

