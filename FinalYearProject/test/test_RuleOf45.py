from backend.SudokuTechniques.ruleOf45 import ruleOf45
from backend.KillerSudoku import KillerSudoku
from backend.KSudokuDomain import KillerSudokuDomain
import copy
import unittest  

class Test_ruleOf45(unittest.TestCase):

    grid = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,2,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]
    
    grid2 = [[2,0,0,0,0,0,0,0,0],
            [0,0,7,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [7,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [3,0,0,0,0,0,0,0,0]]
    
    grid3 = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,5,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,2,0,0,0,0,0,0],
            [0,0,9,0,0,0,0,0,0]]

    cage = {
        1 : {13 : [(0,0),(1,0),(2,0)] },
        2 : {7 : [(0,1),(0,2)] },
        3 : {14 : [(0,3),(0,4)] },
        4 : {12 : [(0,5),(0,6)] },
        5 : {16 : [(0,7),(0,8),(1,7)] },
        6 : {17 : [(1,1),(2,1)] },
        7 : {9 : [(1,2),(1,3)] },
        8 : {10 : [(1,4),(1,5)] },
        9 : {6 : [(1,6),(2,6),(3,6)] },
        35 : {8 : [(2,7)] },
        10 : {6 : [(1,8),(2,8)] },
        11 : {4 : [(2,2),(2,3)] },
        12 : {45 : [(2,4),(3,3),(3,4),(4,3),(4,4),(4,5),(5,4),(5,5),(6,4)] },
        13 : {7 : [(2,5), (3,5)] },
        14 : {13 : [(3,0),(4,0)] },
        15 : {4 : [(3,1),(3,2)] },
        16 : {5 : [(3,7)] },
        36 : {8 : [(3,8)] },
        17 : {7 : [(4,1),(4,2)] },
        18 : {7 : [(4,6),(4,7)] },
        19 : {16 : [(4,8),(5,8)] },
        20 : {13 : [(5,0), (5,1)] },
        21 : {16 : [(5,2),(6,2),(7,2)] },
        22 : {5 : [(5,3),(6,3)] },
        23 : {5 : [(5,6), (5,7)] },
        24 : {13 : [(6,0), (6,1),(7,0)] },
        25 : {12 : [(6,5),(6,6)] },
        26 : {11 : [(6,7), (7,7)] },
        27 : {14 : [(6,8),(7,8),(8,8)] },
        28 : {7 : [(7,1)] },
        29 : {8 : [(8,0),(8,1)] },
        30 : {14 : [(7,3),(7,4)] },
        31 : {14 : [(7,5),(7,6)] },
        32 : {17 : [(8,2),(8,3)] },
        33 : {11 : [(8,4), (8,5)] },
        34 : {3 : [(8,6), (8,7)] }
    }

    cage2 = {
        1 : {13 : [(0,0),(1,0),(2,0)] },
        2 : {7 : [(0,1),(0,2)] },
        3 : {14 : [(0,3),(0,4)] },
        4 : {12 : [(0,5),(0,6)] },
        5 : {16 : [(0,7),(0,8),(1,7)] },
        6 : {17 : [(1,1),(2,1)] },
        7 : {9 : [(1,2),(1,3)] },
        8 : {10 : [(1,4),(1,5)] },
        9 : {14 : [(1,6),(2,6),(3,6)] },
        10 : {14 : [(1,8),(2,7),(2,8)] },
        11 : {4 : [(2,2),(2,3)] },
        12 : {45 : [(2,4),(3,3),(3,4),(4,3),(4,4),(4,5),(5,4),(5,5),(6,4)] },
        13 : {7 : [(2,5), (3,5)] },
        14 : {13 : [(3,0),(4,0)] },
        15 : {4 : [(3,1),(3,2)] },
        16 : {13 : [(3,7),(3,8)] },
        17 : {2 : [(4,1)] },
        18 : {7 : [(4,6),(4,7)] },
        19 : {16 : [(4,8),(5,8)] },
        20 : {13 : [(5,0), (5,1)] },
        21 : {21 : [(4,2),(5,2),(6,2),(7,2)] },
        22 : {5 : [(5,3),(6,3)] },
        23 : {5 : [(5,6), (5,7)] },
        24 : {13 : [(6,0), (6,1),(7,0)] },
        25 : {12 : [(6,5),(6,6)] },
        26 : {11 : [(6,7), (7,7)] },
        27 : {14 : [(6,8),(7,8),(8,8)] },
        28 : {15 : [(7,1),(8,0),(8,1)] },
        29 : {14 : [(7,3),(7,4)] },
        30 : {14 : [(7,5),(7,6)] },
        31 : {17 : [(8,2),(8,3)] },
        32 : {11 : [(8,4), (8,5)] },
        33 : {3 : [(8,6), (8,7)] }
    }

    # testing that mutiple outside cages returns none in row
    def test_checkRuleOf45RowsNone(self):
        d = KillerSudokuDomain(KillerSudoku(self.grid, self.cage))
        domain = d.getAllDomains()
        ro45 = ruleOf45(KillerSudoku(self.grid, self.cage))
        self.assertEqual(ro45.checkRuleOf45Row(0, domain)[0], None)


    # testing that rule of 45 is applied properly in rows
    def test_checkRuleOf45Rows(self):
        d = KillerSudokuDomain(KillerSudoku(self.grid, self.cage))
        domain = d.getAllDomains()
        newDomain = copy.deepcopy(domain)
        newDomain[8][8] = set([6])
        newDomain[7][8] = set([1,3,5,7,6])
        newDomain[6][8] = set([1,3,5,7,6,2])
        ro45 = ruleOf45(KillerSudoku(self.grid, self.cage))
        self.assertEqual(ro45.checkRuleOf45Row(8, domain)[0], newDomain)


    # testing that mutiple outside cages returns none in column
    def test_checkRuleOf45ColumnNone(self):
        ro45 = ruleOf45(KillerSudoku(self.grid, self.cage))
        d = KillerSudokuDomain(KillerSudoku(self.grid, self.cage))
        domain = d.getAllDomains()
        self.assertEqual(ro45.checkRuleOf45Column(0,domain)[0], None)


    # testing that rule of 45 is applied properly in columns
    def test_checkRuleOf45Column(self):
        ro45 = ruleOf45(KillerSudoku(self.grid, self.cage))
        d = KillerSudokuDomain(KillerSudoku(self.grid, self.cage))
        domain = d.getAllDomains()
        newDomain = copy.deepcopy(domain)
        newDomain[0][8] = set([1])
        newDomain[0][7] = set([9,6,8,7])
        newDomain[1][7] = set([9,6,8,7])
        self.assertEqual(ro45.checkRuleOf45Column(8,domain)[0], newDomain)


    # testing that mutiple outside cages returns none in box
    def test_checkRuleOf45BoxNone(self):
        ro45 = ruleOf45(KillerSudoku(self.grid, self.cage))
        d = KillerSudokuDomain(KillerSudoku(self.grid, self.cage))
        domain = d.getAllDomains()
        self.assertEqual(ro45.checkRuleOf45Box(0, 0, domain)[0], None)


    # testing that rule of 45 is applied properly in boxes
    def test_checkRuleOf45Box(self):
        ro45 = ruleOf45(KillerSudoku(self.grid3, self.cage2))
        d = KillerSudokuDomain(KillerSudoku(self.grid3, self.cage2))
        domain = d.getAllDomains()
        newDomain = copy.deepcopy(domain)
        newDomain[3][6] = set([4])
        newDomain[2][6] = set([1,9,2,8,3,7,4,6])
        newDomain[1][6] = set([1,9,2,8,3,7,4,6])
        self.assertEqual(ro45.checkRuleOf45Box(1,2, domain)[0], newDomain)


    # testing that rule of 45 is applied properly in rows with some cells filled in
    def test_checkRuleOf45RowsPartial(self):
        d = KillerSudokuDomain(KillerSudoku(self.grid2, self.cage))
        domain = d.getAllDomains()
        newDomain = copy.deepcopy(domain)
        newDomain[0][7] = set([1,9,8,3,7,4,6])
        newDomain[0][8] = set([1,9,8,3,7,4,6])
        newDomain[1][7] = set([6])
        ro45 = ruleOf45(KillerSudoku(self.grid2, self.cage))
        self.assertEqual(ro45.checkRuleOf45Row(0, domain)[0], newDomain)
    

    # testing that rule of 45 is applied properly in columns with some cells filled in
    def test_checkRuleOf45ColumnPartial(self):
        ro45 = ruleOf45(KillerSudoku(self.grid2, self.cage))
        d = KillerSudokuDomain(KillerSudoku(self.grid2, self.cage))
        domain = d.getAllDomains()
        newDomain = copy.deepcopy(domain)
        newDomain[6][0] = set([1,8,6,4,5])
        newDomain[7][0] = set([1,8,6,4,5])
        newDomain[6][1] = set([4])
        self.assertEqual(ro45.checkRuleOf45Column(0,domain)[0], newDomain)


    # testing that rule of 45 is applied properly in boxes with some cells filled in
    def est_checkRuleOf45BoxPartial(self):
        ro45 = ruleOf45(KillerSudoku(self.grid2, self.cage))
        d = KillerSudokuDomain(KillerSudoku(self.grid2, self.cage))
        domain = d.getAllDomains()
        newDomain = copy.deepcopy(domain)
        newDomain[2][2] = set([1])
        newDomain[2][3] = set([3])
        self.assertEqual(ro45.checkRuleOf45Box(0, 0, domain)[0], newDomain)


    # testing that reduce domains returns the correct domain
    def test_reduceDomains(self):
        ro45 = ruleOf45(KillerSudoku(self.grid2, self.cage))
        d = KillerSudokuDomain(KillerSudoku(self.grid2, self.cage))
        domain = d.getAllDomains()
        newDomain = copy.deepcopy(domain)
        newDomain[2][2] = set([1])
        newDomain[2][3] = set([3])
        self.assertEqual(ro45.reduceDomains([(2,2)], 11, 1, domain), newDomain)


    # testing that reduce domains returns the correct domain when cells are filled in
    def test_reduceDomainsWithFilled(self):
        ro45 = ruleOf45(KillerSudoku(self.grid, self.cage))
        d = KillerSudokuDomain(KillerSudoku(self.grid, self.cage))
        domain = d.getAllDomains()
        newDomain = copy.deepcopy(domain)
        newDomain[5][2] = set([8])
        newDomain[6][2] = set([6])
        self.assertEqual(ro45.reduceDomains([(5,2)], 21, 8, domain), newDomain)
        

    # testing that rule of 45 is applied correctly with large cages and partially filled.
    def test_boxWithMixedFilled(self):
        ro45 = ruleOf45(KillerSudoku(self.grid3, self.cage2))
        d = KillerSudokuDomain(KillerSudoku(self.grid3, self.cage2))
        domain = d.getAllDomains()
        newDomain = copy.deepcopy(domain)
        newDomain[5][2] = set([8])
        newDomain[7][2] = set([2])
        self.assertEqual(ro45.checkRuleOf45Box(2,0,domain)[0][4], newDomain[4])
        