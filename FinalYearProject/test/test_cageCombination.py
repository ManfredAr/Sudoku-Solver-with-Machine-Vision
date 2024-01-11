from backend.cageCombinations import CageCombinations
import unittest 


class Test_cageCombination(unittest.TestCase):

    # testing the correct combinations are returned.
    def test_combinations(self):
        combination = CageCombinations()
        self.assertEqual(combination.getPossibility(2, 10), [[1,9],[2,8],[3,7],[4,6]])
        self.assertEqual(combination.getPossibility(5,32), [[2,6,7,8,9],[3,5,7,8,9],[4,5,6,8,9]])