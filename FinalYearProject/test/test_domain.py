from backend.domain import Domain
import unittest  

class Test_Domain(unittest.TestCase):

    grid = [[5, 8, 0, 1, 3, 2, 9, 0, 7],
            [4, 3, 7, 5, 9, 8, 2, 1, 6],
            [9, 1, 2, 7, 6, 4, 8, 5, 3],
            [0, 0, 5, 4, 2, 7, 3, 9, 1],
            [2, 4, 3, 9, 1, 0, 7, 6, 8],
            [7, 9, 1, 6, 8, 3, 4, 2, 5],
            [6, 0, 9, 8, 7, 1, 5, 3, 4],
            [1, 5, 0, 3, 4, 0, 6, 0, 2],
            [3, 7, 4, 2, 5, 6, 1, 8, 9]]
    
    def test_getDomains(self):
        domains = Domain(self.grid)
        self.assertEqual(domains.getDomain(0, 2), {6})

    def test_getAllDomains(self):
        domains = Domain(self.grid)
        self.assertEqual(domains.getAllDomains(), [[-1, -1, {6}, -1, -1, -1, -1, {4}, -1], 
                                                   [-1, -1, -1, -1, -1, -1, -1, -1, -1], 
                                                   [-1, -1, -1, -1, -1, -1, -1, -1, -1], 
                                                   [{8}, {6}, -1, -1, -1, -1, -1, -1, -1], 
                                                   [-1, -1, -1, -1, -1, {5}, -1, -1, -1], 
                                                   [-1, -1, -1, -1, -1, -1, -1, -1, -1], 
                                                   [-1, {2}, -1, -1, -1, -1, -1, -1, -1], 
                                                   [-1, -1, {8}, -1, -1, {9}, -1, {7}, -1], 
                                                   [-1, -1, -1, -1, -1, -1, -1, -1, -1]])
        

