from backend.KSudokuDomain import KillerSudokuDomain

class KillerSudokuHints:

    def __init__(self, killerSudoku):
        self.grid = killerSudoku.grid
        self.cages = killerSudoku.cages
        self.killerSudoku = killerSudoku
        self.domain = KillerSudokuDomain(killerSudoku)
        self.domainGrid = self.domain.getAllDomains()