from sklearn.datasets import make_regression
import pandas as pd, matplotlib.pyplot as plt, seaborn as sns

#regression:回帰 回帰とは、ある変数の値が他の変数の値にどのように影響されるかを調べること
X,y=make_regression(
    random_state=3, #ランダムの種
    n_features=1, #特徴量
    noise=10, #ノイズとは、データに含まれる誤差や外れ値のこと 最大50のノイズ
    bias=100, #バイアスとは、データの中心位置を示す値 y切片100
    n_samples=300 #サンプル数
)

df=pd.DataFrame(X)
df["target"]=y

sns.set(style="whitegrid")
plt.scatter(df[0],df["target"],color="blue",alpha=0.5)
plt.show()