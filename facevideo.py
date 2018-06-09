# -*- coding: utf-8 -*-

"""
カメラからリアルタイムで画像を読み込み、顔認識
"""

import cv2

CAP = cv2.VideoCapture(0)

# カスケード型識別器の読み込み
CASCADE = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    # Capture frame-by-frame
    RET, FRAME = CAP.read()

    # Our operations on the frame come here
    GRAY = cv2.cvtColor(FRAME, cv2.COLOR_BGR2GRAY)

    # 顔領域の探索
    FACE = CASCADE.detectMultiScale(GRAY, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

    # 顔領域を赤色の矩形で囲むframe
    for (x, y, w, h) in FACE:
        cv2.rectangle(FRAME, (x, y), (x + w, y+h), (0, 0, 200), 3)

    # Display the resulting frame
    cv2.imshow('frame', FRAME)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
CAP.release()
cv2.destroyAllWindows()
