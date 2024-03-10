import matplotlib.pyplot as plt
import cv2

img=cv2.imread(r'C:\Users\1612h\Machine_learning\kujirahikou\test.jpg') #画像の読み込み
print(img.shape) #画像のサイズを表示 (縦, 横, チャンネル数
img_cut=img[10:400, :] #画像の切り取り [縦の範囲, 横の範囲] (縦, 横)px
img_resize=cv2.resize(img_cut, (400, 400)) #画像のリサイズ (横, 縦)px
plt.imshow(cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)) #BGRからRGBに変換して表示
cv2.flip(img_resize, -1) #画像の反転 0:上下反転, 1:左右反転, -1:上下左右反転
plt.axis('off') #軸をオフにして画像のみを表示
plt.show()