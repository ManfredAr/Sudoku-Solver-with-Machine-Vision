import cv2
import numpy as np
from backend.SudokuExtraction import SudokuExtraction
from backend.NumberRecognition import NumberRecognition


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
        self.extraction = SudokuExtraction(image)
        self.digitRecognition = NumberRecognition()

    
    def convertToPuzzle(self):
        '''
        Converts the image of the puzzle into the grid and the cages.

        Returns the grid and the dictionary containing the cages.
        '''
        processedImage = self.extraction.convertAndCrop()
        edgePoints, image = self.extraction.getBorder(processedImage)
        self.image = image
        straightenedImage, original = self.straightenImage(processedImage, edgePoints)
        cells, cageSums = self.cellExtraction(straightenedImage, original)
        cages = self.getPuzzle(cells, cageSums)
        self.cages = [cages[i:i+9] for i in range(0, len(cages), 9)]
        cages = self.constructCages()

        grid = [["-","-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-","-"], 
                ["-","-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-","-"],                
                ["-","-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-","-"],                
                ["-","-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-","-"],                
                ["-","-","-","-","-","-","-","-","-"]]


        return grid, cages

    def constructCages(self):
        '''
        Constructs the cages found withing the puzzle. 

        Returns:
        A dictionary with the key being the cage number, the value is 
        another dictionary with the sum being the key and the value
        being an array containing the cage cells. 
        '''
        cages = {}
        counter = 0
        for i in range(len(self.cages)):
            for j in range(len(self.cages[i])):
                if self.cages[i][j][5] != 1:
                    cells = self.constructCage(i, j)
                    cages[counter] = {self.cages[i][j][0] : cells}
                    counter += 1
        return cages


    def constructCage(self, i, j):
        '''
        A recusive algorithm to find all the cells which are in the same cage.

        Parameters:
        i - the row of the cell
        j - the column of the cell

        Returns:
        An array containing the cells in the same cage.
        '''
        cageCells = [(i, j)]
        cell = self.cages[i][j]
        if cell[5] == 1:
            return []
        self.cages[i][j][5] = 1
        if cell[2] == 0:
            cageCells = cageCells + self.constructCage(i+1, j)
        if cell[3] == 0:
            cageCells = cageCells + self.constructCage(i, j+1)
        if cell[1] == 0:
            cageCells = cageCells + self.constructCage(i, j-1)
        return cageCells
        



    def getPuzzle(self, cells, cageSums):
        '''
        Determines the cage borders for each cell as well as if it contains
        the cage sum.

        Parameters:
        cells - all 81 images of cells, one for each cell
        cageSums - the images of the top left of the cell where the cage sum is usually located.

        Returns:
        A 2D array containing a sub array in the format, cageSum (-1 if not cageSum),
        left, bottom, right and checked 
        '''
        grid = []
        for i in range(len(cells)):
            current_cell = [0,0,0,0,0,0]
            cell_sum = self.isCageSumCell(cageSums[i])
            if cell_sum == -1:
                current_cell[0] = -1
            else:
                current_cell[0] = cell_sum
                current_cell[1], current_cell[4] = 1, 1

            sides = self.getCageSides(cells[i])
            for j in range(len(sides)):
                if sides[j] > 3:
                    current_cell[j+1] = 1
            grid.append(current_cell)
        return grid



    def getCageSides(self, cell):
        '''
        Determines which side the borders of the cage is in the cell.

        Parameters:
        cell - the cell to be checked.

        Returns:
        An array in the format left, bottom, right, and top
        each index with the number of contours found on that side.
        '''

        margin = 20
        #left, bottom, right, top
        sides = [0, 0, 0, 0] 
        contours, hierarchy = cv2.findContours(cell.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)   
        for contour in contours:
            # get the bounding rectangle of the contour
            x, y, w, h = cv2.boundingRect(contour)

            # calculate the center of the bounding rectangle
            center_x = x + w // 2
            center_y = y + h // 2
            
            # check if the center is within the specified margin of the sides
            if center_x < margin and x > 0:
                sides[0] += 1
            elif center_x > 110 - margin and x + w < 110:
                sides[2] += 1
            
            if center_y < margin and y > 0:
                sides[3] += 1
            elif center_y > 110 - margin and y + h < 110:
                sides[1] += 1

        return sides

        


    def isCageSumCell(self, cell):
        '''
        Checks whether the cell contains the sum of the cage.

        parameters:
        cell - the cell to be checked.

        Returns: 
        The cage sum if it exists or -1 otherwise.
        '''

        # improving the image resolution
        high_res = cv2.detailEnhance(cell, sigma_s=15, sigma_r=0.7)
        gray = cv2.cvtColor(high_res, cv2.COLOR_BGR2GRAY)
        #blurred = cv2.GaussianBlur(gray, (3,3), 0)
        canny = cv2.Canny(gray, 160, 255, 1)
        contours, hierarchy = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnt = sorted(contours, key=cv2.contourArea, reverse=True)
        sums = []
        current_x = 0

        # getting the 2 largest contours in the case of double digit numbers
        for j in range(2):
            x, y, w, h = cv2.boundingRect(cnt[j])
            roi = cell[y:y+h, x:x+w]
            canvas = np.zeros_like(roi)
            canvas[:h, :w] = roi
            # filtering contours with are not digits
            if w * h > 80 and w * h < 1500 and  h < 40 and w < 40:
                if len(sums) == 0:
                    sums.append(canvas)
                    current_x = x
                else:
                    if x < current_x:
                        sums.insert(0, canvas)
                    else:
                        sums.append(canvas)

        if len(sums) == 0:
            return -1
        
        # returning the number
        cageSum = self.digitRecognition.ConvertToDigit(sums)
        cageSum = ''.join(map(str, cageSum))
        return int(cageSum) 
            



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
        image = self.image
        
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
    


    def cellExtraction(self, image, original):   
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