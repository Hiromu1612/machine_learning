from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt, pandas as pd, seaborn as sns

X,y=make_blobs(
    random_state=0, #ランダムの種は0にして毎回同じデータが生成されるようにする 1のときは1,2のときは2専用のデータが生成される
    n_features=2, #特徴量
    centers=2, #塊
    cluster_std=1, #ばらつき(標準偏差)
    n_samples=300 #サンプル数
)

#! 1.データを用意
from sklearn.model_selection import train_test_split #train_test_split:学習データ(75%)とテストデータ(25%)に分割する 問題X(説明変数)と答えy(目的変数)
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0) #random_state=0で毎回同じデータが生成されるようにする

df=pd.DataFrame(X_train) #特徴量Xでデータフレームを作り、分類yをtargetの列として追加
df["target"]=y_train
df0=df[df["target"]==0]
df1=df[df["target"]==1]
sns.set(style="whitegrid")
plt.scatter(df0[0],df0[1],color="blue",alpha=0.5)
plt.scatter(df1[0],df1[1],color="red",alpha=0.5)
plt.title("train:75%")
plt.savefig(r"C:\Users\1612h\Machine_learning\python3nenn\2_bunnrui\img\train_75%.png")
# plt.show()

df=pd.DataFrame(X_test) #特徴量Xでデータフレームを作り、分類yをtargetの列として追加
df["target"]=y_test
df0=df[df["target"]==0]
df1=df[df["target"]==1]
sns.set(style="whitegrid")
plt.scatter(df0[0],df0[1],color="blue",alpha=0.5)
plt.scatter(df1[0],df1[1],color="red",alpha=0.5)
plt.title("test:25%")
plt.savefig(r"C:\Users\1612h\Machine_learning\python3nenn\2_bunnrui\img\test_25%.png")
# plt.show()


#! 2.学習モデルを作る
from sklearn import svm
model=svm.SVC() #SVC:Support Vector Classification サポートベクターマシンで学習モデルを作る
print(model.fit(X_train,y_train)) #学習用データを渡して学習する fit:学習する SVC()だけで中のパラメータが表示されない場合もある


#! 3.予測する
predicted=model.predict(X_test) #テストデータを渡して予測する
df=pd.DataFrame(X_test)
df["target"]=predicted
df0=df[df["target"]==0]
df1=df[df["target"]==1]
sns.set(style="whitegrid")
plt.scatter(df0[0],df0[1],color="blue",alpha=0.5)
plt.scatter(df1[0],df1[1],color="red",alpha=0.5)
plt.title("predicted")
plt.savefig(r"C:\Users\1612h\Machine_learning\python3nenn\2_bunnrui\img\predicted.png")
# plt.show()


#! 4.正答率を求める
from sklearn.metrics import accuracy_score #accuracy_score:正答率を求める
score=accuracy_score(y_test,predicted) #(正解データ,予測データ)
print("正答率",score*100,"%")

#横3列でグラフを表示
fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # Create a figure with 3 subplots
# Load and display the images
img_train = plt.imread(r"C:\Users\1612h\Machine_learning\python3nenn\2_bunnrui\img\train_75%.png")
img_test = plt.imread(r"C:\Users\1612h\Machine_learning\python3nenn\2_bunnrui\img\test_25%.png")
img_predicted = plt.imread(r"C:\Users\1612h\Machine_learning\python3nenn\2_bunnrui\img\predicted.png")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # Create a figure with 3 subplots

# Load and display the images
img_train = plt.imread(r"C:\Users\1612h\Machine_learning\python3nenn\2_bunnrui\img\train_75%.png")
img_test = plt.imread(r"C:\Users\1612h\Machine_learning\python3nenn\2_bunnrui\img\test_25%.png")
img_predicted = plt.imread(r"C:\Users\1612h\Machine_learning\python3nenn\2_bunnrui\img\predicted.png")

axes[0].imshow(img_train)
axes[0].set_title("Train: 75%")
axes[0].axis("off")

axes[1].imshow(img_test)
axes[1].set_title("Test: 25%")
axes[1].axis("off")

axes[2].imshow(img_predicted)
axes[2].set_title("Predicted")
axes[2].axis("off")

plt.tight_layout()
plt.show()

# Remove the axis labels
for ax in axes:
    ax.axis("off")

plt.show()