from hagaki_read import detect_post_number
import cv2, matplotlib.pyplot as plt
from joblib import load

#学習データの読み込み
clf=load(r"C:/Users/1612h/Machine_learning/kujirahikou/OpenCV/digits.pkl")

contours,img=detect_post_number(r"C:\Users\1612h\Machine_learning\kujirahikou\hagaki1.png")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) #BGRからRGBに変換して表示
plt.axis('off')
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05) #余白を調整
for i,j in enumerate(contours):
    x,y,w,h=j
    #輪郭の輪の部分だけ小さくする
    #iが4番目以降はさらに小さくする
    if i>=4:
        x+=6
        y+=6
        w-=15
        h-=15
    else:
        x+=4
        y+=4
        w-=12
        h-=12
    #画像データを取得
    im2=img[y:y+h, x:x+w]
    #データを学習データに合わせる
    im2_gray=cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
    im2_gray=cv2.resize(im2_gray, (8, 8))
    im2_gray=15-im2_gray//16 #白黒反転
    im2_gray=im2_gray.reshape(-1, 64)
    #予測
    res=clf.predict(im2_gray)
    #出力
    plt.subplot(1, 7, i+1)
    plt.imshow(im2)
    plt.axis("off")
    plt.title(str(res))
plt.show()