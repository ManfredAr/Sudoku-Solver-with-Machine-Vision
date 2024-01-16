from backend.domain import Domain
from backend.KillerSudoku import KillerSudoku
from backend.KSudokuDomain import KillerSudokuDomain
from backend.SudokuTechniques.HiddenSinglePairTriple import HiddenSinglePairTriple
from backend.SudokuTechniques.ObviousSinglePairTriple import ObviousSinglePairTriple
from backend.SudokuTechniques.PointingCells import PointingCells
from backend.SudokuTechniques.ruleOf45 import ruleOf45

class KillerSudokuHints:
    '''
    This class applies different techniques within Sudoku to find the answer 
    to a cell.  
    '''

    def __init__(self, grid, cage):
        '''
        Constructor for the class. 

        Paramaters:
        grid - a 2D array containing the puzzle. 
        '''
        self.grid = grid
        self.cage = cage

        # converts the puzzle into the correct form.
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == '-':
                    self.grid[i][j] = 0
                else:
                    self.grid[i][j] = int(self.grid[i][j])

        domain = KillerSudokuDomain(KillerSudoku(self.grid, self.cage))
        self.domains = domain.getAllDomains()
        self.ObviousSinglePairTriple = ObviousSinglePairTriple()
        self.HiddenSinglePairTriple = HiddenSinglePairTriple()
        self.PointingCells = PointingCells()
        self.ruleOf45 = ruleOf45()



    def getNextHint(self):
        '''
        Attemptes to apply different techniques to the sudoku puzzle to get the user a better hint.

        Returns:
        An array containing all the techniques used to get the hint. None is techniques could not be 
        applied.
        '''
        output = []
        while True:
            domain, info, ObviousSingle = self.ObviousSinglePairTriple.checkObviousSingle(self.domains)
            if domain != None:
                self.domain = domain
                output.append(ObviousSingle)
                output.append(info)
                break
            domain, ObviousPair = self.ObviousSinglePairTriple.checkObviousPairs(self.domains)
            if domain != None:
                if ObviousPair not in output:
                    self.domain = domain
                    output.append(ObviousPair)
                    continue
            domain, ObviousTriple = self.ObviousSinglePairTriple.checkObviousTriples(self.domains)
            if domain != None:
                if ObviousTriple not in output:
                    self.domain = domain
                    output.append(ObviousTriple)
                    continue
            domain, HiddenSingle = self.HiddenSinglePairTriple.checkHiddenSingles(self.domains)
            if domain != None:
                if HiddenSingle not in output:
                    self.domain = domain
                    output.append(HiddenSingle)
                    continue
            domain, HiddenPair = self.HiddenSinglePairTriple.checkHiddenPair(self.domains)
            if domain != None:
                if HiddenPair not in output:
                    self.domain = domain
                    output.append(HiddenPair)
                    continue
            domain, HiddenTriple = self.HiddenSinglePairTriple.checkHiddenTriple(self.domains)
            if domain != None:
                if HiddenTriple not in output:
                    self.domain = domain
                    output.append(HiddenTriple)
                    continue
            domain, PointingCells = self.PointingCells.checkPointingCells(self.domains)
            if domain != None:
                if PointingCells not in output:
                    self.domain = domain
                    output.append(PointingCells)
                    continue
            domain, ruleOf45 = self.ruleOf45.checkRuleOf45(self.domains)
            if domain != None:
                if ruleOf45 not in output:
                    self.domain = domain
                    output.append(ruleOf45)
                    continue
            return -1
        return output
            
            

