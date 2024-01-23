from backend.KillerSudoku import KillerSudoku
from backend.killerSudokuSolver import KillerSudokuSolver
from backend.killerSudokuSolver3 import KillerSudokuSolver3
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
    
    test = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

    grid2 =[[6,2,5,4,3,9,7,1,8],
            [7,1,3,8,2,5,9,6,4],
            [9,8,4,1,6,7,5,2,3],
            [0,9,1,6,7,4,8,0,2],
            [0,7,8,2,9,1,4,0,6],
            [2,4,6,3,5,8,1,9,7],
            [4,5,2,7,1,6,3,8,9],
            [1,3,7,9,8,2,6,4,5],
            [8,6,9,5,4,3,2,7,1]]
    
    cages = {
        1 : { 5 : [(0,0)] },
        2 : { 11 : [(0,1), (1,1)] },
        3 : { 22 : [(0,4), (0,5), (1,4), (1,5)] },
        4 : { 27 : [(0,6), (0,7), (0,8), (1,7), (1,8)] },
        5 : { 7 : [(0,2), (0,3)] },

        6 : { 14 : [(1,0), (2,0), (2,1)] },
        7 : { 14 : [(1,2), (2,2), (3,2)] },
        8 : { 2 : [(1,6)] },
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

    cage2 = {0: {27:[(7, 0), (7, 1), (8, 0), (8, 1), (8, 2)]}, 
            1: {28: [(0, 6), (0, 7), (1, 5), (1, 6), (1, 7)]}, 
            2: {26: [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]}, 
            3: {23: [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8)]}, 
            4: {28: [(2, 1), (3, 1), (4, 1), (5, 1)]}, 
            5: {25: [(5, 8), (6, 8), (7, 7), (7, 8)]}, 
            6: {20: [(3, 4), (3, 5), (4, 5), (5, 5)]}, 
            7: {25: [(6, 3), (7, 3), (8, 3), (8, 4)]}, 
            8: {17: [(6, 4), (6, 5), (7, 4), (7, 5)]}, 
            9: {16: [(3, 6), (3, 7), (4, 7)]}, 
            10: {16:[(3, 3), (4, 2), (4, 3)]}, 
            11: {10:[(8, 6), (8, 7), (8, 8)]}, 
            12: {10:[(5, 6), (6, 6), (7, 6)]}, 
            13: {9: [(0, 0), (0, 1), (1, 1)]}, 
            14: {12:[(0, 2), (1, 2), (2, 2)]}, 
            15: {14:[(0, 3), (1, 3), (1, 4)]}, 
            16: {12:[(0, 4), (0, 5)]}, 
            17: {14:[(2, 3), (2, 4), (2, 5)]}, 
            18: {7: [(2, 6), (2, 7)]}, 
            19: {1: [(3, 2)]}, 
            20: {17:[(4, 4), (5, 3), (5, 4)]}, 
            21: {4: [(4, 6)]}, 
            22: {13:[(5, 2), (6, 1), (6, 2)]}, 
            23: {17:[(5, 7), (6, 7)]}, 
            24: {4: [(6, 0)]}, 
            25: {7: [(7, 2)]}, 
            26: {3: [(8, 5)]}}


    multipleGrid = [[9,2,6,5,7,1,4,8,3],
                    [3,5,1,4,8,6,2,7,9],
                    [8,7,4,9,2,3,5,1,6],
                    [5,8,2,3,6,7,1,9,4],
                    [1,4,9,2,5,8,3,6,7],
                    [7,6,3,1,0,0,8,2,5],
                    [2,3,8,7,0,0,6,5,1],
                    [6,1,7,8,3,5,9,4,2],
                    [4,9,5,6,1,2,7,3,8]]
    
    multiplecages = {
        1 : {45 : [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8)]},
        2 : {45 : [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8)]},
        3 : {45 : [(2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8)]},
        4 : {45 : [(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8)]},
        5 : {45 : [(4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8)]},
        6 : {17 : [(5,0),(5,1),(5,2),(5,3)]},
        7 : {13 : [(5,4),(5,5)]},
        8 : {15 : [(5,6),(5,7),(5,8)]},
        9 : {20 : [(6,0),(6,1),(6,2),(6,3)]},
        10 : {13 : [(6,4),(6,5)]},
        11 : {12 : [(6,6),(6,7),(6,8)]},
        12 : {45 : [(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8)]},
        13 : {45 : [(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8)]},
    }
    
    # testing that the constructor stores the killer sudoku object properly
    def test_Constructor(self):
        solver = KillerSudokuSolver3(KillerSudoku(self.grid, self.cages))
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
        

    # testing the pq contains all the empty cells.
    def test_setupHeap(self):
        solver = KillerSudokuSolver3(KillerSudoku([[0,8,0,1,3,0,0,4,0],
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
        solver2 = KillerSudokuSolver3(KillerSudoku(self.grid, self.cages))
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
        solver = KillerSudokuSolver3(KillerSudoku([[0,8,0,1,3,0,0,4,0],
                                            [0,0,0,0,9,8,0,1,6],
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
        self.assertEqual(solver.decreaseKeys(poppedCell[2], 5, poppedCell[3], poppedCell[4])[0], [(3, 2, (1, 0), {4, 5, 7}, 13), (4, 2, (1, 2), {3, 4, 5, 7}, 12)])


    # testing that a unique puzzle returns 1
    def test_uniquePuzzle(self):
        solver = KillerSudokuSolver3(KillerSudoku(self.grid, self.cages))
        self.assertEqual(solver.SolutionFinder(), 1)


    # testing that a non unique puzzle does not return 1
    def test_NonuniquePuzzle(self):
        solver = KillerSudokuSolver3(KillerSudoku(self.multipleGrid, self.multiplecages))
        self.assertEqual(solver.SolutionFinder(), 2)


    # testing that 1 is returned
    def test_uniquePuzzle2(self):
        solver = KillerSudokuSolver3(KillerSudoku(self.test, self.cage2))
        self.assertNotEqual(solver.SolutionFinder(), 1)
