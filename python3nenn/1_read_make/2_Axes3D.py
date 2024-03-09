import matplotlib.pyplot as plt, seaborn as sns, pandas as pd
from sklearn import datasets
iris=datasets.load_iris()
sns.set(style="whitegrid")
df=pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"]=iris.target

#3種類のアヤメの品種ごとに、targetの値でデータフレームに分ける
df_setosa=df[df["target"]==0]
df_versicolor=df[df["target"]==1]
df_virginica=df[df["target"]==2]
plt.scatter(df_setosa["sepal width (cm)"],df_setosa["sepal length (cm)"],color="blue",alpha=0.5)
plt.scatter(df_versicolor["sepal width (cm)"],df_versicolor["sepal length (cm)"],color="red",alpha=0.5)
plt.scatter(df_virginica["sepal width (cm)"],df_virginica["sepal length (cm)"],color="green",alpha=0.5)
plt.legend(["setosa","versicolor","virginica"]) #凡例を追加
plt.xlabel("sepal width (cm)")
plt.ylabel("sepal length (cm)")
plt.show()

#赤と緑の点が重なっているため、三次元で表示する
from mpl_toolkits.mplot3d import Axes3D #mplはmatplotlibの略
fig=plt.figure()
ax=Axes3D(fig) #axはaxes(軸)の略
fig.add_axes(ax) #明示的にaxes(軸)を追加しないと、空のfigure(図)になる
ax.scatter(df_setosa["sepal width (cm)"],df_setosa["sepal length (cm)"],df_setosa["petal length (cm)"],color="blue")
ax.scatter(df_versicolor["sepal width (cm)"],df_versicolor["sepal length (cm)"],df_versicolor["petal length (cm)"],color="red")
ax.scatter(df_virginica["sepal width (cm)"],df_virginica["sepal length (cm)"],df_virginica["petal length (cm)"],color="green")
ax.set_xlabel("sepal width (cm)")
ax.set_ylabel("sepal length (cm)")
ax.set_zlabel("petal length (cm)")
plt.legend(["setosa","versicolor","virginica"]) #凡例を追加
ax.view_init(0,240) #視点を変更 0:上から見た 90:横 180:後ろ 240:横 (仰角,方位角)
plt.show()