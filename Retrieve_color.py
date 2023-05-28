import cv2 as cv
import numpy as np
# img = cv.imread("Resources/messi5.jpg")
img = cv.imread("Resources/Screenshot 2023-03-20 115849.jpg")
# img = cv.resize(img,(300,300),interpolation=cv.INTER_AREA)

hsvimg = cv.cvtColor(img,cv.COLOR_BGR2HSV)
output = (np.ones((img.shape[0],img.shape[1]),dtype = np.uint8))*255
# cv.imshow("output",output)
def mlbclick(event,x,y,flags,userdata):
    if event == cv.EVENT_LBUTTONDOWN:
        v = hsvimg[y,x,2]
        s = hsvimg[y,x,1]
        h = hsvimg[y,x,0]
        text = "("+str(h)+","+str(s)+","+str(v)+")"
        cv.putText(output,text,(x,y),cv.FONT_HERSHEY_COMPLEX,1,(0,0,0))
        cv.imshow("output",output)
cv.imshow("image",img)
cv.setMouseCallback("image",mlbclick)
cv.waitKey(0)
cv.destroyAllWindows()
