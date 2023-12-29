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

    grid6 =[["-","-","9","-","3","2","-","-","-"],
            ["-","-","-","7","-","-","-","-","-"],
            ["1","6","2","-","-","-","-","-","-"],
            ["-","1","-","-","2","-","5","6","-"],
            ["-","-","-","9","-","-","-","-","-"],
            ["-","5","-","-","-","-","1","-","7"],
            ["-","-","-","-","-","-","4","-","3"],
            ["-","2","6","-","-","9","-","-","-"],
            ["-","-","5","8","7","-","-","-","-"]]
    

    grid7 =[["-","-","8","-","-","7","-","-","-"],
            ["-","4","2","-","-","5","-","-","-"],
            ["-","-","-","-","-","-","-","-","-"],
            ["-","-","3","-","-","6","8","-","1"],
            ["-","-","-","-","-","-","-","-","6"],
            ["9","-","-","-","-","-","-","-","-"],
            ["-","8","-","1","3","-","4","7","-"],
            ["-","-","-","-","9","-","-","-","-"],
            ["-","1","-","-","-","-","-","-","-"]]
    
    grid8 =[["-","7","-","4","-","8","-","2","9"],
            ["-","-","2","-","-","-","-","-","4"],
            ["8","5","4","-","2","-","-","-","7"],
            ["-","-","8","3","7","4","2","-","-"],
            ["-","2","-","-","-","-","-","-","-"],
            ["-","-","3","2","6","1","7","-","-"],
            ["-","-","-","-","9","3","6","1","2"],
            ["2","-","-","-","-","-","4","-","3"],
            ["1","3","-","6","4","2","-","7","-"]]
    
    grid9 =[["2","9","4","5","1","3","-","-","6"],
            ["6","-","-","8","4","2","3","1","9"],
            ["3","-","-","6","9","7","2","5","4"],
            ["-","-","-","-","5","6","-","-","-"],
            ["-","4","-","-","8","-","-","6","-"],
            ["-","-","-","4","7","-","-","-","-"],
            ["7","3","-","1","6","4","-","-","5"],
            ["9","-","-","7","3","5","-","-","1"],
            ["4","-","-","9","2","8","6","3","7"]]
    
    grid10 = [["3","7","-","-","-","-","-","9","-"],
            ["9","-","-","-","7","-","-","-","-"],
            ["-","-","-","4","2","-","-","-","6"],
            ["-","-","1","-","8","4","2","-","-"],
            ["-","-","-","-","-","-","-","-","-"],
            ["8","-","-","6","-","-","-","5","-"],
            ["-","-","6","-","-","2","-","1","-"],
            ["-","-","-","-","-","-","-","3","9"],
            ["-","5","-","-","-","-","4","-","-"]]

    grid11=[["-","-","-","-","-","1","-","3","-"],
            ["2","3","1","-","9","-","-","-","-"],
            ["-","6","5","-","-","3","1","-","-"],
            ["6","7","8","9","2","4","3","-","-"],
            ["1","-","3","-","5","-","-","-","6"],
            ["-","-","-","1","3","6","7","-","-"],
            ["-","-","9","3","6","-","5","7","-"],
            ["-","-","6","-","1","9","8","4","3"],
            ["3","-","-","-","-","-","-","-","-"]]

    grid12=[["5","-","-","6","2","-","-","3","7"],
            ["-","-","4","8","9","-","-","-","-"],
            ["-","-","-","-","5","-","-","-","-"],
            ["9","3","-","-","-","-","-","-","-"],
            ["-","2","-","-","-","-","6","-","5"],
            ["7","-","-","-","-","-","-","-","3"],
            ["-","-","-","-","-","9","-","-","-"],
            ["-","-","-","-","-","-","7","-","-"],
            ["6","8","-","5","7","-","-","-","2"]]
    
    grid13=[["2","8","-","-","-","-","4","7","3"],
            ["5","3","4","8","2","7","1","9","6"],
            ["-","7","1","-","3","4","-","8","-"],
            ["3","-","-","5","-","-","-","4","-"],
            ["-","-","-","3","4","-","-","6","-"],
            ["4","6","-","7","9","-","3","1","-"],
            ["-","9","-","2","-","3","6","5","4"],
            ["-","-","3","-","-","9","8","2","1"],
            ["-","-","-","-","8","-","9","3","7"]]
    
    grid14=[["9","3","-","-","5","-","-","-","-"],
            ["-","-","-","6","3","-","-","9","5"],
            ["8","5","6","-","-","2","-","-","-"],
            ["-","-","3","1","8","-","5","7","-"],
            ["-","-","5","-","2","-","9","8","-"],
            ["-","8","-","-","-","5","-","-","-"],
            ["-","-","-","8","-","-","1","5","9"],
            ["5","-","8","2","1","-","-","-","4"],
            ["-","-","-","5","6","-","-","-","8"]]

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

    def test_checkObviousTriplesRow(self):
        sudoku = SudokuHints(self.grid8)
        self.assertEqual(sudoku.checkTriplesInRow(4), ("obvious triples in row", [(4,3), (4,4), (4,5)], {5,8,9}))

    def test_checkObviousTriplesColumn(self):
        sudoku = SudokuHints(self.grid9)
        self.assertEqual(sudoku.checkTriplesInColumn(0), ("obvious triples in column", [(3,0), (4,0), (5,0)], {1,5,8}))

    def test_checkObviousTriplesBox(self):
        sudoku = SudokuHints(self.grid10)
        self.assertEqual(sudoku.checkTriplesInBox(0,0), ("obvious triples in box", [(2,0), (2,1), (2,2)], {1,5,8}))

    def test_checkHiddenPairsBox(self):
        sudoku = SudokuHints(self.grid6)
        self.assertEqual(sudoku.hiddenPairBox(1, 0), ("hidden pair in box", [(4,0), (5,0)], 2, 6))

    def test_checkHiddenPairsRow(self):
        sudoku = SudokuHints(self.grid6)
        self.assertEqual(sudoku.hiddenPairRow(2), ("hidden pair in row", [(2,6), (2,7)], 3, 7))

    def test_checkHiddenPairsColumn(self):
        sudoku = SudokuHints(self.grid6)
        self.assertEqual(sudoku.checkHiddenPair(), ("hidden pair in column", [(4,0), (5,0)], 2, 6))

    def test_checkHiddenTriplesBox(self):
        sudoku = SudokuHints(self.grid13)
        self.assertEqual(sudoku.hiddenTripleBox(2, 0), ("hidden triple in box", {(7,1), (8,1), (8,2)}, {2,4,5}))

    def test_checkHiddenTriplesRow(self):
        sudoku = SudokuHints(self.grid11)
        self.assertEqual(sudoku.hiddenTripleRow(0), ("hidden triple in row", {(0,3), (0,6), (0,8)}, {2,5,6}))

    def test_checkHiddenTriplesColumn(self):
        sudoku = SudokuHints(self.grid12)
        self.assertEqual(sudoku.hiddenTripleColumn(5), ("hidden triple in column", {(5,5), (3,5), (7,5)}, {2,5,6}))

    def test_checkPointingCellsRows(self):
        sudoku = SudokuHints(self.grid13)
        self.assertEqual(sudoku.pointingCellsRow(0,2), ("pointing cells in row", {2}, 2))

    def test_checkPointingCellsColumn(self):
        sudoku = SudokuHints(self.grid14)
        self.assertEqual(sudoku.pointingCellsColumn(2,1), ("pointing cells in column", {5}, 3))
