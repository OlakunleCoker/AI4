import cv2
img = cv2.imread("C:/Users/OWNER/Desktop/AI PS/AI4/sample.jpg")
gaussianBlurImg = cv2.GaussianBlur(img,(21,21),0)
cv2.imwrite("gaussianImage.jpg",gaussianBlurImg)
