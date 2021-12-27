import cv2
import time

time.sleep(5)

vidcap = cv2.VideoCapture(0)
success,image = vidcap.read()
cv2.imwrite("bg.jpg", image)     # save frame as JPEG file      
success,image = vidcap.read()
print('Read a new frame: ', success)
