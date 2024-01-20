import copy

class DomainReduction:

    def checkReduction(self, killerSudoku, domain):
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
        tempDomains = [set() for i in range(len(cells))]
        for i in range(len(cells)):
            tempDomains[i] = domain[cells[i][0], cells[i][1]]
        combos = self.fit(tempDomains, 0, set(), len(cells), sums)
        if len(combos) != 0:
            for i in range(len(cells)):
                domain[cells[i][0]][cells[i][1]] = set([combo[i] for combo in combos])

        return domain


    def fit(self, tempDomain, idx, used, length, total):
        tempDomain[idx] -= used

        if idx + 1 == length or len(tempDomain[idx]) == 0 or total < 0:
            return []

        allCombos = []

        for num in tempDomain[idx]:
            used.add(num)
            used = self.fit(tempDomain, idx+1, used, length, total-num)

            if len(used) == length:
                allCombos += list(used)

        return allCombos
            
