import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings
from sklearn.utils import all_estimators

iris_data=pd.read_csv(r"C:\Users\1612h\Machine_learning\kujirahikou\excell\iris.csv", encoding="utf-8")
X=iris_data.loc[:, ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
y=iris_data.loc[:, "Name"] #Name列が正解データ

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,train_size=0.8,shuffle=True) #test_size:テストデータの割合 train_size:学習データの割合 shuffle:データをシャッフルするかどうか

#分類のアルゴリズム全てを取得する
all_Algorithms=all_estimators(type_filter="classifier") #type_filter:分類器のみ取得する 引数なしで全て取得
warnings.filterwarnings("ignore") #警告文を非表示

#! K分割交差検証(クロスバリデーション)で評価する
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
kfold_cv=KFold(n_splits=5,shuffle=True) #n_splits:分割数 shuffle:データをシャッフルするかどうか

for (name,algorithm) in all_Algorithms:    
    try:
        # 特殊なアルゴリズムをスキップ
        if name == 'ClassifierChain' or name == 'MultiOutputClassifier' or name == 'OneVsOneClassifier' or name == 'OneVsRestClassifier' or name == 'OutputCodeClassifier' or name == 'VotingClassifier':
            continue
        clf=algorithm()
        if hasattr(clf,"score"): #hasattr:オブジェクトが指定された属性を持っているかどうかを調べる scoreオブジェクトがないとクロスバリデーションができない
            #! クロスバリデーションを行う
            scores=cross_val_score(clf,X,y,cv=kfold_cv) #(モデル,データ,分割数,シャッフルするかどうか)
            print(name,"の正解率:")
            print(scores*100,"%")
    except:
        print(name,"は不可能です")
        pass