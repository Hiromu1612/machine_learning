import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings
from sklearn.utils import all_estimators

iris_data=pd.read_csv(r"C:\Users\1612h\Machine_learning\kujirahikou\excell\iris.csv", encoding="utf-8")
X=iris_data.loc[:, ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
y=iris_data.loc[:, "Name"] #Name列が正解データ

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,train_size=0.8,shuffle=True) #test_size:テストデータの割合 train_size:学習データの割合 shuffle:データをシャッフルするかどうか

#! 分類のアルゴリズム全てを取得する
all_Algorithms=all_estimators(type_filter="classifier") #type_filter:分類器のみ取得する 引数なしで全て取得
warnings.filterwarnings("ignore") #警告文を非表示

for (name,algorithm) in all_Algorithms:
    try:
        clf=algorithm()
        clf.fit(X_train,y_train) #(学習用データ,答え)
        y_pred=clf.predict(X_test)
        print(name,"の正解率:",accuracy_score(y_test,y_pred)*100,"%") #正解率 (正解データ,予測データ)
    except Exception as e:
        print(name,"は不可能です")
        print(e)