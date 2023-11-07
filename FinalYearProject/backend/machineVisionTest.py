from puzzleExtraction import PuzzleExtraction
from NumberRecognition import NumberRecognition
import cv2
#from KillerSudokuExtraction import KillerSudokuExtraction

a = PuzzleExtraction(cv2.imread(".\MachineVisionImages\sudoku5.jpg"))
print(a.ConvertToArray())