import numpy as np
import cv2 as cv 
from time import time
import os
import datetime as dt


DIRS = {0: "First",
        1: "Second",
        2: "Third"}

fourcc = cv.VideoWriter_fourcc(*"XVID")

caps = [cv.VideoCapture(i) for i in range(3)]
name = str(dt.datetime.now()).replace(":", ".") + ".avi"
outs = [cv.VideoWriter("./" + os.path.join("Дивы", dir, name), fourcc, 30.0, (640, 480)) for dir in DIRS.values()]


interval = 1 * 5

begin = time()


if not all([cap.isOpened() for cap in caps]):
    print("Cannot open camera")
    exit()



while True:
    if time() - begin >= interval:
        print("this")
        for i, out in enumerate(outs):
            out.release()

            name = str(dt.datetime.now()).replace(":", ".") + ".avi"
            outs[i] = cv.VideoWriter("./" + os.path.join("Дивы", list(DIRS.values())[i], name), fourcc, 30.0, (640, 480))
        begin = time()
    for i, cap in enumerate(caps):
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        outs[i].write(frame)
        cv.imshow('frame', frame)


    if cv.waitKey(1) == ord('q'):
        break

for out, cap in zip(outs, caps):
    out.release()
    cap.release()


cv.destroyAllWindows()