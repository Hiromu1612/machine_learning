import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

iris_data=pd.read_csv(r"C:\Users\1612h\Machine_learning\kujirahikou\excell\iris.csv", encoding="utf-8")
X=iris_data.loc[:, ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
y=iris_data.loc[:, "Name"] #Name列が正解データ

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,train_size=0.8,shuffle=True) #test_size:テストデータの割合 train_size:学習データの割合 shuffle:データをシャッフルするかどうか

#! グリッドサーチで最適なパラメータを探す
#今回はSVMのパラメータを探す
parameters=[
    {"C":[1,10,100,1000],"kernel":["linear"]},
    {"C":[1,10,100,1000],"kernel":["rbf"],"gamma":[0.001,0.0001]}, #C:誤分類の許容度 gamma:決定境界の複雑さ rbf(放射基底関数):カーネル関数で非線形分離
    {"C":[1,10,100,1000],"kernel":["sigmoid"],"gamma":[0.001,0.0001]} #sigmoid:ロジスティックシグモイド関数とは、入力値を0から1の間に押し込む関数
]

#! グリッドサーチを行う
from sklearn.model_selection import KFold
kfold_cv=KFold(n_splits=5,shuffle=True) #n_splits:分割数 shuffle:データをシャッフルするかどうか
clf=GridSearchCV(SVC(),parameters,cv=kfold_cv) #(モデル,パラメータ,分割数,クロスバリデーション)
clf.fit(X_train,y_train) #(学習用データ,答え)
print("最適なパラメータ=",clf.best_estimator_) #best_estimator_:最適なパラメータ取得

#最適なパラメーターで評価
y_pred=clf.predict(X_test)
print("最適なパラメーターでの正解率:",accuracy_score(y_test,y_pred)) #正解率 (正解データ,予測データ)