from backend.domain import Domain
from backend.SudokuTechniques.HiddenSinglePairTriple import HiddenSinglePairTriple
from backend.SudokuTechniques.ObviousSinglePairTriple import ObviousSinglePairTriple
from backend.SudokuTechniques.PointingCells import PointingCells

class SudokuHints:
    '''
    This class applies different techniques within Sudoku to find the answer 
    to a cell.  
    '''

    def __init__(self, grid):
        '''
        Constructor for the class. 

        Paramaters:
        grid - a 2D array containing the puzzle. 
        '''
        self.grid = grid

        # converts the puzzle into the correct form.
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == '-':
                    self.grid[i][j] = 0
                else:
                    self.grid[i][j] = int(self.grid[i][j])

        domain = Domain(self.grid)
        self.domains = domain.getAllDomains()



    def getNextHint(self):
        '''
        Attemptes to apply different techniques to the sudoku puzzle to get the user a better hint.

        Returns:
        An array containing all the techniques used to get the hint. None is techniques could not be 
        applied.
        '''
        output = []
        while True:
            domain, ObviousSingle = ObviousSinglePairTriple.checkObviousSingle(self.domains)
            if domain != None:
                self.domain = domain
                output.append(ObviousSingle)
                break
            domain, ObviousPair = ObviousSinglePairTriple.checkObviousPairs(self.domain)
            if domain != None:
                self.domain = domain
                output.append(ObviousPair)
                continue
            domain, ObviousTriple = ObviousSinglePairTriple.checkObviousTriple(self.domain)
            if domain != None:
                self.domain = domain
                output.append(ObviousTriple)
                continue
            domain, HiddenSingle = HiddenSinglePairTriple.checkHiddenSingles(self.domain)
            if domain != None:
                self.domain = domain
                output.append(HiddenSingle)
                continue
            domain, HiddenPair = HiddenSinglePairTriple.checkHiddenPair(self.domain)
            if domain != None:
                self.domain = domain
                output.append(HiddenPair)
                continue
            domain, HiddenTriple = HiddenSinglePairTriple.checkHiddenTriple(self.domain)
            if domain != None:
                self.domain = domain
                output.append(HiddenTriple)
                continue
            domain, PointingCells = PointingCells.checkPointingCells(self.domain)
            if domain != None:
                self.domain = domain
                output.append(PointingCells)
                continue
            return "No technique applied"

        return output
            
            

