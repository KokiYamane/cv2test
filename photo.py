# -*- coding: utf-8 -*-

"""
画像を読み込み、各種処理
"""

import cv2
from matplotlib import pyplot as plt

# 入力画像の読み込み
IMG = cv2.imread("bottle.jpg")

# グレースケール変換
GRAY = cv2.cvtColor(IMG, cv2.COLOR_BGR2GRAY)

#輪郭抽出
EDGES = cv2.Canny(GRAY, 0, 50)

# 結果を出力
#cv2.imshow("result.jpg", IMG)
plt.imshow(EDGES, cmap='gray', interpolation='bicubic')
#plt.xticks(), plt.yticks()  # to hide tick values on X and Y axis
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
