from SudokuExtraction import SudokuExtraction
from NumberRecognition import NumberRecognition
import cv2
#from KillerSudokuExtraction import KillerSudokuExtraction

a = SudokuExtraction(".\MachineVisionImages\Sudoku6.jpg")
print(a.convertToArray())