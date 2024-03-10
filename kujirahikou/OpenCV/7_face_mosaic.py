import matplotlib.pyplot as plt
import cv2
from mosaic import mosaic as mosaic

#カスケードファイルを指定して検出器を作成 カスケードとは、機械学習によって作成された顔の特徴を学習したファイル
cascade_file=r"C:\Users\1612h\Downloads\haarcascade_frontalface_alt.xml"
cascade=cv2.CascadeClassifier(cascade_file)

#画像の読み込み
img=cv2.imread(r'C:\Users\1612h\Machine_learning\kujirahikou\girl.jpg')
img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #グレースケールに変換 物体の明暗によって検出できる

#顔検出の実行
face_list=cascade.detectMultiScale(img_gray, minSize=(150, 150))  #顔の検出 (画像, 最小の物体の大きさ) detectMultiScaleは顔の検出を行う関数

#結果の確認
if len(face_list)==0:
    print('失敗')
    quit()

#検出した部分にモザイクをかける
for (x,y,w,h) in face_list:
    img_face=mosaic(img, (x, y, x+w, y+h), 10) #img,(x1, y1, x2, y2), モザイクの透明さ

#画像の表示
plt.imshow(cv2.cvtColor(img_face, cv2.COLOR_BGR2RGB)) #BGRからRGBに変換して表示
plt.axis('off') #軸をオフにして画像のみを表示
plt.show()