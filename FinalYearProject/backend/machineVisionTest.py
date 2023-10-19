from puzzleExtraction import PuzzleExtraction

test = PuzzleExtraction(".\MachineVisionImages\sudoku3.jpg")
a = test.getCells()

count = 0
for i in range(len(a)):
    if a[i] is not None and a[i].any():
        count += 1

print(count)