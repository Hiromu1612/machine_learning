import cv2
import matplotlib.pyplot as plt

img=cv2.imread(r"C:\Users\1612h\Machine_learning\kujirahikou\flower.jpg")
img=cv2.resize(img, (300, 169))

img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray=cv2.GaussianBlur(img_gray, (7, 7), 0) #ぼかしを入れることでノイズを除去する GaussianBlurとは、画像をぼかす処理を行う関数 (画像, ぼかしの大きさで奇数, ぼかしの標準偏差)
img2=cv2.threshold(img_gray, 140, 240, cv2.THRESH_BINARY_INV)[1] #二値化処理を行う (画像, 閾値, 閾値以上の, どのように処理するか) 閾値を超えたら白、超えないと黒になる
# 140より大きいと白、140より小さいと黒になる INVは反転する

plt.subplot(1, 2, 1) #1行2列の1番目の位置にプロット
plt.imshow(img2, cmap="gray") #グレースケールで表示
plt.axis('off')

#! 輪郭(contour)の検出
contours=cv2.findContours(img2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0] #輪郭の検出 (画像, どのように輪郭を取得するか, どのように輪郭を表現するか)
# RETR_LISTは輪郭を全て取得する, CHAIN_APPROX_SIMPLEは輪郭の端点を圧縮する RETRの略はretrieve

#検出した輪郭を描画
for i in contours:
    x, y, w, h=cv2.boundingRect(i) #輪郭を囲む四角形を取得
    if w<30 or w>200:
        continue #大きすぎたり小さすぎたりする輪郭を除外
    print(x, y, w, h)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2) #(画像, 左上の座標, 右下の座標, 色, 線の太さ)

plt.subplot(1, 2, 2) #1行2列の2番目の位置にプロット
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) #BGRからRGBに変換して表示
plt.axis('off')
plt.show()