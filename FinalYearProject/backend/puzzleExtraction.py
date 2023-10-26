import cv2
import numpy as np
from PIL import Image

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

    
    def getCells(self):
        processedImage = self.ConvertAndCrop()
        edgePoints = self.getBorder(processedImage)
        straightenedImage = self.straightenImage(processedImage, edgePoints)
        cells = self.CellExtraction(straightenedImage)
        final_arr = self.processCells(cells)
        return final_arr
    

    def ConvertAndCrop(self):
        '''
        Converts the image to a grayscale image and run some noise reduction methods.  
        '''
        image = cv2.imread(self.image)

        # some images give an EXIF orientation tag
        # which causes incorrect rotation in images
        # This fixes the rotation problem.
        try:
            with Image.open(self.image) as img:
                exif = img._getexif()
                if exif is not None and 274 in exif:
                    orientation = exif[274]
                    if orientation == 3:
                        image = cv2.rotate(image, cv2.ROTATE_180)
                    elif orientation == 6:
                        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
                    elif orientation == 8:
                        image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        except Exception:
            pass

        if image.shape[0] > 1000 and image.shape[1] > 1000:
            image = self.resizeImage(image)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # applying adaptive threshold to the block
        threshold = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 0)

        return threshold
    
    def resizeImage(self, image):
        '''
        Resizes the image to fit in a 1000x1000 frame

        Parameters:
        the image to be resized.

        Returns:
        The resized image
        '''

        # defining max sizes for image
        max_width = 1000
        max_height = 1000

        height, width, _ = image.shape

        # Calculate the scale factors
        width_scale = max_width / width
        height_scale = max_height / height
        factor = min(width_scale, height_scale)

        # Resize the image with the calculated scale factor
        return cv2.resize(image, None, fx=factor, fy=factor, interpolation=cv2.INTER_AREA)


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
    

    def processCells(self, cells):
        '''
        Processes the images to find out which cells contain a digit and which do not.

        Parameters:
        cells - An array containing the cells to be processed

        Returns:
        An array containing only the cells with digits.
        '''

        digit_Cells = []

        for i in range(len(cells)):
            # Cropping the image by 2 pixels on each side.
            new_height = 50 - 2 * 2
            new_width = 50 - 2 * 2
            cropped_image = cells[i][2:2 + new_height, 2:2 + new_width]

            contours, _ = cv2.findContours(cropped_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            # Only process cells with more than one contour.
            if len(contours) > 1:
                cnt = sorted(contours, key=cv2.contourArea, reverse=True)

                # check if the contour is centered and the right size for a digit.
                x, y, w, h = cv2.boundingRect(cnt[1])
                if h >= 46 // 2 and self.isCentered(x, y, w, h) == True:
                    digit_Cells.append(cropped_image[y:y + h, x:x + w])
                else:
                    digit_Cells.append(-1)
            else:
                digit_Cells.append(-1)


        return digit_Cells

    def isCentered(self, x1, y1, w1, h1):
        '''
        Checking if the given contour is centered or not

        Parameters:
        x1 - x coordinate of contour
        y1 - y cooridnate of contour
        w1 - width of the contour
        h1 - hight of the contour

        Returns:
        True if centered false otherwise.
        '''

        # defining the center to be 15 x 15
        x2, y2, w2, h2 = 15, 15, 15, 15

        # Calculate the right and bottom coordinates of each rectangle
        right1, bottom1 = x1 + w1, y1 + h1
        right2, bottom2 = x2 + w2, y2 + h2

        # Checking if there is an overlap
        if (x1 > right2) or (x2 > right1):
            return False 
        if (y1 > bottom2) or (y2 > bottom1):
            return False

        return True