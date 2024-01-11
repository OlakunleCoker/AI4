import cv2
import imutils
img = cv2.imread("C:/Users/OWNER/Desktop/AI PS/AI4/sample.jpg")
resizeImg = imutils.resize(img,width=20)
cv2.imwrite("resizedImage.jpg",resizeImg)
