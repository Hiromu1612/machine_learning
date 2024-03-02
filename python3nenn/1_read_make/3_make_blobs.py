from sklearn.datasets import make_blobs
import pandas as pd

#架空のサンプルデータセットを自動生成
X,y=make_blobs( #特徴量がX,目的(分類)がyに返ってくる
    random_state=3, #ランダムの種 最初はランダムでその後は同じ値で固定できる state:状態 2次元以上なら大文字,1次元は小文字
    n_features=2, #特徴量の数
    centers=2, #塊の数
    cluster_std=1, #ばらつきの大きさ(標準偏差)
    n_samples=300 #サンプルの数
    )

#特徴量Xでデータフレームを作り、分類yをtargetの列として追加
df=pd.DataFrame(X)
df["target"]=y
print(df.head())

import matplotlib.pyplot as plt,seaborn as sns
sns.set(style="whitegrid")
df0=df[df["target"]==0]
df1=df[df["target"]==1]
plt.figure(figsize=(8,8))
plt.scatter(x=df0[0],y=df0[1],color="blue",alpha=0.5)
plt.scatter(x=df1[0],y=df1[1],color="red",alpha=0.5)
plt.show()