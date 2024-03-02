from sklearn.datasets import make_gaussian_quantiles
import pandas as pd, matplotlib.pyplot as plt, seaborn as sns

#gaussian_quantiles:ガウス分布の量子化 quantiles:分位数(クアンタイル) 同心円状
X,y=make_gaussian_quantiles(
    random_state=3, #ランダムの種
    n_features=2, #特徴量
    n_classes=3, #クラス数 クラスとは、分類されたグループのこと centerに似てる
    n_samples=300 #サンプル数
)

df=pd.DataFrame(X)
df["target"]=y

df0=df[df["target"]==0]
df1=df[df["target"]==1]
df2=df[df["target"]==2]

sns.set(style="whitegrid")
plt.figure(figsize=(6,6))
plt.scatter(df0[0],df0[1],color="blue",alpha=0.5)
plt.scatter(df1[0],df1[1],color="red",alpha=0.5)
plt.scatter(df2[0],df2[1],color="green",alpha=0.5)
plt.show()