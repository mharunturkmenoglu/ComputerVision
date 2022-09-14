import numpy as np
import cv2

img1 = cv2.imread('images/1.jpg')
img2 = cv2.imread('images/2.jpg')
img3 = cv2.imread('images/3.jpg')
img4 = cv2.imread('images/4.jpg')

res = np.concatenate((img1, img2), axis = 1)

#res2 = np.concatenate((img3, img4), axis = 1)
#res3 = np.concatenate((res,res2), axis = 1)


cv2.imwrite("deneme.jpg", res)

cv2.namedWindow("window1", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window1",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow("window1", res)

cv2.waitKey(0)