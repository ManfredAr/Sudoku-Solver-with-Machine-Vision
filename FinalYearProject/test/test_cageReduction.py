from backend.SudokuTechniques.CageReduction import DomainReduction
import unittest 


class Test_cageReduction(unittest.TestCase):

    # testing that inconsistent domain values are removed in the findCombination method.
    def test_findCombinations(self):
        reduce = DomainReduction()
        arr = [(3,0), (3,1), (3,2)]
        self.assertEqual(reduce.findCombinations(arr, 15, [{1,4,7,9},{4,5,6,9},{1,2,5,7}]), [{1,4,7,9},{4,5,6,9},{1,2,5}])


    # testing that inconsistent domain values are removed.
    def test_combinations(self):
        before = [[-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  [{1,4,7,9},{4,5,6,9},{1,2,5,7},-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1]]
        
        after = [[-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  [{1,4,7,9},{4,5,6,9},{1,2,5},-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1,-1]]

        reduce = DomainReduction()
        arr = [(3,0), (3,1), (3,2)]
        self.assertEqual(reduce.checkCombinations(arr, 15, before), after)