from operator import concat
import cv2
from extendImage import ExtendImage
from concatenateImages import ConcatenateImages

def main():
    concat = ConcatenateImages("images/1.jpg", "images/2.jpg", "images/3.jpg", "images/4.jpg")
    img = concat.concatenate()
    cv2.imshow("image", img)
    cv2.waitKey(0)
    
if __name__ == "__main__":
    main()