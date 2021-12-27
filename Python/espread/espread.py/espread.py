import cv2 as cv
import numpy as np
from urllib.request import urlopen
import os
import datetime
import time
import sys

#change to your ESP32-CAM ip
# url="http://192.168.1.20:81/stream"
# url1="http://192.168.1.21:81/stream"

url="http://192.168.1.21"
url1="http://192.168.1.21"

CAMERA_BUFFRER_SIZE=4096
stream=urlopen(url)
#stream1=urlopen(url1)

bts=b''
bts1=b''
i=0
while True:    
    try:
        bts+=stream.read(CAMERA_BUFFRER_SIZE)
        #bts1+=stream1.read(CAMERA_BUFFRER_SIZE)

        jpghead=bts.find(b'\xff\xd8')
        jpgend=bts.find(b'\xff\xd9')

        # jpghead1=bts1.find(b'\xff\xd8')
        # jpgend1=bts1.find(b'\xff\xd9')

        if jpghead>-1 and jpgend>-1:
            jpg=bts[jpghead:jpgend+2]
            bts=bts[jpgend+2:]
            img=cv.imdecode(np.frombuffer(jpg,dtype=np.uint8),cv.IMREAD_UNCHANGED)
            #img=cv.flip(img,0) #>0:垂直翻轉, 0:水平翻轉, <0:垂直水平翻轉            
            #h,w=img.shape[:2]
            #print('影像大小 高:' + str(h) + '寬：' + str(w))
            img=cv.resize(img,(640,480))
            cv.imshow("a",img)
        # if jpghead1>-1 and jpgend1>-1:
        #     jpg1=bts1[jpghead1:jpgend1+2]
        #     bts1=bts1[jpgend1+2:]
        #     img1=cv.imdecode(np.frombuffer(jpg1,dtype=np.uint8),cv.IMREAD_UNCHANGED)
        #     #img=cv.flip(img,0) #>0:垂直翻轉, 0:水平翻轉, <0:垂直水平翻轉            
        #     #h,w=img.shape[:2]
        #     #print('影像大小 高:' + str(h) + '寬：' + str(w))
        #     img1=cv.resize(img1,(640,480))
        #     cv.imshow("a1",img1)

        k=cv.waitKey(1)
    except Exception as e:
        print("Error:" + str(e))
        bts=b''
        stream=urlopen(url)
        continue
    
    k=cv.waitKey(1)
    # 按a拍照存檔
    if k & 0xFF == ord('a'):
        cv.imwrite(str(i) + ".jpg", img)
        i=i+1
    # 按q離開
    if k & 0xFF == ord('q'):
        break
cv.destroyAllWindows()