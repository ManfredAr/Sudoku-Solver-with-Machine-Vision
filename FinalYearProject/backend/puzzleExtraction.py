import cv2
import numpy as np

class PuzzleExtraction:
    '''
    This class is responsible for the processing of an image to extract the individual
    cells of the puzzle. 
    '''

    def __init__(self, image):
        '''
        A constructor method for instantiating the class

        parameters:
        image - the image which will be processed
        '''
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
        straightenedImage = self.straightenImage(img_dilation, edgePoints)
        return self.CellExtraction(straightenedImage)


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
        '''
        Givens the corners of the puzzle, it resizes the puzzle as need to fit in a 
        450x450 box. 

        Parameters:
        processedImage - A grayscale image 
        edges - an array containing the edge points of the puzzle.

        Returns:
        An image which has been straightened.
        '''

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

        return output


    def CellExtraction(self, image):   
        '''
        Extracts all the cells from the image 

        Parameters:
        image - A straighted image of the puzzle

        Returns:
        An array containing the cells in the image.
        '''

        # defining the height and width for each cell      
        cell_height = 450 // 9
        cell_width = 450 // 9

        cells = []

        # looping through each cell in the image.
        for y in range(0, 450, cell_height):
            for x in range(0, 450, cell_width):
                # getting each 50x50 block from the image
                block = image[y:y+cell_height, x:x+cell_width]
                
                # Appending the extracted block to the cells array
                cells.append(block)

        return cells


    def displayImage(self, image):
        '''
        displays the image on the screen

        parameters:
        image - the image to be displayed.
        '''
        cv2.imshow("puzzle", image)
        cv2.waitKey(0)