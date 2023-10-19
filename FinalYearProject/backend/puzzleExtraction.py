import cv2
import numpy as np

class PuzzleExtraction:

    def __init__(self, image):
        self.image = image


    def ConvertAndCrop(self):
        '''
        Converts the image to a grayscale image and run some noise reduction methods.  
        '''
        image = cv2.imread(self.image)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # applying adaptive threshold to the block
        threshold = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 0)

        # a window size for erosion and dilation to be applied
        kernel = np.ones((2, 2), np.uint8) 
        
        # applying erosion and dialation
        img_erosion = cv2.erode(threshold, kernel) 
        img_dilation = cv2.dilate(img_erosion, kernel) 

        edgePoints = self.getBorder(img_dilation)
        self.straightenImage(img_dilation, edgePoints)


    def getBorder(self, ProcessedImage):
        '''
        takes an image and tries to find the corners which the puzzle is bounded by.

        Parameters:
        The image to find the contours for.

        Returns:
        An array containing the edges of the puzzle. 
        '''

        # finds the contours in the image
        contours, hierarchy = cv2.findContours(ProcessedImage.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # sorting the contours by areas
        cnt = sorted(contours, key=cv2.contourArea, reverse=True)

        # The second contour in the puzzle the first is the border of the image.
        puzzleContour = cnt[1]

        # ep calculates the precision of the approxPolyDP method
        ep = 0.02 * cv2.arcLength(puzzleContour, True)

        # gets the corners of the puzzle.
        edgePoints = cv2.approxPolyDP(puzzleContour, ep, True)

        return edgePoints
    

    def straightenImage(self, processedImage, edges):

        # getting the array in the correct format.
        edgePoints = np.zeros((4, 1, 2), dtype=np.float32)
        for i in range(4):
            edgePoints[i][0] = edges[i]

        # creating a 450 by 450 template image
        dst = np.array([[0, 0], [450, 0], [450, 450], [0, 450]], dtype='float32')

        # Calculate the perspective transformation matrix
        M = cv2.getPerspectiveTransform(edgePoints, dst)

        # Apply the perspective transformation to the image
        output = cv2.warpPerspective(processedImage, M, (450, 450))

        self.displayImage(output)

    def displayImage(self, image):
        cv2.imshow("puzzle", image)
        cv2.waitKey(0)