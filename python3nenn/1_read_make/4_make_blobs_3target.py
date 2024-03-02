from sklearn.datasets import make_blobs
import pandas as pd, matplotlib.pyplot as plt, seaborn as sns

#架空のサンプルデータセットを自動生成 blobs:塊
X,y=make_blobs(
    random_state=3, #ランダムの種
    n_features=2, #特徴量
    centers=3, #塊
    cluster_std=1, #ばらつき(標準偏差)
    n_samples=300 #サンプル数
)

df=pd.DataFrame(X) #特徴量Xでデータフレームを作り、分類yをtargetの列として追加
df["target"]=y

df0=df[df["target"]==0]
df1=df[df["target"]==1]
df2=df[df["target"]==2]

sns.set(style="whitegrid")
plt.scatter(df0[0],df0[1],color="blue",alpha=0.5)
plt.scatter(df1[0],df1[1],color="red",alpha=0.5)
plt.scatter(df2[0],df2[1],color="green",alpha=0.5)
plt.show()