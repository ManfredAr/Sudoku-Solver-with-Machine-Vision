from KillerSudokuExtraction import KillerSudokuExtraction
from NumberRecognition import NumberRecognition
import cv2
#from KillerSudokuExtraction import KillerSudokuExtraction

a = KillerSudokuExtraction(".\MachineVisionImages\Ksudoku1.jpg")
print(a.convertToPuzzle())