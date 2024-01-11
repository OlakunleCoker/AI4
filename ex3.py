import cv2
img = cv2.imread("C:/Users/OWNER/Desktop/AI PS/AI4/sample.jpg")
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresImg = cv2.threshold(grayImg,200,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("thresholdImage.jpg",thresImg)
