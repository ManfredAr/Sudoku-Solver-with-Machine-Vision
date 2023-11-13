from SudokuExtraction import SudokuExtraction
from NumberRecognition import NumberRecognition
import cv2
#from KillerSudokuExtraction import KillerSudokuExtraction

a = SudokuExtraction(".\MachineVisionImages\Sudoku2.png")
print(a.convertToArray())