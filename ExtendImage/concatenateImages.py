import numpy as np
import cv2

class ConcatenateImages:
    def __init__(self, imgpath1, imgpath2, imgpath3, imgpath4):
        self.img1 = cv2.imread(imgpath1)
        self.img2 = cv2.imread(imgpath2)
        self.img3 = cv2.imread(imgpath3)
        self.img4 = cv2.imread(imgpath4)

    def concatenate(self):
        step1 = np.concatenate((self.img1, self.img2), axis = 1)
        step2 = np.concatenate((self.img3, self.img4), axis = 1)
        res = np.concatenate((step1, step2), axis = 1)
        return res