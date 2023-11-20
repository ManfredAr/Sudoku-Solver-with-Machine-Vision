from backend.SudokuHeap import SudokuHeap
import unittest  

class Test_heap(unittest.TestCase):

    # testing the class is instantiated properly.
    # the kep_map and qp should be empty initially.
    def test_Constructor(self):
        queue = SudokuHeap()
        self.assertEqual(queue.key_map, {})
        self.assertEqual(queue.pq, [])
        self.assertEqual(queue.REMOVED, '<removed-task>')

    
    # testing the elements pushed and kept sorted in the heap.
    def test_addToHeap(self):
        queue = SudokuHeap()
        queue.addToHeap((3, (0,0), {1,2,3}))
        queue.addToHeap((1, (4,1), {3}))
        queue.addToHeap((2, (8,8), {4,8}))
        self.assertEqual(queue.pq, [[1, 1, (4, 1), {3}], [3, 0, (0, 0), {1, 2, 3}], [2, 2, (8, 8), {8, 4}]])


    # testing that a removed item contains '<removed-task>' in the last index
    def test_removeTask(self):
        queue = SudokuHeap()
        queue.addToHeap((3, (0,0), {1,2,3}))
        queue.addToHeap((1, (4,1), {3}))
        queue.addToHeap((2, (8,8), {4,8}))
        queue.remove_cell((2, (8,8), {4,8}))
        self.assertEqual(queue.pq, [[1, 1, (4, 1), {3}], [3, 0, (0, 0), {1, 2, 3}], [2, 2, (8, 8), '<removed-task>']])


    # testing that an empty heap will return None
    def test_EmptyPopCell(self):
        queue = SudokuHeap()
        self.assertEqual(queue.pop_cell(), (None, None, None, None))


    # testing that an non-empty heap will return cell with the smallest domain
    def test_PopCell(self):
        queue = SudokuHeap()
        queue.addToHeap((3, (0,0), {1,2,3}))
        queue.addToHeap((1, (4,1), {3}))
        queue.addToHeap((2, (8,8), {4,8}))
        self.assertEqual(queue.pop_cell(), (1, 1, (4, 1), {3}))

    
    # testing that Removed elements are not popped even if they are at the head of the queue
    def test_RemovedPopCell(self):
        queue = SudokuHeap()
        queue.addToHeap((3, (0,0), {1,2,3}))
        queue.addToHeap((1, (4,1), {3}))
        queue.addToHeap((2, (8,8), {4,8}))
        queue.remove_cell((1, (4,1), {3}))
        self.assertEqual(queue.pop_cell(), (2, 2, (8,8), {4,8}))


    # testing after assigning a value to a cell the domains are updated for all affected cells.
    def test_decreaseKey(self):
        queue = SudokuHeap()
        queue.addToHeap((3, (0,0), {1,2,3}))
        queue.addToHeap((1, (4,1), {3}))
        queue.addToHeap((2, (0,8), {2,4}))
        # This code means we have assigned the value 2 to the cell in (0,3)
        # So the affected cells are (0,0) and (0,8) and ther are in the same column, so I need to remove the 2 from their domains.
        self.assertEqual(queue.decreaseKey(0, 3, 2), [((0,8),2), ((0,0),2)])
        self.assertEqual(queue.pq, [[1, 1, (4, 1), {3}], [1, 3, (0, 8), {4}], [2, 2, (0, 8), '<removed-task>'], [3, 0, (0, 0), '<removed-task>'], [2, 4, (0, 0), {1, 3}]])


    # testing that that after reverting a change made the affected cells should go back to how they were before. 
    def test_increase(self):
        queue = SudokuHeap()
        queue.addToHeap((3, (0,0), {1,3}))
        queue.addToHeap((1, (4,1), {3}))
        queue.addToHeap((2, (0,8), {4}))
        queue.increaseKey([((0,8), 2), ((0, 0), 2)])
        self.assertEqual(queue.pq, [[1, 1, (4, 1), {3}], [2, 3, (0, 8), {2, 4}], [2, 2, (0, 8), '<removed-task>'], [3, 0, (0, 0), '<removed-task>'], [3, 4, (0, 0), {1, 2, 3}]])