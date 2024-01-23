from backend.KSudokuDomain import KillerSudokuDomain
from backend import KillerSudoku
from backend.SudokuTechniques.SudokuHints import SudokuHints
from backend.SudokuTechniques.PointingCells import PointingCells
import unittest  

class test_PointingCells(unittest.TestCase):

    grid1 =[["-","-","9","-","7","-","-","-","-"],
            ["-","8","-","4","-","-","-","-","-"],
            ["-","-","3","-","-","-","-","2","8"],
            ["1","-","-","-","-","-","6","7","-"],
            ["-","2","-","-","1","3","-","4","-"],
            ["-","4","-","-","-","7","8","-","-"],
            ["6","-","-","-","3","-","-","-","-"],
            ["-","1","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","2","8","4"]]
    
    grid2 = [["9","3","-","-","5","-","-","-","-"],
            ["-","-","-","6","3","-","-","9","5"],
            ["8","5","6","-","-","2","-","-","-"],
            ["-","-","3","1","8","-","5","7","-"],
            ["-","-","5","-","2","-","9","8","-"],
            ["-","8","-","-","-","5","-","-","-"],
            ["-","-","-","8","-","-","1","5","9"],
            ["5","-","8","2","1","-","-","-","4"],
            ["-","-","-","5","6","-","-","-","8"]]

    
    grid7 =[["2","-","8","-","-","-","-","-","6"],
            ["6","-","4","-","2","-","-","-","9"],
            ["3","7","9","-","-","-","-","-","-"],
            ["7","8","-","-","-","-","-","-","-"],
            ["-","2","-","-","-","-","9","-","-"],
            ["-","9","-","-","-","-","-","-","7"],
            ["1","4","7","5","-","-","-","9","8"],
            ["9","3","5","-","-","-","-","7","4"],
            ["8","6","2","4","-","-","-","-","3"]]

    cage = {0: {20: [[3, 1], [3, 2], [4, 2], [5, 2], [5, 3]]}, 
             1: {23: [[2, 4], [3, 4], [4, 4], [5, 4]]}, 
             2: {23: [[0, 3], [0, 4], [1, 2], [1, 3]]}, 
             3: {12: [[4, 0], [4, 1], [5, 0], [6, 0]]}, 
             4: {16: [[7, 2], [7, 3], [7, 4], [7, 5]]}, 
             5: {18: [[4, 5], [4, 6], [4, 7]]}, 
             6: {12: [[5, 5], [5, 6], [5, 7]]}, 
             7: {23: [[7, 0], [8, 0], [8, 1]]}, 
             8: {22: [[2, 5], [2, 6], [3, 5]]}, 
             9: {14: [[2, 3], [3, 3], [4, 3]]}, 
             10: {12: [[0, 5], [0, 6], [0, 7]]}, 
             11: {16: [[1, 5], [1, 6], [1, 7]]}, 
             12: {8: [[0, 0], [1, 0]]}, 
             13: {6: [[0, 1], [1, 1]]}, 
             14: {8: [[0, 2]]}, 
             15: {15: [[0, 8], [1, 8]]}, 
             16: {2: [[1, 4]]}, 
             17: {10: [[2, 0], [2, 1]]}, 
             18: {9: [[2, 2]]}, 
             19: {6: [[2, 7], [2, 8]]}, 
             20: {7: [[3, 0]]}, 
             21: {6: [[3, 6], [3, 7]]}, 
             22: {6: [[3, 8], [4, 8]]}, 
             23: {13: [[5, 1], [6, 1]]}, 
             24: {15: [[5, 8], [6, 8]]}, 
             25: {12: [[6, 2], [6, 3]]}, 
             26: {9: [[6, 4], [6, 5]]}, 
             27: {8: [[6, 6], [7, 6]]}, 
             28: {16: [[6, 7], [7, 7]]}, 
             29: {3: [[7, 1]]}, 
             30: {7: [[7, 8], [8, 8]]}, 
             31: {6: [[8, 2], [8, 3]]}, 
             32: {16: [[8, 4], [8, 5]]}, 
             33: {6: [[8, 6], [8, 7]]}}
    
    def test_checkPointingCellsRows(self):
        sudoku = SudokuHints(self.grid1)
        pointing = PointingCells()
        self.assertEqual(pointing.pointingCellsRow(2,2,sudoku.domains)[0], "1 is a pointing cell in row [6]")

    def test_checkPointingCellsRowsDomains(self):
        sudoku = SudokuHints(self.grid1)
        pointing = PointingCells()
        row2 = [-1, {5,7,9}, {2,4,5,7,8}, {2,5,7,8,9}, -1, {2,4,5,8,9}, {1,5,7,9}, {1,5,9}, {1,5,7,9}]
        self.assertEqual(pointing.pointingCellsRow(2,2,sudoku.domains)[1][6], row2)

    def test_checkPointingCellsColumn(self):
        sudoku = SudokuHints(self.grid2)
        pointing = PointingCells()
        self.assertEqual(pointing.pointingCellsColumn(2,1,sudoku.domains)[0], "3 is a pointing cell in column [5]")

    def test_checkPointingCellsColumnDomain(self):
        sudoku = SudokuHints(self.grid2)
        pointing = PointingCells()
        col5 = [{8, 1, 4, 7}, {8, 1, 4, 7}, -1, {9, 4, 6}, {4, 6, 7}, -1, {3, 4, 7}, {9, 3, 7}, {9, 3, 4, 7}]
        acol5 = pointing.pointingCellsColumn(2,1,sudoku.domains)[1]
        acol5 = [row[5] for row in acol5]
        self.assertEqual(acol5, col5)
