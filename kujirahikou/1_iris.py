import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

iris_data=pd.read_csv(r"C:\Users\1612h\Machine_learning\kujirahikou\excell\iris.csv", encoding="utf-8")
X=iris_data.loc[:, ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
y=iris_data.loc[:, "Name"] #Name列が正解データ

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,train_size=0.8,shuffle=True) #test_size:テストデータの割合 train_size:学習データの割合 shuffle:データをシャッフルするかどうか

clf=SVC()
clf.fit(X_train,y_train) #(学習用データ,答え)

y_pred=clf.predict(X_test)
print("正解率:",accuracy_score(y_test,y_pred)) #正解率 (正解データ,予測データ)