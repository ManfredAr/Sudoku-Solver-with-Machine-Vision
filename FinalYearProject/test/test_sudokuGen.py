from backend.SudokuGenerator import SudokuGenerator  
from backend.Sudoku import Sudoku 
from backend.SudokuSolver import SudokuSolver
import unittest  

class Test_Sudoku(unittest.TestCase):

    # testing that the grid is valid.
    def test_PartiallyFilled(self):
        gen = SudokuGenerator()
        gen.filledGrid()
        sudoku = Sudoku(gen.grid)
        self.assertEqual(sudoku.isValid(), True)

    # testing that easy puzzles are unique.
    def test_easyPuzzle(self):
        gen = SudokuGenerator()
        puzzle = gen.generate("easy")[0]
        solver = SudokuSolver(Sudoku(puzzle))
        self.assertEqual(solver.SolutionFinder(), 1)

    # testing that medium puzzles are unique.
    def test_mediumPuzzle(self):
        gen = SudokuGenerator()
        puzzle = gen.generate("medium")[0]
        solver = SudokuSolver(Sudoku(puzzle))
        self.assertEqual(solver.SolutionFinder(), 1)

    # testing that hard puzzles are unique.
    def test_hardPuzzle(self):
        gen = SudokuGenerator()
        puzzle = gen.generate("hard")[0]
        solver = SudokuSolver(Sudoku(puzzle))
        self.assertEqual(solver.SolutionFinder(), 1)

    # testing that expert puzzles are unique.
    def test_expertPuzzle(self):
        gen = SudokuGenerator()
        puzzle = gen.generate("expert")[0]
        solver = SudokuSolver(Sudoku(puzzle))
        self.assertEqual(solver.SolutionFinder(), 1)