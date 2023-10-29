from backend.KillerSudokuExtraction import KillerSudokuExtraction
import unittest 

class Test_PuzzleExtraction(unittest.TestCase):

    # testing that the constructor is instantiated properly
    def test_Preprocess(self):
        num = KillerSudokuExtraction(".\MachineVisionImages\Ksudoku1.jpg")
        self.assertEqual(num.image, ".\MachineVisionImages\Ksudoku1.jpg")

    # Testing a straightened Image is of height and width 990
    def test_straightenImage(self):
        num = KillerSudokuExtraction(".\MachineVisionImages\Ksudoku1.jpg")
        processedImage = num.extraction.ConvertAndCrop()
        edgePoints = num.extraction.getBorder(processedImage)
        straightenedImage, original = num.straightenImage(processedImage, edgePoints)
        self.assertEqual((990,990), straightenedImage.shape)

    # Testing CellExtraction returns 2 sets of 81 images
    # The second set of images should be coloured  
    def test_cellExtraction(self):
        num = KillerSudokuExtraction(".\MachineVisionImages\Ksudoku1.jpg")
        processedImage = num.extraction.ConvertAndCrop()
        edgePoints = num.extraction.getBorder(processedImage)
        straightenedImage, original = num.straightenImage(processedImage, edgePoints)
        cells, cageSums = num.CellExtraction(straightenedImage, original)
        self.assertEqual(len(cells), 81)
        self.assertEqual(len(cageSums), 81)
        self.assertEqual(cageSums[0].shape, (50,50,3))


    # testing that for a puzzle with 33 cages, the dictionary of cages returned is of length 33
    def test_convertToPuzzle(self):
        num = KillerSudokuExtraction(".\MachineVisionImages\Ksudoku1.jpg")
        grid, cages = num.ConvertToPuzzle()
        self.assertEqual(len(cages), 33)

