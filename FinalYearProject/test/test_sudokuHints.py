from backend.SudokuHints import SudokuHints
import unittest  

class Test_Domain(unittest.TestCase):

    grid = [["-","9","2","-","-","5","7","6","-"],
            ["6","-","7","4","-","3","1","-","-"],
            ["1","3","8","-","6","7","4","-","2"],
            ["-","7","-","2","3","-","6","1","5"],
            ["-","1","-","5","-","6","2","4","7"],
            ["2","6","5","-","4","-","8","3","9"],
            ["5","-","-","1","9","2","-","7","4"],
            ["9","-","3","-","7","-","5","2","1"],
            ["7","-","1","-","-","4","9","-","6"]]

    grid2 = [["-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-"]]
    
    grid3 =[["-","-","2","-","8","5","-","-","4"],
            ["-","-","-","-","3","-","-","6","-"],
            ["-","-","4","2","1","-","-","3","-"],
            ["-","-","-","-","-","-","-","5","2"],
            ["-","-","-","-","-","-","3","1","-"],
            ["9","-","-","-","-","-","-","-","-"],
            ["8","-","-","-","-","6","-","-","-"],
            ["2","5","-","4","-","-","-","-","8"],
            ["-","-","-","-","-","1","6","-","-"]]
    
    grid4 =[["-","-","9","-","3","2","-","-","-"],
            ["-","-","-","7","-","-","-","-","-"],
            ["1","6","2","-","-","-","-","-","-"],
            ["-","1","-","-","2","-","5","6","-"],
            ["-","-","-","9","-","-","-","-","-"],
            ["-","5","-","-","-","-","1","-","7"],
            ["-","-","-","-","-","-","4","-","3"],
            ["-","2","6","-","-","9","-","-","-"],
            ["-","-","5","8","7","-","-","-","-"]]
    
    grid5 =[["-","-","2","-","8","5","-","-","4"],
            ["-","-","-","-","3","-","-","6","-"],
            ["-","-","4","2","1","-","-","3","-"],
            ["-","-","-","-","-","-","-","5","2"],
            ["-","-","-","-","-","-","3","1","-"],
            ["9","-","-","-","-","-","-","-","-"],
            ["8","-","-","-","-","6","-","-","-"],
            ["2","5","-","4","-","-","-","-","8"],
            ["-","-","-","-","-","1","6","-","-"]]
    
    
    def test_constructor(self):
        sudoku = SudokuHints(self.grid)
        self.assertEqual(sudoku.grid, [[0,9,2,0,0,5,7,6,0],
                                       [6,0,7,4,0,3,1,0,0],
                                       [1,3,8,0,6,7,4,0,2],
                                       [0,7,0,2,3,0,6,1,5],
                                       [0,1,0,5,0,6,2,4,7],
                                       [2,6,5,0,4,0,8,3,9],
                                       [5,0,0,1,9,2,0,7,4],
                                       [9,0,3,0,7,0,5,2,1],
                                       [7,0,1,0,0,4,9,0,6]])

    
    def test_checkObviousSingle(self):
        sudoku = SudokuHints(self.grid)
        self.assertEqual(sudoku.checkObviousSingle(), ("Obvious single", 0, 0, 4))

    def test_nocheckObviousSingle(self):
        sudoku = SudokuHints(self.grid2)
        self.assertEqual(sudoku.checkObviousSingle(), None)


    def test_checkHiddenSinglesColumn(self):
        sudoku = SudokuHints(self.grid4)
        self.assertEqual(sudoku.hiddenSingleColumn(2), ("Hidden single in column", (6, 2), 1))

    def test_checkHiddenSinglesBox(self):
        sudoku = SudokuHints(self.grid4)
        self.assertEqual(sudoku.hiddenSingleBox(2, 0), ("Hidden single in box", (6, 2), 1))

    def test_checkHiddenSinglesRow(self):
        sudoku = SudokuHints(self.grid3)
        self.assertEqual(sudoku.hiddenSingleRow(1), ("Hidden single in row", (1, 6), 2))

    def test_checkObviousPairsBox(self):
        sudoku = SudokuHints(self.grid5)
        self.assertEqual(sudoku.checkPairsInBox(0, 1), ("Obvious Pairs in box", [(1,3), (2,5)], {9,7}))

    def test_checkObviousPairsRow(self):
        sudoku = SudokuHints(self.grid5)
        self.assertEqual(sudoku.checkPairsInRow(7), ("Obvious Pairs in row", [(7,4), (7,7)], {7,9}))

    def test_checkObviousPairsColumn(self):
        sudoku = SudokuHints(self.grid5)
        self.assertEqual(sudoku.checkPairsInColumn(7), ("Obvious Pairs in column", [(0,7), (7,7)], {7,9}))