from backend.SudokuTechniques.SudokuHints import SudokuHints
from backend.SudokuTechniques.ObviousSinglePairTriple import ObviousSinglePairTriple
import unittest  

class Test_ObviousSinglePairTriple(unittest.TestCase):

    grid1 = [["-","9","2","-","-","5","7","6","-"],
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

    grid4 =[["-","7","-","4","-","8","-","2","9"],
            ["-","-","2","-","-","-","-","-","4"],
            ["8","5","4","-","2","-","-","-","7"],
            ["-","-","8","3","7","4","2","-","-"],
            ["-","2","-","-","-","-","-","-","-"],
            ["-","-","3","2","6","1","7","-","-"],
            ["-","-","-","-","9","3","6","1","2"],
            ["2","-","-","-","-","-","4","-","3"],
            ["1","3","-","6","4","2","-","7","-"]]
    
    grid5 =[["2","9","4","5","1","3","-","-","6"],
            ["6","-","-","8","4","2","3","1","9"],
            ["3","-","-","6","9","7","2","5","4"],
            ["-","-","-","-","5","6","-","-","-"],
            ["-","4","-","-","8","-","-","6","-"],
            ["-","-","-","4","7","-","-","-","-"],
            ["7","3","-","1","6","4","-","-","5"],
            ["9","-","-","7","3","5","-","-","1"],
            ["4","-","-","9","2","8","6","3","7"]]
    
    grid6 = [["3","7","-","-","-","-","-","9","-"],
            ["9","-","-","-","7","-","-","-","-"],
            ["-","-","-","4","2","-","-","-","6"],
            ["-","-","1","-","8","4","2","-","-"],
            ["-","-","-","-","-","-","-","-","-"],
            ["8","-","-","6","-","-","-","5","-"],
            ["-","-","6","-","-","2","-","1","-"],
            ["-","-","-","-","-","-","-","3","9"],
            ["-","5","-","-","-","-","4","-","-"]]
    
    
    
    def test_checkObviousSingle(self):
        sudoku = SudokuHints(self.grid1)
        obviousS = ObviousSinglePairTriple()
        ret = obviousS.checkObviousSingle(sudoku.domains)
        self.assertEqual(ret[2], "4 is an obvious single in cell (0, 0)")
        self.assertEqual(ret[1], (0, 0, 4))

    def test_nocheckObviousSingle(self):
        sudoku = SudokuHints(self.grid2)
        obviousS = ObviousSinglePairTriple()
        self.assertEqual(obviousS.checkObviousSingle(sudoku.domains)[0], None)

    # testing the domain is reduce correctly.
    def test_reduceDomain(self):
        sudoku = SudokuHints(self.grid2)
        obviousS = ObviousSinglePairTriple()
        domain = obviousS.reduceDomain(0,0,1,sudoku.domains)
        count = 0
        for i in range(9):
            if domain[0][i] != -1 and 1 in domain[0][i]:
                count += 1
            if domain[i][0] != -1 and 1 in domain[i][0]:
                count += 1

        for i in range(0, 3):
            for j in range(0, 3):
                if domain[i][j] and 1 in domain[i][j]:
                    count += 1
        self.assertEqual(count, 0)


    def test_checkObviousPairsBox(self):
        sudoku = SudokuHints(self.grid3)
        obviousS = ObviousSinglePairTriple()
        self.assertEqual(obviousS.checkPairsInBox(0, 1, sudoku.domains)[0], "{9, 7} are obvious pairs box (0, 1) in cells ((1, 3), (2, 5))")

    def test_checkObviousPairsBoxDomain(self):
        sudoku = SudokuHints(self.grid3)
        obviousS = ObviousSinglePairTriple()
        a = obviousS.checkPairsInBox(0, 1, sudoku.domains)[1]
        box2 = [{6},-1,-1,{7,9},-1,{4},-1,-1,{7,9}]
        abox2 = [a[0][3],a[0][4],a[0][5],a[1][3],a[1][4],a[1][5],a[2][3],a[2][4],a[2][5]]
        self.assertEqual(abox2,box2)

    def test_checkObviousPairsRow(self):
        sudoku = SudokuHints(self.grid3)
        obviousS = ObviousSinglePairTriple()
        self.assertEqual(obviousS.checkPairsInRow(7, sudoku.domains)[0], "{9, 7} are obvious pairs row 7 in cells ((7, 4), (7, 7))")

    def test_checkObviousPairsRowDomain(self):
        sudoku = SudokuHints(self.grid3)
        obviousS = ObviousSinglePairTriple()
        a = obviousS.checkPairsInRow(7, sudoku.domains)[1]
        row2 = [-1,-1,{1,3,6},-1,{7,9},{3},{1},{7,9},-1]
        arow2 = [a[7][0],a[7][1],a[7][2],a[7][3],a[7][4],a[7][5],a[7][6],a[7][7],a[7][8]]
        self.assertEqual(arow2, row2)

    def test_checkObviousPairsColumn(self):
        sudoku = SudokuHints(self.grid3)
        obviousS = ObviousSinglePairTriple()
        self.assertEqual(obviousS.checkPairsInColumn(7, sudoku.domains)[0], "{9, 7} are obvious pairs column 7 in cells ((0, 7), (7, 7))")

    def test_checkObviousPairsColumnDomain(self):
        sudoku = SudokuHints(self.grid3)
        obviousS = ObviousSinglePairTriple()
        a = obviousS.checkPairsInColumn(7, sudoku.domains)[1]
        col = [{7,9},-1,-1,-1,-1,{4,8},{2,4},{7,9},{2,4}]
        acol2 = [a[0][7],a[1][7],a[2][7],a[3][7],a[4][7],a[5][7],a[6][7],a[7][7],a[8][7]]
        self.assertEqual(acol2, col)

    def test_checkObviousTriplesRow(self):
        sudoku = SudokuHints(self.grid4)
        obviousS = ObviousSinglePairTriple()
        self.assertEqual(obviousS.checkTriplesInRow(4, sudoku.domains)[0], "{5, 8, 9} are obvious triples in row 4 in cells [(4, 3), (4, 4), (4, 5)]")

    def test_checkObviousTriplesRowDomain(self):
        sudoku = SudokuHints(self.grid6)
        obviousS = ObviousSinglePairTriple()
        a = obviousS.checkTriplesInRow(2, sudoku.domains)[1]
        row = [{1,5},{1,8},{5,8},-1,-1,{3,9},{3,7},{7},-1]
        arow2 = [a[2][0],a[2][1],a[2][2],a[2][3],a[2][4],a[2][5],a[2][6],a[2][7],a[2][8]]
        self.assertEqual(arow2,row)

    def test_checkObviousTriplesColumn(self):
        sudoku = SudokuHints(self.grid5)
        obviousS = ObviousSinglePairTriple()
        self.assertEqual(obviousS.checkTriplesInColumn(0, sudoku.domains)[0], "{1, 5, 8} are obvious triples in column 0 in cells [(3, 0), (4, 0), (5, 0)]")

    def test_checkObviousTriplesColumnDomain(self):
        sudoku = SudokuHints(self.grid5)
        obviousS = ObviousSinglePairTriple()
        a = obviousS.checkTriplesInColumn(0, sudoku.domains)[1]
        col = [-1,-1,-1,{1,8},{1,5},{1,5,8},-1,-1,-1]
        acol2 = [a[0][0],a[1][0],a[2][0],a[3][0],a[4][0],a[5][0],a[6][0],a[7][0],a[8][0]]
        self.assertEqual(acol2,col)

    def test_checkObviousTriplesBox(self):
        sudoku = SudokuHints(self.grid6)
        obviousS = ObviousSinglePairTriple()
        self.assertEqual(obviousS.checkTriplesInBox(0,0, sudoku.domains)[0], "{1, 5, 8} are obvious triples in box (0, 0) in cells [(2, 0), (2, 1), (2, 2)]")

    def test_checkObviousTriplesBoxDomain(self):
        sudoku = SudokuHints(self.grid6)
        obviousS = ObviousSinglePairTriple()
        a = obviousS.checkTriplesInBox(0,0, sudoku.domains)[1]
        box = [-1,-1,{2,4},-1,{2,4,6},{2,4},{1,5},{1,8},{5,8}]
        abox2 = [a[0][0],a[0][1],a[0][2],a[1][0],a[1][1],a[1][2],a[2][0],a[2][1],a[2][2]]
        self.assertEqual(abox2,box)
