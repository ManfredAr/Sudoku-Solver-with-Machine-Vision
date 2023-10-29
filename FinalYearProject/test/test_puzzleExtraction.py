from backend.puzzleExtraction import PuzzleExtraction
import unittest  
import numpy as np

class Test_PuzzleExtraction(unittest.TestCase):

    # testing that the constructor is instantiated properly
    def test_Preprocess(self):
        num = PuzzleExtraction(".\MachineVisionImages\Sudoku3.jpg")
        self.assertEqual(num.image, ".\MachineVisionImages\Sudoku3.jpg")

    # testing the image is resized properly
    def test_ResizeImage(self):
        num = PuzzleExtraction(".\MachineVisionImages\Sudoku3.jpg")
        img = np.zeros((2000,2000,1))
        returnedImage = num.resizeImage(img)
        self.assertEqual((1000,1000), returnedImage.shape)

    # Testing a straightened Image is of height and width 450
    def test_straightenImage(self):
        num = PuzzleExtraction(".\MachineVisionImages\Sudoku3.jpg")
        processedImage = num.ConvertAndCrop()
        edgePoints = num.getBorder(processedImage)
        straightenedImage = num.straightenImage(processedImage, edgePoints)
        self.assertEqual((450,450), straightenedImage.shape)

    # Testing that after cell extraction there are 81 images
    def test_cellExtraction(self):
        num = PuzzleExtraction(".\MachineVisionImages\Sudoku3.jpg")
        processedImage = num.ConvertAndCrop()
        edgePoints = num.getBorder(processedImage)
        straightenedImage = num.straightenImage(processedImage, edgePoints)
        cells = num.CellExtraction(straightenedImage)
        self.assertEqual(81, len(cells))

    # testing that a contour in the center of the image returns True
    def test_TrueCentered(self):
        num = PuzzleExtraction(".\MachineVisionImages\Sudoku3.jpg")
        # A box which overlaps the center box.
        self.assertEqual(True, num.isCentered(1, 1, 40, 40))

    # testing that a contour not in the center of the image returns False
    def test_FalseCentered(self):
        num = PuzzleExtraction(".\MachineVisionImages\Sudoku3.jpg")
        # A box which does not overlaps the center box.
        self.assertEqual(False, num.isCentered(1, 1, 2, 2))