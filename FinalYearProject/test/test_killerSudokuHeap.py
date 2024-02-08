from backend.killerSudokuHeap import KillerSudokuHeap
from backend.KillerSudoku import KillerSudoku
import unittest  

class Test_KSudokuHeap(unittest.TestCase):

    grid = [[0,0,0,1,3,0,0,4,0],
        [0,0,0,5,9,8,0,1,6],
        [0,0,2,0,0,0,0,5,0],
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

    # testing the class is instantiated properly.
    # the kep_map and qp should be empty initially.
    def test_Constructor(self):
        queue = KillerSudokuHeap()
        self.assertEqual(queue.key_map, {})
        self.assertEqual(queue.pq, [])
        self.assertEqual(queue.REMOVED, '<removed-task>')

    
    # testing the elements pushed and kept sorted in the heap.
    def test_addToHeap(self):
        queue = KillerSudokuHeap()
        queue.addToHeap((3, 1, (0,0), {1,2,3}, 3))
        queue.addToHeap((1, 1, (4,1), {3}, 2))
        queue.addToHeap((2, 1, (8,8), {4,8}, 4))
        self.assertEqual(queue.pq, [[1, 1, 1, (4, 1), {3}, 2, 'available'], [3, 1, 0, (0, 0), {1, 2, 3}, 3, 'available'], [2, 1, 2, (8, 8), {8, 4}, 4, 'available']])


    # testing that a removed item contains '<removed-task>' in the last index
    def test_removeTask(self):
        queue = KillerSudokuHeap()
        queue.addToHeap((3, 1, (0,0), {1,2,3}, 3))
        queue.addToHeap((1, 1, (4,1), {3}, 2))
        queue.addToHeap((2, 1, (8,8), {4,8}, 4))
        queue.remove_cell((2, 1, (8,8), {4,8}))
        self.assertEqual(queue.pq, [[1, 1, 1, (4, 1), {3}, 2, 'available'], [3, 1, 0, (0, 0), {1, 2, 3}, 3, 'available'], [2, 1, 2, (8, 8), {8, 4}, 4, '<removed-task>']])


    # testing that an empty heap will return None
    def test_EmptyPopCell(self):
        queue = KillerSudokuHeap()
        self.assertEqual(queue.pop_cell(), (None, None, None, None, None))


    # testing that an non-empty heap will return cell with the smallest domain
    def test_PopCell(self):
        queue = KillerSudokuHeap()
        queue.addToHeap((3, 1, (0,0), {1,2,3}, 3))
        queue.addToHeap((1, 1, (4,1), {3}, 2))
        queue.addToHeap((2, 1, (8,8), {4,8}, 4))
        self.assertEqual(queue.pop_cell(), (1, 1, (4, 1), {3}, 2))

    
    # testing that Removed elements are not popped even if they are at the head of the queue
    def test_RemovedPopCell(self):
        queue = KillerSudokuHeap()
        queue.addToHeap((3, 1, (0,0), {1,2,3}, 3))
        queue.addToHeap((1, 1, (4,1), {3}, 2))
        queue.addToHeap((2, 1, (8,8), {4,8}, 4))
        queue.remove_cell((1, 1, (4,1), {3}, 2))
        self.assertEqual(queue.pop_cell(), (2, 1, (8, 8), {8, 4}, 4))


    # testing after assigning a value to a cell the domains are updated for all cage values
    def test_decreaseCageKey(self):
        queue = KillerSudokuHeap()
        queue.addToHeap((3, 1, (0,0), {1,2,3}, 3))
        queue.addToHeap((1, 1, (4,1), {3}, 2))
        queue.addToHeap((2, 1, (8,8), {4,8}, 4))
        queue.decreaseCageKey((0, 0), 3, 1, 2)
        self.assertEqual(queue.pq, [[1, 1, 1, (4, 1), {3}, 2, 'available'], [2, 0, 3, (0, 0), {1, 2}, 0, 'available'], [2, 1, 2, (8, 8), {8, 4}, 4, 'available'], [3, 1, 0, (0, 0), {1, 2, 3}, 3, '<removed-task>']])


    # testing after assigning a value to a cell the domains are updated for non cage values
    def test_decreaseNonCageKey(self):
        queue = KillerSudokuHeap()
        queue.addToHeap((3, 1, (0,0), {1,2,3}, 3))
        queue.decreaseNonCageKey((0, 0), 2)
        self.assertEqual(queue.pq, [[2, 1, 1, (0, 0), {1, 3}, 3, 'available'], [3, 1, 0, (0, 0), {1, 2, 3}, 3, '<removed-task>']])


    # testing that after reverting a change made the affected cells should go back to how they were before. 
    def test_increase(self):
        queue = KillerSudokuHeap()
        queue.addToHeap((3, 1, (0,0), {1,2,3}, 3))
        queue.addToHeap((1, 1, (4,1), {3}, 2))
        queue.addToHeap((2, 1, (8,8), {4,8}, 4))
        queue.increaseKey([(2, 1, (4,1), {3,4}, 5)])
        self.assertEqual(queue.pq, [[1, 1, 1, (4, 1), {3}, 2, '<removed-task>'], [2, 1, 3, (4, 1), {3, 4}, 5, 'available'], [2, 1, 2, (8, 8), {8, 4}, 4, 'available'], [3, 1, 0, (0, 0), {1, 2, 3}, 3, 'available']])


    # testing that if domains were updating without any errors then it shoudl return false
    def test_noBacktrack(self):
        queue = KillerSudokuHeap()
        queue.addToHeap((4, 3, (1,0), {1,4,7,9}, 15))
        queue.addToHeap((4, 3, (2,0), {4,5,6,9}, 15))
        queue.addToHeap((4, 3, (2,1), {1,2,5,7}, 15))
        queue.reduceDomain([(1,0),(2,0),(2,1)], KillerSudoku(self.grid, self.cages))
        self.assertEqual(queue.reduceDomain([(1,0),(2,0),(2,1)], KillerSudoku(self.grid, self.cages)), True)


    # testing that if there was an error while updating domains false is returned.
    def test_Backtrack(self):
        queue = KillerSudokuHeap()
        queue.addToHeap((4, 3, (1,0), {1,4,7,9}, 15))
        queue.addToHeap((4, 3, (2,0), {4,5,6,9}, 15))
        queue.addToHeap((4, 3, (2,1), {7}, 15))
        queue.reduceDomain([(1,0),(2,0),(2,1)], KillerSudoku(self.grid, self.cages))
        self.assertEqual(queue.reduceDomain([(1,0),(2,0),(2,1)], KillerSudoku(self.grid, self.cages)), False)

