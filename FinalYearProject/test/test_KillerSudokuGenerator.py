from backend.killerSudokuGenerator import killerSudokuGenerator
import unittest  

class Test_KillerSudokuGenerator(unittest.TestCase):

    def test_connected5cells(self):
        gen = killerSudokuGenerator()
        gen.grid = [[1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [2,-1,-1,-1,-1,-1,-1,-1,-1],
                    [3,-1,-1,-1,-1,-1,-1,-1,-1],
                    [4, 5,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1]]
        self.assertEqual(gen.findConnectCells(5, (0,0), []), set([(0,0), (1,0), (2,0), (3,0), (3,1)]))

    def test_connectedNonecells(self):
        gen = killerSudokuGenerator()
        gen.grid = [[1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [2,-1,-1,-1,-1,-1,-1,-1,-1],
                    [3,-1,-1,-1,-1,-1,-1,-1,-1],
                    [4, 5,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1]]
        self.assertEqual(gen.findConnectCells(5, (8,0), []), -1)

    def test_connectedRandomcells(self):
        gen = killerSudokuGenerator()
        gen.grid = [[1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [2,-1,-1,-1,-1,-1,-1,-1,-1],
                    [3,-1,-1,-1,-1,-1,-1,-1,-1],
                    [4, 5,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1]]
        cells = gen.findConnectCells(5, (2,0), [])
        self.assertEqual(cells, set([(0,0), (1,0), (2,0), (3,0), (3,1)]))


    def test_addCage(self):
        gen = killerSudokuGenerator()
        gen.grid = [[1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [2,-1,-1,-1,-1,-1,-1,-1,-1],
                    [3,-1,-1,-1,-1,-1,-1,-1,-1],
                    [4, 5,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1]]
        cells = gen.findConnectCells(5, (2,0), [])
        remaining = [(i, j) for i in range(9) for j in range(9)]  
        gen.addCage(list(cells), remaining)
        self.assertEqual(gen.cages[0], {15 : [(0,0), (1,0), (2,0), (3,0), (3,1)]})


    def test_FillRemainingCells(self):
        gen = killerSudokuGenerator()
        gen.grid = [[4,9,2,8,1,5,7,6,3],
                    [6,5,7,4,2,3,1,9,8],
                    [1,3,8,9,6,7,4,5,2],
                    [8,7,4,2,3,9,6,1,5],
                    [3,1,9,5,8,6,2,4,7],
                    [2,6,5,7,4,1,8,3,9],
                    [5,8,6,1,9,2,3,7,4],
                    [9,4,3,6,7,8,5,2,1],
                    [7,2,1,3,5,4,9,8,6]]
        remaining = [(i, j) for i in range(9) for j in range(9)] 
        gen.fillRemainingCells(remaining)
        total = 0
        cellAmount = 0
        for key, inner_dict in gen.cages.items():
            total += sum(inner_dict.keys())
            cellAmount += sum(len(cells) for cells in inner_dict.values())
        self.assertEqual(total, 405)
        self.assertEqual(cellAmount, 81)


    def test_FindCages(self):
        gen = killerSudokuGenerator()
        gen.grid = [[9,2,6,5,7,1,4,8,3],
                    [3,5,1,4,8,6,2,7,9],
                    [8,7,4,9,2,3,5,1,6],
                    [5,8,2,3,6,7,1,9,4],
                    [1,4,9,2,5,8,3,6,7],
                    [7,6,3,1,0,0,8,2,5],
                    [2,3,8,7,0,0,6,5,1],
                    [6,1,7,8,3,5,9,4,2],
                    [4,9,5,6,1,2,7,3,8]]
        gen.generateCages({"3" : [3], "4" : [2], "5" : [1]})
        differentCages = 0
        for key, inner_dict in gen.cages.items():
            cellAmount = sum(len(cells) for cells in inner_dict.values())
            if cellAmount == 3 or cellAmount == 4 or cellAmount == 5:
                differentCages += 1
        self.assertEqual(differentCages, 6)