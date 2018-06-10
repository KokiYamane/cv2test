# -*- coding: utf-8 -*-

"""
カメラからリアルタイムで画像を読み込み、背景除去
"""

import cv2

cap = cv2.VideoCapture(0)
bgs = cv2.createBackgroundSubtractorMOG2()

while True:

    # フレーム読み込み
    ret, frame = cap.read()

    # 背景除去
    mask = bgs.apply(frame, learningRate=0.01)
    bg = bgs.getBackgroundImage()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mov = gray * mask

    # 結果表示
    cv2.imshow('mask', mask)
    cv2.imshow('bg', bg)
    cv2.imshow('mov', mov)

    # 終了処理
    if cv2.waitKey(1) != -1:
        break

cap.release()
cv2.destroyAllWindows()
