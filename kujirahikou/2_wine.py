
#! 1.データを用意
import pandas as pd
wine=pd.read_csv(r"C:\Users\1612h\Machine_learning\kujirahikou\excell\winequality-white.csv",sep=";",encoding="utf-8") #sep:区切り文字を読み込む デフォルトはカンマ
#? 酸性度、酢酸、クエン酸、残糖、塩化物、遊離二酸化硫黄、総二酸化硫黄、密度、pH、硫酸塩、アルコール度数、品質(0-10)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report #classification_report:適合率、再現率、F値を表示する

X=wine.drop("quality",axis=1) #drop:列を削除 axis:0=行,1=列 Xは解答,yは答え
y=wine["quality"] #quality列を抽出

#! yのラベルを付けなおす 0-10→0,1,2
newlist=[]
for i in list(y):
    if i <= 4:
        newlist+=[0] #0:悪いワイン
    elif i <= 7:
        newlist+=[1] #1:普通のワイン
    else:
        newlist+=[2] #2:良いワイン
y=newlist

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, train_size=0.8, shuffle=True) #test_size:テストデータの割合 train_size:学習データの割合 shuffle:データをシャッフルする 


#! 2.学習モデルを作る
model=RandomForestClassifier()
model.fit(X_train,y_train) #学習用データを渡して学習する fit:学習する

#! 3.予測する
predicted=model.predict(X_test)

#! 4.評価する
score=accuracy_score(y_test,predicted) #正解率
print("正解率:",score*100,"%")
# print(classification_report(y_test,predicted)) 
#precision(適合率)、recall(再現率 実際に正解した割合)、f1-score(適合率と再現率の調和平均)、support(正解ラベルのデータ数)を表示する