
#! 1.データを用意
from sklearn.datasets import load_digits
X,y=load_digits(return_X_y=True) #64×1の画像データ(問題),数字(答え)をX,yに代入 Falseだと辞書型で説明などの情報も返す
# X_0=X[0].reshape(8,8) #1次元配列を8×8の2次元配列に変換
from matplotlib import pyplot as plt
# plt.imshow(X_0, cmap="binary") #cmap:カラーマップ
# plt.show()
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)


#! 2.学習モデルを作る
from sklearn.linear_model import LogisticRegression #clf:classifier(分類器)
clf=LogisticRegression(random_state=0, solver="liblinear", multi_class="auto") #solver:最適化問題を解くアルゴリズム multi_class:多クラス分類問題を解く方法
print(clf.fit(X_train,y_train)) #学習用データを渡して学習する fit:学習する


#? 自分の手書きの文字を読み込む
from PIL import Image, ImageEnhance, ImageOps
im=Image.open(r"C:\Users\1612h\Machine_learning\1bannyasasii\2_image_recognition\moji.jpg")
enhancer=ImageEnhance.Brightness(im)
im_enhanced=enhancer.enhance(1.3) #明るさを1.4倍にする
im_gray=im_enhanced.convert(mode="L") #convert:変換 L:グレースケール 1:白黒(二値) 2:16階調 3:256階調

#? UCIのデータは白(0)-黒(16)だが、PILのデータは白(255)-黒(0)なので、白(255)-黒(0)に変換する
im_inverted=ImageOps.invert(im_gray) #白黒反転

#? 8×8にリサイズ
im_resized=im_inverted.resize((8,8))
plt.imshow(im_resized, cmap="gray")
# plt.show()

#? 画像を配列に変換 画像データの最大値が16になるように、17×値÷256で計算し、0.0~16.93 小数点以下をnp.floorで切り捨てると0.0~16.0の値になる
import numpy as np
X_im2d=np.asarray(im_resized) #asarrayで画像を二次元の配列に変換
X_im1d=X_im2d.flatten() #flatten:多次元配列を1次元配列に変換
X_multiplied=X_im1d*(16/255)


#! 3.予測する
predicted=clf.predict([X_multiplied]) #学習データは2次元配列だから、予測データも2次元配列にする
print("予測結果:",predicted)

y_predicted=clf.predict(X_test)


#! 4.評価する
from sklearn.metrics import accuracy_score #accuracy_score:正解率
score=accuracy_score(y_test,y_predicted) #正解率
print("正解率:",score*100,"%")


#! 5.間違って予測された文字を表示する
for i in range(len(y_test)): 
    if y_test[i]!=y_predicted[i]:
        print("正解:",y_test[i],"予測:",y_predicted[i])
        plt.imshow(X_test[i].reshape(8,8), cmap="binary")
        plt.show()
        break #一つだけ表示する