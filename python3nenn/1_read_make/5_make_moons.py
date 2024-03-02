from sklearn.datasets import make_moons
import pandas as pd, matplotlib.pyplot as plt, seaborn as sns

#架空のサンプルデータセットを自動生成 moons:三日月
X,y=make_moons(
    random_state=3, #ランダムの種
    noise=0.1, #ノイズとは、データに含まれる誤差や外れ値のこと 10%のノイズ
    n_samples=300 #サンプル数
)

df=pd.DataFrame(X) #特徴量Xでデータフレームを作り、分類yをtargetの列として追加
df["target"]=y

df0=df[df["target"]==0]
df1=df[df["target"]==1]

sns.set(style="whitegrid")
plt.scatter(df0[0],df0[1],color="blue",alpha=0.5)
plt.scatter(df1[0],df1[1],color="red",alpha=0.5)
plt.show()