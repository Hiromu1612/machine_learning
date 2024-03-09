from sklearn.linear_model import LinearRegression
import pandas as pd, numpy as np, matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\1612h\Machine_learning\kujirahikou\excell\output.csv", encoding="utf-8")
X_train=(df["年"] <= 2015)
X_test=(df["年"] >= 2016)

#過去6日分を学習するデータを作成
def make_data(data):
    X=[]
    y=[]
    temps=list(data["気温"]) #気温の列をリストにする
    for i in range(len(temps)):
        interval=6  
        if i <= interval:
            continue #iが6日目までならスキップ 最初のデータには過去が存在しないため
        y.append(temps[i]) #７日目以降はその日の気温
        xa=[] #i-6日目からi-1日目までの気温を格納するリスト
        for p in range(interval): #過去6日間それそれのループ
            d=i+p-interval 
            xa.append(temps[d])
        X.append(xa)
    return X,y

X_train,y_train=make_data(df[X_train])
X_test,y_test=make_data(df[X_test])

#! 学習モデルを作り、予測する
model=LinearRegression()
model.fit(X_train,y_train) #学習用データを渡して学習する fit:学習する
predicted=model.predict(X_test)

#! グラフを描く
plt.figure(figsize=(10,6),dpi=100) #figure:グラフの大きさ dpi:解像度
plt.plot(y_test,c="red") #実際の気温
plt.plot(predicted,c="blue") #予測気温
import japanize_matplotlib
plt.legend(["実際の気温","予測気温"])
plt.show()

#! 評価
difference_temp=abs(y_test-predicted) #予測と実際の気温の差 abs:絶対値
print("誤差平均:",sum(difference_temp)/len(difference_temp))
print("最大誤差:",max(difference_temp))