import cv2
import numpy as np

class PuzzleExtraction:

    def __init__(self, image):
        self.image = image


    def ConvertAndCrop(self):
        image = cv2.imread(self.image, cv2.IMREAD_GRAYSCALE)
        # the block size to process the image
        block_size = 92

        # creating a new image which is black.
        bin_image = np.zeros_like(image)

        # Iterate through the image in blocks
        for y in range(0, image.shape[0], block_size):
            for x in range(0, image.shape[1], block_size):
                #Getting a block from the original image
                block = image[y:y + block_size, x:x + block_size]

                # applying adaptive threshold to the block
                threshold = cv2.adaptiveThreshold(block, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 0)

                # Placing the block in the corresponding place in the new image.
                bin_image[y:y + block_size, x:x + block_size] = threshold


        self.displayImage(bin_image)

    
    def displayImage(self, image):
        cv2.imshow("puzzle", image)
        cv2.waitKey(0)