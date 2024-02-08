from backend.SudokuSolver import SudokuSolver
from backend.Sudoku import Sudoku
import unittest  

class Test_Sudoku(unittest.TestCase):

    grid = [[0,9,0,8,0,0,0,6,0],
            [6,0,7,0,2,0,1,0,0],
            [0,3,0,0,0,7,0,0,0],
            [8,0,4,0,0,9,0,1,0],
            [0,0,0,5,0,0,2,0,0],
            [0,6,0,0,0,0,0,0,0],
            [0,0,0,0,9,0,0,0,4],
            [0,0,3,0,0,0,0,0,0],
            [7,0,1,0,0,4,0,8,0]]
    
    answer = [[4,9,2,8,1,5,7,6,3],
              [6,5,7,4,2,3,1,9,8],
              [1,3,8,9,6,7,4,5,2],
              [8,7,4,2,3,9,6,1,5],
              [3,1,9,5,8,6,2,4,7],
              [2,6,5,7,4,1,8,3,9],
              [5,8,6,1,9,2,3,7,4],
              [9,4,3,6,7,8,5,2,1],
              [7,2,1,3,5,4,9,8,6]]

    # testing the class is instantiated properly
    def test_Constructor(self):
        solver = SudokuSolver(Sudoku(self.grid))
        self.assertEqual(solver.sudoku.grid, self.grid)


    # testing that the correct answer is returned for a puzzle
    def test_validGridSolver(self):
        solver = SudokuSolver(Sudoku(self.grid))
        self.assertEqual(solver.solver(), self.answer)


    # testing that an invalid grid returns false
    def test_invalidGridSolver(self):
        solver = SudokuSolver(Sudoku([[1,0,1,0,0,1,0,0,1],
                                      [1,0,1,5,9,8,1,1,6],
                                      [1,1,0,0,1,0,0,0,4],
                                      [0,0,2,4,0,0,4,9,4],
                                      [1,4,2,2,4,5,4,6,4],
                                      [1,2,0,0,4,4,4,2,4],
                                      [6,2,0,0,3,4,4,4,4],
                                      [0,5,0,2,0,0,0,3,2],
                                      [0,7,0,2,0,0,0,8,0]]))
        self.assertEqual(solver.solver(), False)


    # testing the pq contains all the empty cells.
    def test_setupHeap(self):
        solver = SudokuSolver(Sudoku([[0,9,0,8,0,0,0,6,0],
                                        [6,0,7,0,2,0,1,0,0],
                                        [0,3,0,0,0,7,0,0,0],
                                        [8,0,4,0,0,9,0,1,0],
                                        [0,0,0,5,0,0,2,0,0],
                                        [0,6,0,0,0,0,0,0,0],
                                        [0,0,0,0,9,0,0,0,4],
                                        [0,0,3,0,0,0,0,0,0],
                                        [7,0,1,0,0,4,0,8,0]]))
        # reseting pq from previous tests.
        solver.heap.pq = []
        solver.setupHeap()
        self.assertEqual(len(solver.heap.pq), 58)

    # testing that SolutionFinder returns one for unique puzzles.
    def test_numSolutions(self):
        solver = SudokuSolver(Sudoku([[0,9,0,8,0,0,0,6,0],
                                        [6,0,7,0,2,0,1,0,0],
                                        [0,3,0,0,0,7,0,0,0],
                                        [8,0,4,0,0,9,0,1,0],
                                        [0,0,0,5,0,0,2,0,0],
                                        [0,6,0,0,0,0,0,0,0],
                                        [0,0,0,0,9,0,0,0,4],
                                        [0,0,3,0,0,0,0,0,0],
                                        [7,0,1,0,0,4,0,8,0]]))
        solver.heap.pq = []
        solver.setupHeap()
        self.assertEqual(solver.SolutionFinder(), 1)

    # testing that SolutionFinder does not returns one for non unique puzzles.
    def test_validNumSolutions(self):
        solver = SudokuSolver(Sudoku([[9,2,6,5,7,1,4,8,3],
                                       [3,5,1,4,8,6,2,7,9],
                                       [8,7,4,9,2,3,5,1,6],
                                       [5,8,2,3,6,7,1,9,4],
                                       [1,4,9,2,5,8,3,6,7],
                                       [7,6,3,1,0,0,8,2,5],
                                       [2,3,8,7,0,0,6,5,1],
                                       [6,1,7,8,3,5,9,4,2],
                                       [4,9,5,6,1,2,7,3,8]]))
        solver.heap.pq = []
        solver.setupHeap()
        self.assertEqual(solver.SolutionFinder(), 2)