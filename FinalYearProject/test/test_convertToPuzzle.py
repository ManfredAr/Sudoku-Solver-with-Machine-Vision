from backend.convertToPuzzle import convertToPuzzle
import unittest   # The test framework


class Test_convertToPuzzle(unittest.TestCase):

    testSudoku = [["4","-","-","8","1","5","-","6","3"],
                ["6","-","7","4","2","3","1","9","8"],
                ["1","3","8","-","6","-","-","5","2"],
                ["8","7","4","2","-","9","-","1","5"],
                ["3","-","-","5","8","-","2","4","7"],
                ["2","6","5","7","4","1","8","-","9"],
                ["5","-","6","-","9","2","-","7","4"],
                ["9","-","3","6","7","-","5","2","1"],
                ["7","2","-","3","5","4","-","-","6"]]
    
    incorrectSudoku = [["4","4","-","8","1","5","-","6","3"],
                ["6","-","7","4","2","3","1","9","8"],
                ["1","3","8","-","6","-","-","5","2"],
                ["8","7","4","2","-","9","-","1","5"],
                ["3","-","-","5","8","-","2","4","7"],
                ["2","6","5","7","4","1","8","-","9"],
                ["5","-","6","-","9","2","-","7","4"],
                ["9","-","3","6","7","-","5","2","1"],
                ["7","2","-","3","5","4","-","-","6"]]
    
    answer = [[4,9,2,8,1,5,7,6,3],
              [6,5,7,4,2,3,1,9,8],
              [1,3,8,9,6,7,4,5,2],
              [8,7,4,2,3,9,6,1,5],
              [3,1,9,5,8,6,2,4,7],
              [2,6,5,7,4,1,8,3,9],
              [5,8,6,1,9,2,3,7,4],
              [9,4,3,6,7,8,5,2,1],
              [7,2,1,3,5,4,9,8,6]]
    
    testKSudoku = [["-","-","-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-","-","-"]]
    
    testCages = {
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

    KsudokuAns = [[5, 8, 6, 1, 3, 2, 9, 4, 7],
                [4, 3, 7, 5, 9, 8, 2, 1, 6],
                [9, 1, 2, 7, 6, 4, 8, 5, 3],
                [8, 6, 5, 4, 2, 7, 3, 9, 1],
                [2, 4, 3, 9, 1, 5, 7, 6, 8],
                [7, 9, 1, 6, 8, 3, 4, 2, 5],
                [6, 2, 9, 8, 7, 1, 5, 3, 4],
                [1, 5, 8, 3, 4, 9, 6, 7, 2],
                [3, 7, 4, 2, 5, 6, 1, 8, 9]]


    # testing the constructor is setup up correctly for sudoku
    def test_sudokuConstructor(self):
        converter = convertToPuzzle(self.testSudoku, None)
        self.assertEqual(converter.puzzle, self.testSudoku)
        self.assertEqual(converter.prevCages, None)


    # testing the constructor is setup up correctly for killer sudoku
    def test_KsudokuConstructor(self):
        converter = convertToPuzzle(self.testKSudoku, self.testCages)
        self.assertEqual(converter.puzzle, self.testKSudoku)
        self.assertEqual(converter.prevCages, self.testCages)

    
    # testing that the solution is returned for sudoku.
    def test_sudokuValid(self):
        converter = convertToPuzzle(self.testSudoku, None)
        puzzle, solution = converter.validateSudoku()
        self.assertEqual(solution, self.answer)

    # testing that the solution is returned for killer sudoku.
    def test_KsudokuValid(self):
        converter = convertToPuzzle(self.testKSudoku, self.testCages)
        puzzle, cages, solution = converter.validateKSudoku()
        self.assertEqual(solution, self.KsudokuAns)

    # testing that false returned if there is no solution for sudoku.
    def test_sudokuinValid(self):
        converter = convertToPuzzle(self.incorrectSudoku, None)
        puzzle, solution = converter.validateSudoku()
        self.assertEqual(solution, False)

    # testing that false returned if there is no solution for killer sudoku.
    def test_KsudokuinValid(self):
        converter = convertToPuzzle(self.testKSudoku, {})
        puzzle, cages, solution = converter.validateKSudoku()
        self.assertEqual(solution, False)
