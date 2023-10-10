import heapq
import itertools

class heap:

    def __init__(self):
        self.pq = []
        self.key_map = {} 
        self.REMOVED = '<removed-task>'  
        self.counter = itertools.count() 

    

    def addToHeap(self, item):
        if item[1] in self.key_map:
            self.remove_cell(item)
        count = next(self.counter)
        entry = [item[0], count, item[1], item[2]]
        self.key_map[item[1]] = entry
        heapq.heappush(self.pq, entry)



    def remove_cell(self, task):
        entry = self.key_map.pop(task[1])
        entry[-1] = self.REMOVED



    def pop_cell(self):
        while self.pq:
            priority, count, cell, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.key_map[cell]
                return priority, count, cell, task
        return None, None, None, None
    


    def decreaseKey(self, row, col, val):
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
        for updated in updatedCells:
            m_set = self.key_map[updated[0]][3]
            m_set.add(updated[1])
            self.addToHeap((len(m_set), updated[0], m_set))
