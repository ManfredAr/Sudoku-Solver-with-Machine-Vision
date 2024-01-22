import copy

class DomainReduction:
    '''
    This class is responsible for using cage combinations to reduce
    the domains for cells and 
    '''

    def checkReduction(self, killerSudoku, domain):
        '''
        Tries to reduce the domains for all cells in the puzzle.

        parameters:
        killerSudoku - the killer sudoku object containing the puzzle
        domain - a 2d array containing the domain for each cell

        returns:
        a modified domain with a reduced valuess.
        '''
        for cageNumber, cage in killerSudoku.cages.items():
            for cageSum, cells in cage.items():
                remaining_cells = []
                remaining_sum = cageSum
                for cell in cells:
                    if killerSudoku.grid[cell[0]][cell[1]] != 0:
                        remaining_sum -= killerSudoku.grid[cell[0]][cell[1]]
                    else:
                        remaining_cells.append(cell)

                domain = self.checkCombinations(remaining_cells, remaining_sum, domain)

        return domain
    


    def checkCombinations(self, cells, sums, domain):
        '''
        Check the domains for all cages and try to look for reductions.

        parameters:
        cells - the cells in the cage
        sums - the sum the cells should add up to
        domain - 2d array containing the domains

        returns:
        An updated domain to reflect changed domains.
        '''
        tempDomains = [0 for i in range(len(cells))]
        for i in range(len(cells)):
            tempDomains[i] = domain[cells[i][0]][cells[i][1]]
        combos = self.fit(tempDomains, 0, [], len(cells), sums)
        if len(combos) != 0:
            for i in range(len(cells)):
                domain[cells[i][0]][cells[i][1]] = set([combo[i] for combo in combos])
        return domain
    

    def findCombinations(self, cells, sums, domains):
        '''
        Finds all combinations within the domains which add up to the sums.

        parameters:
        cells - a 2d array with the cells involved
        sums - the sum the cells should add up to
        domains - a 2d array with the set containing each cells domains

        returns:
        A 2d array with sets containing the reduced domains
        None if reductions returned empty sets.
        '''
        combos = self.fit(domains, 0, [], len(cells), sums)
        
        if combos == None or len(combos) == 0:
            return None
        
        for i in range(len(cells)):
            domains[i] = set([combo[i] for combo in combos])
        return domains


    def fit(self, tempDomain, idx, used, length, total):
        '''
        Recursively tries to find all combinations of domaisn which add up to the sum.

        parameters:
        tempDomains - the current domains of the cells in an array
        idx - 0
        used - an empty set
        length - int containing the number of cell
        total - the int contain the cage sum

        returns:
        A 2d array containing all possible combinations.
        '''
        # combination found so return solution
        if idx == length and total == 0:
            return [list(used)]

        # no solution for current values so backtrack
        if idx == length or len(tempDomain[idx]) == 0 or total < 0:
            return None

        allCombos = []

        # tries all values in the domains
        for num in tempDomain[idx]:
            if num not in used:
                used.append(num)
                combo = self.fit(tempDomain, idx + 1, used, length, total - num)

                if combo is not None:
                    allCombos.extend(combo)

                # remove last added value
                used.pop()

        return allCombos