from backend.KillerSudoku import KillerSudoku
import unittest

class Test_KillerSudoku(unittest.TestCase):

    grid = [[0,8,0,1,3,0,0,4,0],
            [0,0,0,5,9,8,0,1,6],
            [0,1,2,0,0,0,0,5,0],
            [0,0,0,4,0,7,0,9,0],
            [0,4,0,0,0,5,0,6,0],
            [0,0,0,0,0,0,0,2,0],
            [6,0,0,0,0,0,0,0,0],
            [1,5,0,0,0,0,6,0,2],
            [0,7,0,0,0,0,0,8,9]]
    
    cages = {
        1 : { 5 : [(0,0)] },
        2 : { 11 : [(0,1), (1,1)] },
        3 : { 22 : [(0,4), (0,5), (1,4), (1,5)] },
        4 : { 27 : [(0,6), (0,7), (0,8), (1,7), (1,8)] },
        5 : { 7 : [(0,2), (0,3)] },

        6 : { 14 : [(1,0), (2,0), (2,1)] },
        7 : { 14 : [(1,2), (2,2), (3,2)] },
        8 : { 2 : [(1,6)] } ,
        9 : { 12 : [(1,3), (2,3)] },

        10 : { 8 : [(2,6)] },
        11 : { 9 : [(2,7), (2,8), (3,8)] },
        12 : { 10 : [(2,4), (2,5)] },

        13 : { 10 : [(3,0), (4,0)] },
        14 : { 22 : [(3,1), (4,1), (4,2), (5,1)] },
        15 : { 13 : [(3,3), (3,4), (3,5)] },
        16 : { 12 : [(3,6), (3,7)] },

        17 : { 10 : [(4,3), (4,4)] },
        18 : { 8 : [(4,5), (5,5)] },
        19 : { 11 : [(4,6), (5,6)] },
        20 : { 20 : [(4,7), (5,7), (5,8), (6,7), (6,8)] },
        21 : { 8 : [(4,8)] },

        22 : { 7 : [(5,0)] },
        23 : { 10 : [(5,2), (6,2)] },
        24 : { 14 : [(5,3), (6,3)] },
        25 : { 8 : [(5,4)] },             
    
        26 : { 17 : [(6,0), (7,0), (8,0), (8,1)] },
        27 : { 2 : [(6,1)] },
        28 : { 22 : [(6,4), (7,4), (8,4), (8,5)] },
        29 : { 15 : [(6,5), (6,6), (7,5)] },
        
        30 : { 13 : [(7,1), (7,2)] },
        31 : { 9 : [(7,3), (8,2), (8,3)] },
        32 : { 13 : [(7,6), (7,7)] },
        33 : { 20 : [(7,8), (8,6), (8,7), (8,8)] },
}


    # testing the class is instantiated properly
    def test_Constructor(self):
        sudoku = KillerSudoku(self.grid, self.cages)
        self.assertEqual(sudoku.grid, self.grid)
        self.assertEqual(sudoku.cages, self.cages)

    # testing the getters methods return correctly
    def test_Getter(self):
        sudoku = KillerSudoku(self.grid, self.cages)
        self.assertEqual(sudoku.getGrid(), self.grid)
        self.assertEqual(sudoku.getCages(), self.cages) 

    # testing false is returned if cages do not equal 405 sum 
    def test_incorrectSum(self):
        self.grid[0][0] = 8
        sudoku = KillerSudoku(self.grid, {})
        self.assertEqual(sudoku.checkSum(), False)

    # testing true is returns is sum is correct
    def test_Sum(self):
        self.grid[0][0] = 8
        sudoku = KillerSudoku(self.grid, self.cages)
        self.assertEqual(sudoku.checkSum(), True)
    
    # testing false is returned if row, column or box contains duplicated
    def test_inValidGrid(self):
        self.grid[0][0] = 8
        sudoku = KillerSudoku(self.grid, self.cages)
        self.assertEqual(sudoku.checkValid(), False)


    # testing true is returned when no duplicates occur
    def test_ValidGrid(self):
        self.grid[0][0] = 0
        sudoku = KillerSudoku(self.grid, self.cages)
        self.assertEqual(sudoku.checkValid(), True)


    # testing the cell to cage dictionary is correct
    def test_cellCages(self):
        sudoku = KillerSudoku(self.grid, self.cages)
        self.assertEqual(len(sudoku.cellCage), 81)


    # testing related cells returns all cells related to a particular cell
    def test_RelatedCells(self):
        sudoku = KillerSudoku(self.grid, self.cages)
        self.assertEqual(len(sudoku.getRelatedCells(0, 0)), 21)

    # testing cageCells returns all the cells in a givens cells cage
    def test_cageCells(self):
        sudoku = KillerSudoku(self.grid, self.cages)
        self.assertEqual(sudoku.getCageCells(0, 1), [(0, 1), (1, 1)])

    # testing cageSum returns the sum of a cage the cell is in
    def test_cageSum(self):
        sudoku = KillerSudoku(self.grid, self.cages)
        self.assertEqual(sudoku.getCageSum(0, 1), 11)