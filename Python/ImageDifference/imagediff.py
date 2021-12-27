import cv2 
import numpy as np 


imgFile = cv2.imread(r'/home/dass/Downloads/35.jpg',0)
imgFile2 = cv2.imread(r'/home/dass/Downloads/36.jpg',0)


 
image = cv2.imread('C:/Users/N/Desktop/Test.jpg')
imgFile[0:120] = 1
imgFile[:,:250] = 1
cv2.imshow('Test image',imgFile)
cv2.waitKey(0)
cv2.destroyAllWindows()

thresh = 127
im_bw = cv2.threshold(imgFile, thresh, 255, cv2.THRESH_BINARY)[1]
im_bw2 = cv2.threshold(imgFile2, thresh, 255, cv2.THRESH_BINARY)[1]
out_arr = np.logical_xor(im_bw, im_bw2)  
#print ("Output array after bitwise_xor: ", out_arr)
print(np.count_nonzero(out_arr==True))
print(np.count_nonzero(out_arr==True)/(out_arr.shape[0] * out_arr.shape[1]))
