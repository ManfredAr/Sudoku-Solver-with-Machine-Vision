from backend.KillerSudoku import KillerSudoku
from backend.killerSudokuSolver import KillerSudokuSolver
from backend.killerSudokuSolver2 import KillerSudokuSolver2
import unittest

class Test_KSudokuSolver(unittest.TestCase):

    grid = [[0,8,0,1,3,0,0,4,0],
            [0,0,0,5,9,8,0,1,6],
            [0,1,2,0,0,0,0,5,0],
            [0,0,0,4,0,7,0,9,0],
            [0,4,0,0,0,5,0,6,0],
            [0,0,0,0,0,0,0,2,0],
            [6,0,0,0,7,0,5,0,4],
            [1,5,0,0,0,0,6,0,2],
            [0,7,0,2,0,0,0,8,9]]
    
    cages = {
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
    
    # testing that the constructor stores the killer sudoku object properly
    def test_Constructor(self):
        solver = KillerSudokuSolver2(KillerSudoku(self.grid, self.cages))
        self.assertEqual(solver.KSudoku.grid, self.grid)
        self.assertEqual(solver.KSudoku.cages, self.cages)
        self.assertEqual(len(solver.KSudoku.cellCage), 81)



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

    
    # testing the correct domain is returned
    def test_getDomain(self):
        solver = KillerSudokuSolver2(KillerSudoku([[0,8,0,1,3,0,0,4,0],
                                                [0,0,0,5,9,8,0,1,6],
                                                [0,1,2,0,0,0,0,5,0],
                                                [0,0,0,4,0,7,0,9,0],
                                                [0,4,0,0,0,5,0,6,0],
                                                [0,0,0,0,0,0,0,2,0],
                                                [6,0,0,0,7,0,5,0,4],
                                                [1,5,0,0,0,0,6,0,2],
                                                [0,7,0,2,0,0,0,8,9]], self.cages))
        self.assertEqual(solver.getDomain(3, 0), set([2, 3, 5, 8]))

    
    # testing is a cell is the last cage to be filled or on its own its values becames the cage sum
    def test_getLastDomain(self):
        solver = KillerSudokuSolver2(KillerSudoku([[0,8,0,1,3,0,0,4,0],
                                                [0,0,0,5,9,8,0,1,6],
                                                [0,1,2,0,0,0,0,5,0],
                                                [0,0,0,4,0,7,0,9,0],
                                                [0,4,0,0,0,5,0,6,0],
                                                [0,0,0,0,0,0,0,2,0],
                                                [6,0,0,0,7,0,5,0,4],
                                                [1,5,0,0,0,0,6,0,2],
                                                [0,7,0,2,0,0,0,8,9]], self.cages))
        self.assertEqual(solver.getDomain(1, 1), set([3]))
        

    # testing the pq contains all the empty cells.
    def test_setupHeap(self):
        solver = KillerSudokuSolver2(KillerSudoku([[0,8,0,1,3,0,0,4,0],
                                                    [0,0,0,5,9,8,0,1,6],
                                                    [0,1,2,0,0,0,0,5,0],
                                                    [0,0,0,4,0,7,0,9,0],
                                                    [0,4,0,0,0,5,0,6,0],
                                                    [0,0,0,0,0,0,0,2,0],
                                                    [6,0,0,0,7,0,5,0,4],
                                                    [1,5,0,0,0,0,6,0,2],
                                                    [0,7,0,2,0,0,0,8,9]], self.cages))
        solver.setupHeap()
        self.assertEqual(len(solver.queue.pq), 50)
        

    # testing the killer sudoku grid is solved correctly
    def test_correctSolution(self):
        solver2 = KillerSudokuSolver2(KillerSudoku(self.grid, self.cages))
        self.assertEqual(solver2.solver(), [[5, 8, 6, 1, 3, 2, 9, 4, 7],
                                            [4, 3, 7, 5, 9, 8, 2, 1, 6],
                                            [9, 1, 2, 7, 6, 4, 8, 5, 3],
                                            [8, 6, 5, 4, 2, 7, 3, 9, 1],
                                            [2, 4, 3, 9, 1, 5, 7, 6, 8],
                                            [7, 9, 1, 6, 8, 3, 4, 2, 5],
                                            [6, 2, 9, 8, 7, 1, 5, 3, 4],
                                            [1, 5, 8, 3, 4, 9, 6, 7, 2],
                                            [3, 7, 4, 2, 5, 6, 1, 8, 9]])
        

    # testing that decrease keys returns all the orginal values of te changed keys
    def test_decreaseKeys(self):
        solver = KillerSudokuSolver2(KillerSudoku([[0,8,0,1,3,0,0,4,0],
                                            [0,0,0,5,9,8,0,1,6],
                                            [0,1,2,0,0,0,0,5,0],
                                            [0,0,0,4,0,7,0,9,0],
                                            [0,4,0,0,0,5,0,6,0],
                                            [0,0,0,0,0,0,0,2,0],
                                            [6,0,0,0,7,0,5,0,4],
                                            [1,5,0,0,0,0,6,0,2],
                                            [0,7,0,2,0,0,0,8,9]], self.cages))
        solver.setupHeap()
        poppedCell = solver.queue.pop_cell()
        solver.KSudoku.grid[0][0] = 5
        # this only changes the domain of one cell 
        self.assertEqual(solver.decreaseKeys(poppedCell[1], 5), [(4, (3, 0), {8, 2, 3, 5})])
