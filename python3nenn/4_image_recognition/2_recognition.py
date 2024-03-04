import matplotlib.pyplot as plt, pandas as pd, seaborn as sns, numpy as np


#! 1.データを用意
from sklearn.datasets import load_digits
digits=load_digits() #digit:桁,数字
#data:学習用画像データ target:画像データに対応する数字 target_names:画像データに対応する数字 images:画像データのピクセル値 DESCR:データセットの説明(description)
df=pd.DataFrame(digits.data)

X=digits.data #64×1の画像データ(問題)
y=digits.target #数字(答え)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)


#! 2.学習モデルを作る
from sklearn import svm
model=svm.SVC(kernel="rbf", gamma=0.001)
model.fit(X_train,y_train) #学習用データを渡して学習する fit:学習する


#! 3.予測する
predicted=model.predict(X_test) 


#! 4.評価する
predicted=model.predict(X_test)
from sklearn.metrics import accuracy_score #accuracy_score:正解率
score=accuracy_score(y_test,predicted) #正解率
print("正解率:",score*100,"%")


#! 5.画像を読み込んで予測する
#画像を読み込み、グレースケールに変換
from PIL import Image
image=Image.open(r"C:\Users\1612h\Machine_learning\python3nenn\4_image_recognition\images\4.png").convert("L") #convert:変換 L:グレースケール
image=image.resize((8,8),Image.Resampling.LANCZOS) #resize:サイズ変更 ANTIALIAS:アンチエイリアス(画像を拡大・縮小する際にできるギザギザ(エイリアス)を滑らかにする) ランチョスフィルターに改名
image=np.array(image, dtype=float) #array:配列に変換

#読み込んだテストデータは黒(0)と白(255)→学習データの白(0)と黒(16)に変換
#画像データの最大値が16になるように、17×値÷256で計算し、0.0~16.93 小数点以下をnp.floorで切り捨てると0.0~16.0の値になる
image=16-np.floor(17*image/256)

#8×8を1×64の画像データに変換
image=image.flatten()

#予測
predicted=model.predict([image]) #学習データは2次元配列だから、予測データも2次元配列にする
print("予測結果:",predicted)