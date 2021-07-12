import numpy as np
import cv2 as cv 
from time import time
import os
import datetime as dt


cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*"XVID")     
name = str(dt.datetime.now()).replace(":", ".") + ".avi"
out = cv.VideoWriter(name, fourcc, 30.0, (640, 480))


interval = 1 * 5

begin = time()


if not cap.isOpened():
    print("Cannot open camera")
    exit()



while True:

    if time() - begin >= interval:
        out.release()  
        videos = sorted([name for name in os.listdir() if name.split(".")[-1] == "avi"], key=lambda x: dt.datetime.fromisoformat(x.replace(".", ":", 2).replace(".avi", "")))
        print(videos)
        os.remove(videos[0])
        name = str(dt.datetime.now()).replace(":", ".") + ".avi"
        out = cv.VideoWriter(name, fourcc, 30.0, (640, 480))
        begin = time()

    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break


    out.write(frame)
    cv.imshow('frame', frame)


    if cv.waitKey(1) == ord('q'):
        break



out.release()
cap.release()
cv.destroyAllWindows()