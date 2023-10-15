import time
from killerSudokuSolver import KillerSudokuSolver
from killerSudokuSolver2 import KillerSudokuSolver2
from KillerSudoku import KillerSudoku
from heap import heap

grid = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

cages = {
    1 : { 12 : [(0,0), (1,0),(2,0)]},
    2 : { 7 : [(0,1), (0,2)]},
    3 : { 14 : [(0,3), (0,4), (0,5)]},
    4 : { 16 : [(0,6), (1,6), (2,6)]},
    5 : { 9 : [(0,7), (1,7), (2,7)]},
    6 : { 13 : [(0,8), (1,8)]},

    7 : { 15 : [(1,1), (1,2)]},
    8 : { 15 : [(1,3), (1,4)]},
    9 : { 7 : [(1,5), (2,5)]},

    10 : { 17 : [(2,1), (2,2), (3,2)]},
    11 : { 10 : [(2,3), (3,3), (4,3)]},
    12 : { 14 : [(2,4), (3,4), (4,4)]},
    13 : { 7 : [(2,8)]},

    14 : { 10 : [(3,0), (3,1)]},
    15 : { 3 : [(3,5)]},
    16 : { 12 : [(3,6), (3,7)]},
    17 : { 14 : [(3,8), (4,7), (4,8)]},

    18 : { 22 : [(4,0), (4,1), (5,0), (5,1)]},
    19 : { 24 : [(4,2), (5,2), (6,2), (7,2), (7,3)]},
    20 : { 14 : [(4,5), (4,6)]},

    21 : { 9 : [(5,3), (6,3)]},
    22 : { 12 : [(5,4), (6,4)]},
    23 : { 7 : [(5,5), (6,5)]},
    24 : { 12 : [(5,6), (5,7)]},
    25 : { 19 : [(5,8), (6,6), (6,7), (6,8), (7,7)]},
    
    26 : { 9 : [(6,0)]},
    27 : { 15 : [(6,1), (7,0), (7,1)]},

    28 : { 17 : [(7,4), (8,2), (8,3), (8,4)]},
    29 : { 17 : [(7,5), (7,6), (8,5)]},
    30 : { 13 : [(7,8), (8,8)]},

    31 : { 7 : [(8,0), (8,1)]},
    32 : { 13 : [(8,6), (8,7)]},
}


a = KillerSudokuSolver(KillerSudoku(grid, cages))
start = time.time()
print(a.solver())
end = time.time()
print(end - start)