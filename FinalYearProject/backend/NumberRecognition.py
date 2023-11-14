import math
import keras
import cv2
import numpy as np
from scipy import ndimage

class NumberRecognition:
    '''
    This class is responsible for classifying images of number to its corresponding integer.

    The preprocesses steps were used from the website:
    https://mkdev.me/posts/fundamentals-of-front-end-django
    '''

    def __init__(self):
        '''
        Constructor for the class, it instantiates the trained model so it can make predictions.
        '''
        self.model = keras.models.load_model("backend/newModel.h5")

    def ConvertToArray(self, arr):
        '''
        Runs all images through the model to get the predictions.

        Parameters:
        arr - the array containing image to be classified.
        '''
        for i in range(len(arr)):
            if not np.array_equal(arr[i], -1):               
                processedImages = self.preprocess(arr[i])
                img = processedImages.reshape((1, 28, 28, 1))
                prediction = self.model.predict(img)
                arr[i] = prediction.argmax()
            else:
                arr[i] = 0

        # converting the 1D array to a 2D array and returning it.
        return [arr[i:i+9] for i in range(0, len(arr), 9)]
    

    def ConvertToDigit(self, arr):
        '''
        Runs all images through the model to get the predictions.

        Parameters:
        arr - the array containing image to be classified.
        '''
        pred_arr = []
        for i in range(len(arr)):
            gray_image = cv2.cvtColor(arr[i], cv2.COLOR_BGR2GRAY)
            processedImages = self.preprocess(gray_image)
            img = processedImages.reshape((1, 28, 28, 1))
            prediction = self.model.predict(img)
            pred_arr.append(int(prediction.argmax()))

        return pred_arr


    def preprocess(self, image):
        '''
        Resizes the image of the number to fit in a 20x20 canvas and then
        center the image in a 28x28 canvas as defined by the MNIST dataset.

        Parameters:
        image - the image to be processed

        Returns:
        The processed image. 

        '''
        image = image / 255.0
        image = 1 - image

        rows = image.shape[0]
        cols = image.shape[1]

        # fitting the image in a 20x20 box.
        if rows > cols:
            factor = 20.0/rows
            rows = 20
            cols = int(round(cols*factor))
            image = cv2.resize(image, (cols,rows))
        else:
            factor = 20.0/cols
            cols = 20
            rows = int(round(rows*factor))
            image = cv2.resize(image, (cols, rows))

        # padding the image to get it in a 28x28 shape.
        colsPadding = (int(math.ceil((28-cols)/2.0)),int(math.floor((28-cols)/2.0)))
        rowsPadding = (int(math.ceil((28-rows)/2.0)),int(math.floor((28-rows)/2.0)))
        image = np.lib.pad(image,(rowsPadding,colsPadding),'constant')

        shiftx, shifty = self.getBestShift(image)

        return self.shift(image, shiftx, shifty)
    

    def getBestShift(self, img):
        '''
        Finds the x and y shifts for the image which is needed to center it.

        Parameters:
        A image which is 28x28

        Returns:
        The X and Y shifts.
        '''
        centerY, centerX = ndimage.center_of_mass(img)

        rows,cols = img.shape
        shiftx = np.round(cols/2.0-centerY).astype(int)
        shifty = np.round(rows/2.0-centerX).astype(int)

        return shiftx,shifty
    

    def shift(self, img, sx, sy):
        '''
        Performs the shift on the image to center in within the background.

        Parameters:
        img - a 28x28 image
        sx - the x shift 
        sy - the y shift

        returns:
        A centered image 
        '''
        rows,cols = img.shape
        matrix = np.float32([[1,0,sx],[0,1,sy]])
        centeredImage = cv2.warpAffine(img, matrix, (cols,rows))
        return centeredImage
