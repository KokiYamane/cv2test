# -*- coding: utf-8 -*-

"""
画像を読み込み、各種処理
"""

import cv2
from matplotlib import pyplot as plt

# 入力画像の読み込み
IMG = cv2.imread("Photos/IMG_20180609_161152.jpg")

# グレースケール変換
GRAY = cv2.cvtColor(IMG, cv2.COLOR_BGR2GRAY)
plt.imshow(GRAY, cmap='gray', interpolation='bicubic')
plt.show()

# 輪郭抽出
EDGES = cv2.Canny(GRAY, 50, 50)
plt.imshow(EDGES, cmap='gray', interpolation='bicubic')
plt.show()

# ヒストグラム
HIST = cv2.calcHist([EDGES], [0], None, [10], [0, 256])

plt.plot(HIST)
plt.xlim([0, 10])
plt.show()

# 結果を出力
#cv2.imshow("result.jpg", IMG)
#plt.imshow(EDGES, cmap='gray', interpolation='bicubic')
#plt.xticks(), plt.yticks()  # to hide tick values on X and Y axis
#plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
