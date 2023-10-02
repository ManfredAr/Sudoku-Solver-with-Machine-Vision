from backend.Sudoku import Sudoku    # The code to test
import unittest   # The test framework

class Test_Sudoku(unittest.TestCase):
    # testing the class is instantiated properly
    def test_Constructor(self):
        sudoku = Sudoku([1,2,3,4])
        self.assertEqual(sudoku.grid, [1,2,3,4])

    def test_checkRow(self):
        sudoku = Sudoku([[1,0,0,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9]])
        self.assertEqual(sudoku.checkRow(0), True)

    def test_checkIncorrectRow(self):
        sudoku = Sudoku([[1,2,3,4,4,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9]])
        self.assertEqual(sudoku.checkRow(0), False)

    def test_checkIncorrectCol(self):
        sudoku = Sudoku([[1,2,3,4,4,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9],
                        [1,2,3,4,5,6,7,8,9]])
        self.assertEqual(sudoku.checkCol(0), False)

    def test_checkCol(self):
        sudoku = Sudoku([[1,2,3,4,4,6,7,8,9],
                        [2,2,3,4,5,6,7,8,9],
                        [3,2,3,4,5,6,7,8,9],
                        [4,2,3,4,5,6,7,8,9],
                        [0,2,3,4,5,6,7,8,9],
                        [0,2,3,4,5,6,7,8,9],
                        [7,2,3,4,5,6,7,8,9],
                        [8,2,3,4,5,6,7,8,9],
                        [9,2,3,4,5,6,7,8,9]])
        self.assertEqual(sudoku.checkCol(0), True)

    def test_checkIncorrectBox(self):
        sudoku = Sudoku([[1,2,3,4,4,6,7,8,9],
                        [2,2,3,4,5,6,7,8,9],
                        [3,2,3,4,5,6,7,8,9],
                        [4,2,3,4,5,6,7,8,9],
                        [5,2,3,4,5,6,7,8,9],
                        [6,2,3,4,5,6,7,8,9],
                        [7,2,3,4,5,6,7,8,9],
                        [8,2,3,4,5,6,7,8,9],
                        [9,2,3,4,5,6,7,8,9]])
        self.assertEqual(sudoku.checkBox(0,0), False)

    def test_checkBox(self):
        sudoku = Sudoku([[1,0,3,4,4,6,7,8,9],
                        [4,0,6,4,5,6,7,8,9],
                        [7,8,9,4,5,6,7,8,9],
                        [4,2,3,4,5,6,7,8,9],
                        [5,2,3,4,5,6,7,8,9],
                        [6,2,3,4,5,6,7,8,9],
                        [7,2,3,4,5,6,7,8,9],
                        [8,2,3,4,5,6,7,8,9],
                        [9,2,3,4,5,6,7,8,9]])
        self.assertEqual(sudoku.checkBox(0,0), True)

    def test_checkIncorrectGrid(self):
        sudoku = Sudoku([[1,2,3,4,4,6,7,8,9],
                        [4,5,6,4,5,6,7,8,9],
                        [7,8,9,4,5,6,7,8,9],
                        [4,2,3,4,5,6,7,8,9],
                        [5,2,3,4,5,6,7,8,9],
                        [6,2,3,4,5,6,7,8,9],
                        [7,2,3,4,5,6,7,8,9],
                        [8,2,3,4,5,6,7,8,9],
                        [9,2,3,4,5,6,7,8,9]])
        self.assertEqual(sudoku.isValid(), False)

    def test_checkGrid(self):
        sudoku = Sudoku([[0,0,0,0,0,0,0,0,1],
                         [0,0,0,0,0,0,0,1,0],
                         [0,0,0,0,0,0,1,0,0],
                         [0,0,0,0,0,2,0,0,0],
                         [0,0,0,0,2,0,0,0,0],
                         [0,0,0,3,0,0,0,0,0],
                         [0,0,4,0,0,0,0,0,0],
                         [0,5,0,0,0,0,0,0,0],
                         [6,0,0,0,0,0,0,0,0]])
        self.assertEqual(sudoku.isValid(), True)


if __name__ == '__main__':
    unittest.main()