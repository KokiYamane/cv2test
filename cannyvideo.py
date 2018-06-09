# -*- coding: utf-8 -*-

"""
カメラからリアルタイムで画像を読み込み、輪郭抽出
"""

import cv2

CAP = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    RET, FRAME = CAP.read()

    # Our operations on the frame come here
    GRAY = cv2.cvtColor(FRAME, cv2.COLOR_BGR2GRAY)

    #輪郭抽出
    EDGES = cv2.Canny(GRAY, 50, 100)

    # Display the resulting frame
    cv2.imshow('frame', EDGES)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
CAP.release()
cv2.destroyAllWindows()
