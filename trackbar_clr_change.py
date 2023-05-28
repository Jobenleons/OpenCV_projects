import cv2 as cv
img = cv.imread("Resources/messi5.jpg")
cv.namedWindow("output")
def change(x):
    pass



cv.createTrackbar("switch","output",0,1,change)
cv.createTrackbar("color","output",0,1,change)

while True:
    cv.imshow("output", img)
    s1 = cv.getTrackbarPos("color", "output")

    if s1==0:
        g_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow("output", g_img)
    else :
        pass

    if cv.waitKey(1) == ord("q"):
        break
cv.waitKey(0)
cv.destroyAllWindows()