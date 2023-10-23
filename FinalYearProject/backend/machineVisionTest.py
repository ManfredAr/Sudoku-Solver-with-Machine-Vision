from puzzleExtraction import PuzzleExtraction
from NumberRecognition import NumberRecognition

b = NumberRecognition()
test = PuzzleExtraction(".\MachineVisionImages\sudoku5.jpg")
a = test.getCells()
print(a)

print(b.CovertToArray(a))