from backend.NumberRecognition import NumberRecognition
import unittest   # The test framework
import numpy as np

class Test_NumberRecognition(unittest.TestCase):

    # testing that the preprocess step returns a 28x28 image
    def test_Preprocess(self):
        num = NumberRecognition()
        processedImg = num.preprocess(np.array([[0,0], [1,1]]))
        self.assertEqual(processedImg.shape, (28,28))