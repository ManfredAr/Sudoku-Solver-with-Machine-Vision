import heapq
import itertools

class SudokuHeap:
    '''
    This class is an implementation of a priority queue 
    to order the cells in order of the smallest domain first.
    '''

    def __init__(self):
        '''
        constructor for the queue and initialises the required values.
        '''
        self.pq = []
        self.key_map = {} 
        self.REMOVED = '<removed-task>'  
        self.counter = itertools.count() 

    

    def addToHeap(self, item):
        '''
        Takes a cell and pushes it into the priority queue to be ordered.

        parameters:
        A tuple containing:
        - the length of the domain
        - A tuple containing the row and column
        - A set containing all the values in the domain
        '''

        if item[1] in self.key_map:
            self.remove_cell(item)
        count = next(self.counter)
        entry = [item[0], count, item[1], item[2]]
        self.key_map[item[1]] = entry
        heapq.heappush(self.pq, entry)



    def remove_cell(self, task):
        '''
        Sets the given task to removed. The cell is not removed it is simple ignored. 

        parameters:
        A tuple containing:
        - the length of the domain
        - A tuple containing the row and column
        - A set containing all the values in the domain
        '''
        entry = self.key_map.pop(task[1])
        entry[-1] = self.REMOVED



    def pop_cell(self):
        '''
        Returns the cell which contains the smallest domain.

        Returns:
        The length of the array, count, the cell and its domain.
        If the queue us empty it returns None fot all. 
        '''
        while self.pq:
            priority, count, cell, domain = heapq.heappop(self.pq)
            if domain is not self.REMOVED:
                del self.key_map[cell]
                return priority, count, cell, domain
        return None, None, None, None
    


    def decreaseKey(self, row, col, val):
        '''
        Goes through all the cells in the given cells row, column and 3x3 box and
        updates them if the values assigned is contained in their domain.

        Parameters:
        The row, column and the value that was assigned.

        Returns:
        An array containing tuples with the row, column and value of the cells which were updated.
        '''
        cells = set()
        for i in range(9):
            if (row, i) in self.key_map:
                cells.add((row, i))

            if (i, col) in self.key_map:
                cells.add((i, col))

        box_row = (row // 3) * 3
        col_box = (col // 3) * 3

        for a in range(box_row, box_row + 3):
            for b in range(col_box, col_box + 3):
                if (a, b) in self.key_map:
                    cells.add((a, b))
        removed = []
        for i in cells:
            if val in self.key_map[i][3]:
                m_set = self.key_map[i][3]
                m_set.remove(val)
                removed.append((i, val))
                self.addToHeap((self.key_map[i][0] - 1, i, m_set))
        return removed


    def increaseKey(self, updatedCells):
        '''
        Goes through all the cells which were changed and reverts their change.

        Parameters:
        An array containing tuples with the row, col and value which was removed.
        '''
        for updated in updatedCells:
            m_set = self.key_map[updated[0]][3]
            m_set.add(updated[1])
            self.addToHeap((len(m_set), updated[0], m_set))
