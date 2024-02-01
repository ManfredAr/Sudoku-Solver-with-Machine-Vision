from backend.SudokuExtraction import SudokuExtraction  
import unittest  
import cv2
import numpy as np

class Test_SudokuExtractor(unittest.TestCase):

    # testing the images are resized properly.
    def test_testResized(self):
        image = cv2.imread("MachineVisionImages/Sudoku7.jpg")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        extract = SudokuExtraction(image)

        self.assertLessEqual(len(extract.resizeImage(image)), 1000)
        self.assertLessEqual(len(extract.resizeImage(image)[0]), 1000)

    
    # testing that getBorder returns 4 points (cannot check if they are correct through code)
    def test_getBorder(self):
        image = cv2.imread("MachineVisionImages/Sudoku7.jpg")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        threshold = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 0)
        extract = SudokuExtraction(threshold)
        extract.image_copy = threshold
        self.assertEqual(len(extract.getBorder(threshold)[0]), 4)


    # testing that the points are sorted corerctly.
    def test_sortPoints(self):
        image = cv2.imread("MachineVisionImages/Sudoku7.jpg")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        threshold = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 0)
        extract = SudokuExtraction(threshold)
        extract.image_copy = threshold
        a, b = extract.getBorder(threshold)
        self.assertEqual((extract.sortPoints(a).reshape(4,2)==np.array([[  75,  216],[ 934,  209],[ 954, 1079],[  91, 1074]])).all(), True)


    # testing that cell extract returns 81 images.
    def test_cellExtraction(self):
        image = cv2.imread("MachineVisionImages/Sudoku7.jpg")
        extract = SudokuExtraction(image)
        self.assertEqual(len(extract.cellExtraction(image)), 81)

    # testing that a centered contour returns true
    def test_isCentered(self):
        image = cv2.imread("MachineVisionImages/Sudoku7.jpg")
        extract = SudokuExtraction(image)
        self.assertEqual(extract.isCentered(15, 15, 20, 20), True)


    # testing that an uncentered contour returns false.
    def test_isNotCentered(self):
        image = cv2.imread("MachineVisionImages/Sudoku7.jpg")
        extract = SudokuExtraction(image)
        self.assertEqual(extract.isCentered(0, 0, 10, 10), False)