import cv2
import time
import numpy as np

class ExtendImage:
    """
    Class for extending and displaying images to both dual and quadro monitors.

    Args:
        imagepat1 (str): The first image path.
        imagepat2 (str): The second image path.
        imagepat3 (str): The third image path.
        imagepat4 (str): The fourth image path.
    """
    def __init__(self, imgpath1, imgpath2, imgpath3, imgpath4):
        self.img1 = cv2.imread(imgpath1)
        self.img2 = cv2.imread(imgpath2)
        self.img3 = cv2.imread(imgpath3)
        self.img4 = cv2.imread(imgpath4)

    def twobytwo(self):
            """ Method for displaying four images on quadro monitor that aligned two horizontal and two vertical"""
            cv2.namedWindow("window1", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("window1",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.imshow("window1", self.img1)

            cv2.namedWindow("window2", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("window2",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.imshow("window2", self.img2)
            cv2.moveWindow("window2", 1920, 0)

            cv2.namedWindow("window3", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("window3",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.imshow("window3", self.img3)
            cv2.moveWindow("window3", 0, 1080)

            cv2.namedWindow("window4", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("window4",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.imshow("window4", self.img4)
            cv2.moveWindow("window4", 1920, 1080)
            cv2.waitKey(0)

    def fourhorizontal(self):
        """ Method for displaying four images on quadro monitor that aligned four horizontal"""
        cv2.namedWindow("window1", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window1",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow("window1", self.img1)

        cv2.namedWindow("window2", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window2",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow("window2", self.img2)
        cv2.moveWindow("window2", 1920, 0)

        cv2.namedWindow("window3", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window3",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow("window3", self.img3)
        cv2.moveWindow("window3", 3840, 0)

        cv2.namedWindow("window4", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window4",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow("window4", self.img4)
        cv2.moveWindow("window4", 5760, 0)
        cv2.waitKey(0)

    def twohorizontal(self):
        """ Method for displaying four images on double monitor that aligned two horizontal"""
        cv2.namedWindow("window1", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window1",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

        cv2.namedWindow("window2", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window2",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.moveWindow("window2", 1920, 0)

        timerStart = time.time()

        cv2.imshow("window2", self.img2)
        cv2.imshow("window1", self.img1)

        timerEnd = time.time()
        executionTime = timerEnd - timerStart

        print("execution time:",executionTime)
        cv2.waitKey(0)

    def fourvertical(self):
        """ Method for displaying four images on double monitor that aligned four vertical"""
        cv2.namedWindow("window1", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window1",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow("window1", self.img1)

        cv2.namedWindow("window2", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window2",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow("window2", self.img2)
        cv2.moveWindow("window2", 0, 1080)

        cv2.namedWindow("window3", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window3",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow("window3", self.img3)
        cv2.moveWindow("window3", 0, 2160)

        cv2.namedWindow("window4", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window4",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow("window4", self.img4)
        cv2.moveWindow("window4", 0, 3240)
        cv2.waitKey(0)
    
    def dualhd(self, imgpath):
        img = cv2.imread(imgpath)
        cv2.namedWindow("window1", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window1",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow("window1", img)
        cv2.waitKey(0)
