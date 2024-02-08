import heapq
import itertools
from backend.SudokuTechniques.CageReduction import DomainReduction

class KillerSudokuHeap:
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

        if item[2] in self.key_map:
            self.remove_cell(item)
        count = next(self.counter)
        entry = [item[0], item[1], count, item[2], item[3], item[4], "available"]
        self.key_map[item[2]] = entry
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
        entry = self.key_map.pop(task[2])
        entry[-1] = self.REMOVED



    def pop_cell(self):
        '''
        Returns the cell which contains the smallest domain.

        Returns:
        The length of the array, count, the cell and its domain.
        If the queue us empty it returns None fot all. 
        '''
        while self.pq:
            priority, cageLength, count, cell, domain, cageSum, status = heapq.heappop(self.pq)
            if status is not self.REMOVED:
                del self.key_map[cell]
                return priority, cageLength, cell, domain, cageSum
        return None, None, None, None, None
    


    def decreaseCageKey(self, cell, val, lowLim, upLim):
        '''
        Goes through all the cells in the given cells row, column and 3x3 box and
        updates them if the values assigned is contained in their domain.

        Parameters:
        The row, column and the value that was assigned.

        Returns:
        An array containing tuples with the row, column and value of the cells which were updated.
        '''
        item = self.key_map[cell]
        m_set = item[4].copy()
        if val in m_set:
            m_set.remove(val)
        m_set = {i for i in m_set if i <= upLim and i >= lowLim}
        self.addToHeap((len(m_set), item[1]-1, item[3], m_set, item[5]-val))
        return (item[0], item[1], item[3], item[4], item[5])
    

    def reduceDomain(self, cells, killerSudoku):
        '''
        finds any reductions that can be made for any domains.

        parameters:
        cells - a 2d array with the cell in the cage.
        killerSudoku - a killer sudoku object containing the puzzle. 

        returns:
        boolean whether a backtrack is needed or not.
        '''
        reduceCells = []
        cellDomains = []
        sums = 0
        
        for i in cells:
            if killerSudoku.grid[i[0]][i[1]] == 0:
                reduceCells.append(i)
                item = self.key_map[i]
                domain = item[4].copy()
                cellDomains.append(domain)
                sums = item[5]

        domain = DomainReduction()
        newDomain = domain.findCombinations(reduceCells, sums, cellDomains)
        if newDomain == None:
            return False

        for i in range(len(reduceCells)):
            item = self.key_map[reduceCells[i]]
            self.addToHeap((len(newDomain[i]), item[1], item[3], newDomain[i], item[5]))

        return True
        


    def decreaseNonCageKey(self, cell, val):
        '''
        Goes through all the cells in the given cells row, column and 3x3 box and
        updates them if the values assigned is contained in their domain.

        Parameters:
        The row, column and the value that was assigned.

        Returns:
        An array containing tuples with the row, column and value of the cells which were updated.
        '''
        item = self.key_map[cell]
        if val in item[4]:
            m_set = item[4].copy()
            m_set.remove(val)
            self.addToHeap((len(m_set), item[1], item[3], m_set, item[5]))
            return (item[0], item[1], item[3], item[4], item[5])
        return None


        


    def increaseKey(self, updatedCells):
        '''
        Goes through all the cells which were changed and reverts their change.

        Parameters:
        An array containing tuples with the row, col and value which was removed.
        '''
        for updated in updatedCells:
            self.addToHeap(updated)
