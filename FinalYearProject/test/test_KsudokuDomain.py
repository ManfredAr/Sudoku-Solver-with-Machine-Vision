from backend.KSudokuDomain import KillerSudokuDomain
import unittest 
from backend.KillerSudoku import KillerSudoku


class Test_killerSudokuDomain(unittest.TestCase):

    grid = [[0,8,0,1,3,0,0,4,0],
            [0,0,0,5,9,8,0,1,6],
            [0,1,2,0,0,0,0,5,0],
            [0,0,0,4,0,7,0,9,0],
            [0,4,0,0,0,5,0,6,0],
            [0,0,0,0,0,0,0,2,0],
            [6,0,0,0,0,0,0,0,0],
            [1,5,0,0,0,0,6,0,2],
            [0,7,0,0,0,0,0,8,9]]
    
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

    # testing only used values are returned
    def test_getUsedValues(self):
        domain = KillerSudokuDomain(KillerSudoku(self.grid, self.cages))
        self.assertEqual(domain.getUsedValues(0, 0), set([1,2,3,4,6,8]))

    # testing the correct domain is returned for empty cages
    def test_getSingleDomain(self):
        domain = KillerSudokuDomain(KillerSudoku(self.grid, self.cages))
        self.assertEqual(domain.getDomain(6, 5)[0], set([1,2,3,4,9]))
        self.assertEqual(domain.getDomain(6, 5)[1], 3)
        self.assertEqual(domain.getDomain(6, 5)[2], 15)

    # testing the correct domain is returned for partially filled domains.
    def test_partiallyFilledCageGetDomain(self):
        domain = KillerSudokuDomain(KillerSudoku(self.grid, self.cages))
        self.assertEqual(domain.getDomain(0, 8)[0], set([7]))
        self.assertEqual(domain.getDomain(0, 8)[1], 2)
        self.assertEqual(domain.getDomain(0, 8)[2], 16)
