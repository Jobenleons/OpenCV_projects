import cv2
import numpy as np
import time
cap=cv2.VideoCapture("Resources/Parkour_office.mp4")
start = time.time()
while True:
    ret,img=cap.read()
    ts = time.time()-start
    bg = np.zeros((360,640,3),dtype = np.uint8)
    bg = cv2.putText(bg, str(ts), (50, 300), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
    newimg = cv2.addWeighted(img,0.8,bg,0.2,0)
    cv2.imshow("output",newimg)
    if cv2.waitKey(25)==ord('q'):
        print(img.shape)
        break

cap.release()
cv2.destroyAllWindows()
