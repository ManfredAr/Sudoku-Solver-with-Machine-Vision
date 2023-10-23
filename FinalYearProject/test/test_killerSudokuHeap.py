from backend.KillerSudokuHeap import KillerSudokuHeap
import unittest  

class Test_KSudokuHeap(unittest.TestCase):

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
        queue.addToHeap((3, (0,0), {1,2,3}))
        queue.addToHeap((1, (4,1), {3}))
        queue.addToHeap((2, (8,8), {4,8}))
        self.assertEqual(queue.pq, [[1, 1, (4, 1), {3}, 'available'], [3, 0, (0, 0), {1, 2, 3}, 'available'], [2, 2, (8, 8), {8, 4}, 'available']])


    # testing that a removed item contains '<removed-task>' in the last index
    def test_removeTask(self):
        queue = KillerSudokuHeap()
        queue.addToHeap((3, (0,0), {1,2,3}))
        queue.addToHeap((1, (4,1), {3}))
        queue.addToHeap((2, (8,8), {4,8}))
        queue.remove_cell((2, (8,8), {4,8}))
        self.assertEqual(queue.pq, [[1, 1, (4, 1), {3}, 'available'], [3, 0, (0, 0), {1, 2, 3}, 'available'], [2, 2, (8, 8), {8, 4}, '<removed-task>']])


    # testing that an empty heap will return None
    def test_EmptyPopCell(self):
        queue = KillerSudokuHeap()
        self.assertEqual(queue.pop_cell(), (None, None, None))


    # testing that an non-empty heap will return cell with the smallest domain
    def test_PopCell(self):
        queue = KillerSudokuHeap()
        queue.addToHeap((3, (0,0), {1,2,3}))
        queue.addToHeap((1, (4,1), {3}))
        queue.addToHeap((2, (8,8), {4,8}))
        self.assertEqual(queue.pop_cell(), (1, (4, 1), {3}))

    
    # testing that Removed elements are not popped even if they are at the head of the queue
    def test_RemovedPopCell(self):
        queue = KillerSudokuHeap()
        queue.addToHeap((3, (0,0), {1,2,3}))
        queue.addToHeap((1, (4,1), {3}))
        queue.addToHeap((2, (8,8), {4,8}))
        queue.remove_cell((1, (4,1), {3}))
        self.assertEqual(queue.pop_cell(), (2, (8, 8), {8, 4}))


    # testing after assigning a value to a cell the domains are updated for all cage values
    def test_decreaseCageKey(self):
        queue = KillerSudokuHeap()
        queue.addToHeap((3, (0,0), {1,2,3}))
        queue.addToHeap((1, (4,1), {3}))
        queue.addToHeap((2, (0,8), {2,4}))
        queue.decreaseCageKey((0, 0), {1,2})
        self.assertEqual(queue.pq, [[1, 1, (4, 1), {3}, 'available'], [2, 3, (0, 0), {1, 2}, 'available'], [2, 2, (0, 8), {2, 4}, 'available'], [3, 0, (0, 0), {1, 2, 3}, '<removed-task>']])


    # testing after assigning a value to a cell the domains are updated for non cage values
    def test_decreaseNonCageKey(self):
        queue = KillerSudokuHeap()
        queue.addToHeap((3, (0,0), {1,2,3}))
        queue.decreaseNonCageKey((0, 0), 2)
        self.assertEqual(queue.pq, [[2, 1, (0, 0), {1, 3}, 'available'], [3, 0, (0, 0), {1, 2, 3}, '<removed-task>']])


    # testing that that after reverting a change made the affected cells should go back to how they were before. 
    def test_increase(self):
        queue = KillerSudokuHeap()
        queue.addToHeap((3, (0,0), {1,3}))
        queue.addToHeap((1, (4,1), {3}))
        queue.addToHeap((2, (0,8), {4}))
        queue.increaseKey([(2, 2, (0,8), {1,4})])
        self.assertEqual(queue.pq, [[1, 1, (4, 1), {3}, 'available'], [2, 3, 2, (0, 8), 'available'], [2, 2, (0, 8), {4}, 'available'], [3, 0, (0, 0), {1, 3}, 'available']])
