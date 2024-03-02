from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt, pandas as pd, seaborn as sns

X,y=make_blobs(
    random_state=0, #ランダムの種は0にして毎回同じデータが生成されるようにする 1のときは1,2のときは2専用のデータが生成される
    n_features=2, #特徴量
    centers=2, #塊
    cluster_std=1, #ばらつき(標準偏差)
    n_samples=300 #サンプル数
)

df=pd.DataFrame(X) #特徴量Xでデータフレームを作り、分類yをtargetの列として追加
df["target"]=y
# print(df.head())

df0=df[df["target"]==0]
df1=df[df["target"]==1]

sns.set(style="whitegrid")
plt.scatter(df0[0],df0[1],color="blue",alpha=0.5)
plt.scatter(df1[0],df1[1],color="red",alpha=0.5)
plt.show()