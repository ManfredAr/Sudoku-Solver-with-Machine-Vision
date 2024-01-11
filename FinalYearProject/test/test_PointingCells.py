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
        col5 = [{8, 1, 4, 7}, {8, 1, 4, 7}, -1, {9, 4, 6}, {3, 4, 6, 7}, -1, {3, 4, 7}, {9, 3, 7}, {9, 3, 4, 7}]
        acol5 = pointing.pointingCellsColumn(2,1,sudoku.domains)[1]
        acol5 = [row[5] for row in acol5]
        self.assertEqual(acol5, col5)

