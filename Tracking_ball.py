import cv2 as cv
import numpy as np
cap = cv.VideoCapture("Resources/video_ball.mp4")
pointlist= []
temp =0
while cap.isOpened():

    ret,frame = cap.read()
    gframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gframe, (5, 5), 0)
    _, thr = cv.threshold(blur, 127, 255, cv.THRESH_BINARY)
    contours,heirarchy = cv.findContours(thr,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    lp1 = []
    for cnt in contours:
        cv.drawContours(frame,cnt,-1,(255,0,0),2)
        x,y,w,h = cv.boundingRect(cnt)
        p1 = (x+(w//2),y+(h//2))
        if temp:
            if pointlist[-1]!= p1:
                lp1.append(p1)
    pointlist.append(lp1)
    # print(pointlist)
    if len(pointlist)>2:
        for i in range(len(pointlist)-1):
            ip = pointlist[i]
            fp = pointlist[i + 1]
            for points1, points2 in zip(ip, fp):
                cv.line(frame, (points1[0], points1[1]), (points2[0], points2[1]), (255, 0, 0), 2)
        if len(pointlist)>32:
            pointlist.pop(0)
        #     for i in range (2):
        #
        #         fp = pointlist[i]
        #         for points1, points2 in zip(ip, fp):
        #             cv.line(frame, (points1[0], points1[1]), (points2[0], points2[1]), (255, 0, 0), 2)
    # if len(pointlist)==3:
    #     ip = pointlist.pop(0)
    #     for i in range (2):
    #
    #         fp = pointlist[i]
    #         for points1, points2 in zip(ip, fp):
    #             cv.line(frame, (points1[0], points1[1]), (points2[0], points2[1]), (255, 0, 0), 2)
    cv.imshow("Output",frame)
    temp=1
    if cv.waitKey(30) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

