import matplotlib.pyplot as plt
import cv2

img=cv2.imread(r'C:\Users\1612h\Machine_learning\kujirahikou\test.jpg') #画像の読み込み
# plt.imshow(img) #imshowはRGBで表示する
# plt.show()
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) #BGRからRGBに変換して表示
plt.axis('off') #軸をオフにして画像のみを表示
plt.show()

cv2.imwrite(r'C:\Users\1612h\Machine_learning\kujirahikou\test_write.png', img) #画像の保存