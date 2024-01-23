from backend.SudokuTechniques.SudokuHints import SudokuHints
from backend.SudokuTechniques.HiddenSinglePairTriple import HiddenSinglePairTriple
import unittest  
from backend.KSudokuDomain import KillerSudokuDomain
from backend.KillerSudoku import KillerSudoku

class test_HiddenSinglePairTriple(unittest.TestCase):

    grid1 =[["-","-","2","-","8","5","-","-","4"],
            ["-","-","-","-","3","-","-","6","-"],
            ["-","-","4","2","1","-","-","3","-"],
            ["-","-","-","-","-","-","-","5","2"],
            ["-","-","-","-","-","-","3","1","-"],
            ["9","-","-","-","-","-","-","-","-"],
            ["8","-","-","-","-","6","-","-","-"],
            ["2","5","-","4","-","-","-","-","8"],
            ["-","-","-","-","-","1","6","-","-"]]
    
    grid2 =[["-","-","9","-","3","2","-","-","-"],
            ["-","-","-","7","-","-","-","-","-"],
            ["1","6","2","-","-","-","-","-","-"],
            ["-","1","-","-","2","-","5","6","-"],
            ["-","-","-","9","-","-","-","-","-"],
            ["-","5","-","-","-","-","1","-","7"],
            ["-","-","-","-","-","-","4","-","3"],
            ["-","2","6","-","-","9","-","-","-"],
            ["-","-","5","8","7","-","-","-","-"]]
    
    grid3 =[["-","-","9","-","3","2","-","-","-"],
            ["-","-","-","7","-","-","-","-","-"],
            ["1","6","2","-","-","-","-","-","-"],
            ["-","1","-","-","2","-","5","6","-"],
            ["-","-","-","9","-","-","-","-","-"],
            ["-","5","-","-","-","-","1","-","7"],
            ["-","-","-","-","-","-","4","-","3"],
            ["-","2","6","-","-","9","-","-","-"],
            ["-","-","5","8","7","-","-","-","-"]]
    
    grid4 = [["-","-","-","-","-","1","-","3","-"],
            ["2","3","1","-","9","-","-","-","-"],
            ["-","6","5","-","-","3","1","-","-"],
            ["6","7","8","9","2","4","3","-","-"],
            ["1","-","3","-","5","-","-","-","6"],
            ["-","-","-","1","3","6","7","-","-"],
            ["-","-","9","3","6","-","5","7","-"],
            ["-","-","6","-","1","9","8","4","3"],
            ["3","-","-","-","-","-","-","-","-"]]

    grid5 = [["5","-","-","6","2","-","-","3","7"],
            ["-","-","4","8","9","-","-","-","-"],
            ["-","-","-","-","5","-","-","-","-"],
            ["9","3","-","-","-","-","-","-","-"],
            ["-","2","-","-","-","-","6","-","5"],
            ["7","-","-","-","-","-","-","-","3"],
            ["-","-","-","-","-","9","-","-","-"],
            ["-","-","-","-","-","-","7","-","-"],
            ["6","8","-","5","7","-","-","-","2"]]
    
    grid6 = [["2","8","-","-","-","-","4","7","3"],
            ["5","3","4","8","2","7","1","9","6"],
            ["-","7","1","-","3","4","-","8","-"],
            ["3","-","-","5","-","-","-","4","-"],
            ["-","-","-","3","4","-","-","6","-"],
            ["4","6","-","7","9","-","3","1","-"],
            ["-","9","-","2","-","3","6","5","4"],
            ["-","-","3","-","-","9","8","2","1"],
            ["-","-","-","-","8","-","9","3","7"]]




    def test_checkHiddenSinglesColumn(self):
        sudoku = SudokuHints(self.grid2)
        hidden = HiddenSinglePairTriple()
        self.assertEqual(hidden.hiddenSingleColumn(2, sudoku.domains)[0], "1 is a hidden single in column 2 in cell (6, 2)")

    def test_checkHiddenSinglesColumnDomain(self):
        sudoku = SudokuHints(self.grid2)
        hidden = HiddenSinglePairTriple()
        a = hidden.hiddenSingleColumn(2, sudoku.domains)[1]
        col = [-1,{3,4,8},-1,{3,4,7,8},{3,4,7,8},{3,4,8},{1},-1,-1]
        acol = [a[0][2],a[1][2],a[2][2],a[3][2],a[4][2],a[5][2],a[6][2],a[7][2],a[8][2]]
        self.assertEqual(col, acol)

    def test_checkHiddenSinglesBox(self):
        sudoku = SudokuHints(self.grid2)
        hidden = HiddenSinglePairTriple()
        self.assertEqual(hidden.hiddenSingleBox(2, 0, sudoku.domains)[0], "1 is a hidden single in box (2, 0) in cell (6, 2)")

    def test_checkHiddenSinglesBoxDomain(self):
        sudoku = SudokuHints(self.grid2)
        hidden = HiddenSinglePairTriple()
        a = hidden.hiddenSingleBox(2, 0, sudoku.domains)[1]
        box = [{7,8,9},{7,8,9},{1},{3,4,7,8},-1,-1,{3,4,9},{3,4,9},-1]
        abox = [a[6][0],a[6][1],a[6][2],a[7][0],a[7][1],a[7][2],a[8][0],a[8][1],a[8][2]]
        self.assertEqual(box, abox)

    def test_checkHiddenSinglesRow(self):
        sudoku = SudokuHints(self.grid1)
        hidden = HiddenSinglePairTriple()
        self.assertEqual(hidden.hiddenSingleRow(1, sudoku.domains)[0], "2 is a hidden single in row 1 in cell (1, 6)")

    def test_checkHiddenSinglesRowDomain(self):
        sudoku = SudokuHints(self.grid1)
        hidden = HiddenSinglePairTriple()
        a = hidden.hiddenSingleRow(1, sudoku.domains)[1]
        box = [{1,5,7},{8,1,9,7},{1,5,7,8,9},{1,5,7,8,9},-1,{9,4,7},{2},-1,{1,5,9,7}]
        abox = [a[1][0],a[1][1],a[1][2],a[1][2],a[1][4],a[1][5],a[1][6],a[1][7],a[1][8]]
        self.assertEqual(box, abox)

    def test_checkHiddenPairsBox(self):
        sudoku = SudokuHints(self.grid3)
        hidden = HiddenSinglePairTriple()
        self.assertEqual(hidden.hiddenPairBox(1, 0, sudoku.domains)[0], "(2, 6) are hidden pairs in box (1, 0) in cells ((4, 0), (5, 0))")

    def test_checkHiddenPairsBoxDomain(self):
        sudoku = SudokuHints(self.grid3)
        hidden = HiddenSinglePairTriple()
        a = hidden.hiddenPairBox(1, 0, sudoku.domains)[1]
        box = [{3,4,7,8,9},-1,{3,4,7,8},{2,6},{3,4,7,8},{3,4,7,8},{2,6},-1,{3,4,8}]
        abox = [a[3][0],a[3][1],a[3][2],a[4][0],a[4][1],a[4][2],a[5][0],a[5][1],a[5][2]]
        self.assertEqual(box, abox)

    def test_checkHiddenPairsRow(self):
        sudoku = SudokuHints(self.grid3)
        hidden = HiddenSinglePairTriple()
        self.assertEqual(hidden.hiddenPairRow(2, sudoku.domains)[0], "(3, 7) are hidden pairs in row 2 in cells ((2, 6), (2, 7))")

    def test_checkHiddenPairsRowDomain(self):
        sudoku = SudokuHints(self.grid3)
        hidden = HiddenSinglePairTriple()
        a = hidden.hiddenPairRow(2, sudoku.domains)[1]
        row = [-1,-1,-1,{4,5},{8,9,4,5},{8,4,5},{3,7},{3,7},{8,9,4,5}]
        arow = [a[2][0],a[2][1],a[2][2],a[2][3],a[2][4],a[2][5],a[2][6],a[2][7],a[2][8]]
        self.assertEqual(row, arow)

    def test_checkHiddenPairsColumn(self):
        sudoku = SudokuHints(self.grid3)
        hidden = HiddenSinglePairTriple()
        self.assertEqual(hidden.hiddenPairColumn(0, sudoku.domains)[0], "(2, 6) are hidden pairs in column 0 in cells ((4, 0), (5, 0))")

    def test_checkHiddenPairsColumnDomain(self):
        sudoku = SudokuHints(self.grid3)
        hidden = HiddenSinglePairTriple()
        a = hidden.hiddenPairColumn(0, sudoku.domains)[1]
        col = [{8,4,5,7},{8,3,4,5},-1,{3,4,7,8,9},{2,6},{2,6},{8,9,7},{8,3,4,7},{9,3,4}]
        acol = [a[0][0],a[1][0],a[2][0],a[3][0],a[4][0],a[5][0],a[6][0],a[7][0],a[8][0]]
        self.assertEqual(col, acol)

    def test_checkHiddenTriplesBox(self):
        sudoku = SudokuHints(self.grid6)
        hidden = HiddenSinglePairTriple()
        self.assertEqual(hidden.hiddenTripleBox(2, 0, sudoku.domains)[0], "{2, 4, 5} are hidden triples in box in cells [(7, 1), (8, 1), (8, 2)]")

    def test_checkHiddenTriplesBoxDomain(self):
        sudoku = SudokuHints(self.grid6)
        hidden = HiddenSinglePairTriple()
        a = hidden.hiddenTripleBox(2, 0, sudoku.domains)[1]
        col = [{1,7,8},-1,{7,8},{6,7},{4,5},-1,{1,6},{2,4,5},{2,5}]
        acol = [a[6][0],a[6][1],a[6][2],a[7][0],a[7][1],a[7][2],a[8][0],a[8][1],a[8][2]]
        self.assertEqual(col, acol)

    def test_checkHiddenTriplesRow(self):
        sudoku = SudokuHints(self.grid4)
        hidden = HiddenSinglePairTriple()
        self.assertEqual(hidden.hiddenTripleRow(0, sudoku.domains)[0], "{2, 5, 6} are hidden triples in row in cells [(0, 8), (0, 3), (0, 6)]")

    def test_checkHiddenTriplesRowDomain(self):
        sudoku = SudokuHints(self.grid4)
        hidden = HiddenSinglePairTriple()
        a = hidden.hiddenTripleRow(0, sudoku.domains)[1]
        row = [{4,7,8,9},{4,8,9},{4,7},{2,5,6},{4,7,8},-1,{2,6},-1,{2,5}]
        arow = [a[0][0],a[0][1],a[0][2],a[0][3],a[0][4],a[0][5],a[0][6],a[0][7],a[0][8]]
        self.assertEqual(row, arow)

    def test_checkHiddenTriplesColumn(self):
        sudoku = SudokuHints(self.grid5)
        hidden = HiddenSinglePairTriple()
        self.assertEqual(hidden.hiddenTripleColumn(5, sudoku.domains)[0], "{2, 5, 6} are hidden triples in column in cells [(5, 5), (7, 5), (3, 5)]")

    def test_checkHiddenTriplesColumnDomain(self):
        sudoku = SudokuHints(self.grid5)
        hidden = HiddenSinglePairTriple()
        a = hidden.hiddenTripleColumn(5, sudoku.domains)[1]
        col = [{1,4},{1,3,7},{1,3,4,7},{2,5,6},{1,3,4,7,8},{2,5,6},-1,{2,6},{1,3,4}]
        acol = [a[0][5],a[1][5],a[2][5],a[3][5],a[4][5],a[5][5],a[6][5],a[7][5],a[8][5]]
        self.assertEqual(col, acol)