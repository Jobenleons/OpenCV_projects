import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Resources/messi5.jpg")
print(img.shape)
#roi
cv.imshow("Image",img)

mask = np.zeros((img.shape[0],img.shape[1]),dtype=np.uint8)
print(mask.shape)

r = cv.selectROI(img,showCrosshair=True)
mask[r[1]:r[1]+r[3],r[0]:r[0]+r[2]] = 1
col = ['b', 'g', 'r']
for i,col in enumerate(col):
    hist = cv.calcHist([img],[i],mask = mask, histSize = [256], ranges = [0,256])
    plt.plot(hist,color = col)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()


