from sklearn import datasets
iris=datasets.load_iris() #アヤメのデータセットを読み込む
print(iris.data) #data:学習用のデータ feature_names:特徴量の名前 target:目的(分類)の値 target_names:目的(分類)の名前 DESCR:データセットの説明(英語)
print(iris.feature_names) #特徴量の名前
print(iris.target_names) #目的(分類)の名前
print(iris.target) #目的(分類)の値 sepal(がく),petal(花弁)

import pandas as pd
df=pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"]=iris.target #アヤメの品種(分類)の値を追加
print(df.head())

import matplotlib.pyplot as plt, seaborn as sns
sns.set(style="whitegrid")
#3種類のアヤメの品種ごとに、targetの値でデータフレームに分ける
df_setosa=df[df["target"]==0]
df_versicolor=df[df["target"]==1]
df_virginica=df[df["target"]==2]
df_setosa["sepal width (cm)"].hist(color="red",alpha=0.5)
df_versicolor["sepal width (cm)"].hist(color="blue",alpha=0.5)
df_virginica["sepal width (cm)"].hist(color="green",alpha=0.5)
plt.legend(["setosa","versicolor","virginica"]) #凡例を追加
plt.xlabel("sepal width (cm)")
plt.ylabel("count")
plt.show()