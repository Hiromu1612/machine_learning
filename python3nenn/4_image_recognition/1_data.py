import pandas as pd
from sklearn.datasets import load_digits

digits=load_digits() #digit:桁,数字
#data:学習用画像データ target:画像データに対応する数字 target_names:画像データに対応する数字 images:画像データのピクセル値 DESCR:データセットの説明(description)
df=pd.DataFrame(digits.data)
# print(df.head())


import matplotlib.pyplot as plt
#機械用の64×1(横1列)の画像データ
for i in range(10):
    #先頭から10個の画像データを横一列に変換して表示
    plt.subplot(10,1,i+1) #subplot:複数のグラフを並べて表示 10行1列のi+1番目
    plt.axis("off") #軸を表示しない
    plt.imshow(digits.data[i:i+1],cmap="Grays") #imshow:画像を表示する cmap:カラーマップ Grays:グレースケール
    plt.title(digits.target[i])
plt.show()

#人間用に変換した8×8の画像データ
for i in range(10):
    plt.subplot(1,10,i+1) #subplot:複数のグラフを並べて表示 1行10列のi+1番目
    plt.axis("off") #軸を表示しない
    plt.imshow(digits.images[i],cmap="Grays") #imshow:画像を表示する cmap:カラーマップ
    plt.title(digits.target[i])
plt.show()


from sklearn.model_selection import train_test_split
X=digits.data #64×1の画像データ(問題)
y=digits.target #数字(答え)

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)
print(len(X_train),len(X_test),len(y_train),len(y_test)) #学習用75% テスト用25%