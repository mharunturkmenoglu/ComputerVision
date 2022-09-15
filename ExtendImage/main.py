from operator import concat
import cv2
from ExtendImage import ExtendImage
from concatenateImages import ConcatenateImages

def main():
    concat = ConcatenateImages("images/1.jpg", "images/2.jpg", "images/3.jpg", "images/4.jpg")
    img = concat.concatenate()

    cv2.namedWindow("window1", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window1",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow("window1", img)
    cv2.waitKey(0)
    
if __name__ == "__main__":
    main()