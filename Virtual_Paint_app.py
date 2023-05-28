import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0,cv.CAP_DSHOW)
kernel = np.ones((5, 5), np.uint8)
pl = []

while (cap.isOpened()):
    ret,frame = cap.read()
    frame = cv.flip(frame, 1)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cap.set(3, 640)
    cap.set(4, 480)
    cap.set(10, 100)

    # hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    l_b = np.array([100,20,20])

    u_b = np.array([120,255,255])
    mask = cv.inRange(hsv,l_b,u_b)
    mask = cv.erode(mask, kernel, iterations=2)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    mask = cv.dilate(mask, kernel, iterations=1)
    cnts,hr = cv.findContours(mask, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    if len(cnts) > 0:
        cnt = sorted(cnts, key=cv.contourArea, reverse=True)[0]
        x, y, w, h = cv.boundingRect(cnt)
        p1 = (x + (w // 2), y + (h // 2))

        pl.append(p1)
    if len(pl)>100:
        pl.pop(0)
    for i in range(len(pl)):
        if i==0:
            continue
        cv.line(frame, pl[i-1], pl[i], [0,255,0], 2)
        # cv.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 2)
    res = cv.bitwise_and(frame,frame,mask= mask)
    cv.imshow("mask",mask)
    cv.imshow("Result", res)
    cv.imshow("Output",frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv.destroyAllWindows()
