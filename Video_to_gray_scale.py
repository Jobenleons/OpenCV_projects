import cv2 as cv

cap = cv.VideoCapture("Resources/Parkour_office.mp4")

while True:
    ret,img = cap.read()
    g_img =cv.cvtColor(img,cv.COLOR_BGR2HSV)
    cv.imshow("Output",g_img)
    if cv.waitKey(25) == ord('q'):
        break
cv.destroyAllWindows()