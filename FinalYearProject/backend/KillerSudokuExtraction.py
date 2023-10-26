import cv2
import numpy as np
from PIL import Image
from puzzleExtraction import PuzzleExtraction
import imutils


class KillerSudokuExtraction:
    '''
    This class is responsible for the processing killer Sudoku images.
    '''

    def __init__(self, image):
        '''
        A constructor method for instantiating the class

        parameters:
        image - the image which will be processed
        '''
        self.image = image
        self.extraction = PuzzleExtraction(image)

    
    def ExtractCells(self):
        processedImage = self.extraction.ConvertAndCrop()
        edgePoints = self.extraction.getBorder(processedImage)
        straightenedImage, original = self.straightenImage(processedImage, edgePoints)
        cells, cageSums = self.CellExtraction(straightenedImage, original)
        self.isCageSumCell(cageSums)


    def isCageSumCell(self, cells):

        for i in range(len(cells)):
            high_res = cv2.detailEnhance(cells[i], sigma_s=15, sigma_r=0.7)
            gray = cv2.cvtColor(high_res, cv2.COLOR_BGR2GRAY)
            #blurred = cv2.GaussianBlur(gray, (3,3), 0)
            canny = cv2.Canny(gray, 70, 255, 1)
            contours, hierarchy = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = sorted(contours, key=cv2.contourArea, reverse=True)
            
            for j in range(2):
                x, y, w, h = cv2.boundingRect(cnt[j])
                roi = cells[i][y:y+h, x:x+w]
                canvas = np.zeros_like(roi)
                canvas[:h, :w] = roi
                if w * h > 80 and w * h < 1500 and  h < 40 and w < 40:
                    print(i)
                    cv2.imshow('h', canvas)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
            



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
        image = cv2.imread(self.image)
        if image.shape[0] > 1000 and image.shape[1] > 1000:
            image = self.extraction.resizeImage(image)

        edgePoints = np.zeros((4, 1, 2), dtype=np.float32)
        for i in range(4):
            edgePoints[i][0] = edges[i]

        # creating a 990 by 990 template image
        dst = np.array([[0, 0], [990, 0], [990, 990], [0, 990]], dtype='float32')

        # Calculate the perspective transformation matrix
        M = cv2.getPerspectiveTransform(edgePoints, dst)

        # Apply the perspective transformation to the image
        output1 = cv2.warpPerspective(processedImage, M, (990, 990))
        output2 = cv2.warpPerspective(image, M, (990, 990))

        return output1, output2
    


    def CellExtraction(self, image, original):   
        '''
        Extracts all the cells from the image 

        Parameters:
        image - A straighted image of the puzzle

        Returns:
        An array containing the cells in the image.
        '''

        # defining the height and width for each cell      
        cell_height = 990 // 9
        cell_width = 990 // 9
        cells = []
        original_cells = []

        # Loop through each cell in the image.
        for y in range(0, 990, cell_height):
            for x in range(0, 990, cell_width):
                # Get each 110x110 block from the image
                block = image[y:y+cell_height, x:x+cell_width]
                
                # Append the extracted block to the cells array
                cells.append(block)

                original_cells.append(original[y:y+50, x:x+50])

        return cells, original_cells