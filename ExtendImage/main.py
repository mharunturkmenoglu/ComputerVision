from operator import concat
import cv2
from ExtendImage import ExtendImage
from concatenateImages import ConcatenateImages
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidgetAction
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, uic
from PyQt5.uic import loadUi
import os

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("main.ui",self)
    
def main():
    """"
    concat = ConcatenateImages("images/1.jpg", "images/2.jpg", "images/3.jpg", "images/4.jpg")
    img = concat.concatenate()

    cv2.namedWindow("window1", cv2.WINDOW_AUTOSIZE)
    cv2.moveWindow("window1", 0, 50)
    cv2.imshow("window1", img)
    cv2.waitKey(0)
    """
    
    extend = ExtendImage("images/1.jpg", "images/2.jpg", "images/3.jpg", "images/4.jpg")
    extend.fourhorizontal()
    
if __name__ == "__main__":
    main()