import cv2
import numpy as np
from PIL import Image
from puzzleExtraction import PuzzleExtraction

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
        straightenedImage = self.straightenImage(processedImage, edgePoints)
        cells = self.CellExtraction(straightenedImage)



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

        # creating a 990 by 990 template image
        dst = np.array([[0, 0], [990, 0], [990, 990], [0, 990]], dtype='float32')

        # Calculate the perspective transformation matrix
        M = cv2.getPerspectiveTransform(edgePoints, dst)

        # Apply the perspective transformation to the image
        output = cv2.warpPerspective(processedImage, M, (990, 990))

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
        cell_height = 990 // 9
        cell_width = 990 // 9
        print(image.shape)
        cells = []

        # Loop through each cell in the image.
        for y in range(0, 990, cell_height):
            for x in range(0, 990, cell_width):
                # Get each 110x110 block from the image
                block = image[y:y+cell_height, x:x+cell_width]
                
                # Append the extracted block to the cells array
                cells.append(block)

        return cells