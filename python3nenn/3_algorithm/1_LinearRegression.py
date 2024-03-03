from sklearn.datasets import make_regression
import matplotlib.pyplot as plt, pandas as pd, seaborn as sns

X,y=make_regression(
    random_state=3,
    n_features=1,
    noise=20,
    n_samples=30
)

df=pd.DataFrame(X)
sns.set(style="whitegrid")
plt.scatter(df[0],y,color="blue",alpha=0.5)
plt.show()


#線形回帰の線を引く
from sklearn.linear_model import LinearRegression #LinearRegression:線形回帰モデル
from sklearn.metrics import r2_score #r2_score:決定係数のことで、回帰分析の当てはまりの良さを示す指標
from sklearn.model_selection import train_test_split #train_test_split:学習データ(75%)とテストデータ(25%)に分割する 問題X(説明変数)と答えy(目的変数)

#! 1.データを用意
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0) #random_state=0で毎回同じデータが生成されるようにする

#! 2.学習モデルを作る
model=LinearRegression()
print(model.fit(X_train,y_train)) #学習用データを渡して学習する fit:学習する

#! 3.予測する
predicted=model.predict(X_test)
score=r2_score(y_test,predicted) #回帰分析の正解率
print("正解率:",score*100,"%")

plt.scatter(X,y,color="blue",alpha=0.5)
#散布図に線形回帰の線を引くために点をたくさん書いて直線にする
plt.plot(X,model.predict(X),color="red")
plt.show()