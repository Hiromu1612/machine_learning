import matplotlib.pyplot as plt
import cv2
from mosaic import mosaic as mosaic

img=cv2.imread(r'C:\Users\1612h\Machine_learning\kujirahikou\girl.jpg')
mos_img=mosaic(img, (200, 400, 500, 600), 30) #img,(x1, y1, x2, y2), モザイクの透明さ
print(mos_img.shape) #(縦, 横, チャンネル数)

#モザイク画像の表示
plt.imshow(cv2.cvtColor(mos_img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()