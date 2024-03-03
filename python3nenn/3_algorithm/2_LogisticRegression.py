from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt, pandas as pd, seaborn as sns, numpy as np


#! 1.データを用意
X,y=make_blobs(
    random_state=5,
    n_features=2, #特徴量
    centers=3, #塊
    cluster_std=1, #ばらつき(標準偏差)
    n_samples=300
)
from sklearn.model_selection import train_test_split #train_test_split:学習データ(75%)とテストデータ(25%)に分割する 問題X(説明変数)と答えy(目的変数)
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0) #random_state=0で毎回同じデータが生成されるようにする

df=pd.DataFrame(X)



#! 2.学習モデルを作る
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
print(model.fit(X_train,y_train)) #学習用データを渡して学習する fit:学習する SVC()だけで中のパラメータが表示されない場合もある



#! 3.予測する
predicted=model.predict(X_test)
df=pd.DataFrame(X_test)



#! 4.評価する
from sklearn.metrics import accuracy_score #accuracy_score:正解率
score=accuracy_score(y_test,predicted) #正解率
print("正解率:",score*100,"%")




#! 5.分類の境界を描画する
from matplotlib.colors import ListedColormap
def plot_boundary(model, X, Y, target, xlabel, ylabel): #分類を行う学習済みモデル、特徴量X、特徴量Y、分類の値、x軸のラベル、y軸のラベル model=Noneで散布図だけを描画
    # 点と塗りのカラーマップ
    cmap_dots = ListedColormap([ "#1f77b4", "#ff7f0e", "#2ca02c"])
    cmap_fills = ListedColormap([ "#c6dcec", "#ffdec2", "#cae7ca"]) 

    # モデルがあれば、表示範囲の点をすべて予測して色を塗る
    if model:
        # 表示範囲を少し広げて分割し、調べる点（200x200）を用意する
        XX, YY = np.meshgrid(
            np.linspace(X.min()-1, X.max()+1, 200), #Xの最小値-1からXの最大値+1まで200分割 linspace:等間隔の数列を生成 linear space
            np.linspace(Y.min()-1, Y.max()+1, 200)) #Yの最小値-1からYの最大値+1まで200分割
        # 全ての点の値を、モデルで予測する
        pred = model.predict(np.c_[XX.ravel(), YY.ravel()]).reshape(XX.shape) #ravel:多次元配列を1次元配列に変換 c_:配列を結合する
        # 予測結果の値（0〜2）の色（cmap_fills）で塗りつぶす
        plt.pcolormesh(XX, YY, pred, cmap=cmap_fills, shading="auto") #pcolormesh:マス目上に区切る cmap:色の指定(カラーマップ)
        # 境界を灰色で塗る
        plt.contour(XX, YY, pred, colors="gray") 
    # targetの値（0〜2）の色（cmap_dots）で点を描画する
    plt.scatter(X, Y, c=target, cmap=cmap_dots) 
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

plot_boundary(model,df[0],df[1],y_test,"df [0]","df [1]")