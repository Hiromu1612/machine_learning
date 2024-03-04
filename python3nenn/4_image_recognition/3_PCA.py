from sklearn.datasets import load_digits
from sklearn import decomposition
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import matplotlib.pyplot as plt

digits = load_digits()
X = digits.data
y = digits.target

# 0〜9の色名を用意する
numbercolor = ["BLACK","BROWN","RED","DARKORANGE","GOLD",
               "GREEN","BLUE","PURPLE","GRAY","SKYBLUE"]
# yの値を色名に変えて、colorsリストを作る
colors = []
for i in y:
	colors.append(numbercolor[i])

# 主成分分析で、64個の特徴量を3個へと次元を減らす
pca = decomposition.PCA(n_components=3)
features3 = pca.fit_transform(X)

# 3個へ減らしたデータ（features3)で、データフレームを作る
df = pd.DataFrame(features3)

# 3D散布図の準備
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(projection='3d')
# 3個の特徴量をX,Y,Zにして、各点の数字に対応する色で散布図を描画
ax.scatter(df[0], df[1], df[2], color=colors)

# 数字がどの色かの見本を描画
ty = 0
for col in numbercolor:
    ax.text(50, 30, 30-ty*5, str(ty), size=20, color=col)
    ty+=1
plt.show()