import cv2
import time

cam = cv2.VideoCapture(0)#initial the camera
time.sleep(1)
while True:       #infinite loop to run continuously
    _,img = cam.read()
    cv2.imshow("cameraFeed",img)#To display in your window
    key = cv2.waitKey(1)& 0xFF
    if key == ord("q"):
        break       
    
cam.release()
cv2.destroyAllWindows()#This will close windows open currently
