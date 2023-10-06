from backend.KillerSudoku import KillerSudoku
from backend.killerSudokuSolver import KillerSudokuSolver
import unittest

class Test_KSudokuSolver(unittest.TestCase):

    grid = [[0,8,0,1,3,0,0,4,0],
            [0,0,0,5,9,8,0,1,6],
            [0,1,2,0,0,0,0,5,0],
            [0,0,0,4,0,7,0,9,0],
            [0,4,0,0,0,5,0,6,0],
            [0,0,0,0,0,0,0,2,0],
            [6,0,0,0,0,0,0,0,0],
            [1,5,0,0,0,0,6,0,2],
            [0,7,0,0,0,0,0,8,9]]
    
    cages = {frozenset([(0,0)]) : 5,
            frozenset([(0,1), (1,1)]) : 11,
            frozenset([(0,4), (0,5), (1,4), (1,5)]) : 22,
            frozenset([(0,6), (0,7), (0,8), (1,7), (1,8)]) : 27,
            frozenset([(0,2), (0,3)]) : 7,

            frozenset([(1,0), (2,0), (2,1)]) : 14,
            frozenset([(1,2), (2,2), (3,2)]) : 14,
            frozenset([(1,6)]) : 2, 
            frozenset([(1,3), (2,3)]) : 12,

            frozenset([(2,6)]) : 8,
            frozenset([(2,7), (2,8), (3,8)]) : 9,
            frozenset([(2,4), (2,4)]) : 10,

            frozenset([(3,0), (4,0)]) : 10,
            frozenset([(3,1), (4,1), (4,1), (5,2)]) : 22,
            frozenset([(3,3), (3,4), (3,5)]) : 13,
            frozenset([(3,6), (3,7)]) : 12,

            frozenset([(4,3), (4,4)]) : 10,
            frozenset([(4,5), (5,5)]) : 8, 
            frozenset([(4,6), (5,6)]) : 11,
            frozenset([(4,7), (5,7), (5,8), (6,7), (6,8)]) : 20,
            frozenset([(4,8)]) : 8,

            frozenset([(5,0)]) : 7,
            frozenset([(5,2), (6,2)]) : 10,
            frozenset([(5,3), (6,3)]) : 14,
            frozenset([(5,4)]) : 8,             
        
            frozenset([(6,0), (7,0), (8,0), (8,1)]) : 17,
            frozenset([(6,1)]) : 2,
            frozenset([(6,4), (4,1), (4,1), (5,1)]) : 22,
            frozenset([(6,5), (6,6), (7,5)]) : 15,
            
            frozenset([(6,2), (7,1)]) : 13,
            frozenset([(7,3), (8,2), (8,3)]) : 9,
            frozenset([(7,6), (7,7)]) : 13,
            frozenset([(7,8), (8,6), (8,7), (8,8)]) : 20
            }
    
    # testing that the constructor stores the killer sudoku object properly
    def test_Constructor(self):
        solver = KillerSudokuSolver(KillerSudoku(self.grid, self.cages))
        self.assertEqual(solver.KSudoku.grid, self.grid)
        self.assertEqual(solver.KSudoku.cages, self.cages)


    # testing that the next empty cell is returned correctly
    def test_GetNextCell(self):
        solver = KillerSudokuSolver(KillerSudoku(self.grid, self.cages))
        self.assertEqual(solver.getNextEmptyCell(), (0, 0))

    
    # testing that if theres no next empty cell then None, None is returned.
    def test_GetNoNextCell(self):
        # test grid
        test = [[1,2,3,4,5,6,7,8,9], 
         [9,8,7,6,5,4,3,2,1],
         [1,2,3,4,5,6,7,8,9], 
         [9,8,7,6,5,4,3,2,1],
         [1,2,3,4,5,6,7,8,9], 
         [9,8,7,6,5,4,3,2,1],
         [1,2,3,4,5,6,7,8,9], 
         [9,8,7,6,5,4,3,2,1],
         [1,2,3,4,5,6,7,8,9]]
        solver = KillerSudokuSolver(KillerSudoku(test, self.cages))
        self.assertEqual(solver.getNextEmptyCell(), (None, None))