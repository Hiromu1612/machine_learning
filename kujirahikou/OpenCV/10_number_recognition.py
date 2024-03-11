from sklearn.model_selection import train_test_split
from sklearn import datasets, svm, metrics
from sklearn.metrics import accuracy_score
from joblib import dump

digits=datasets.load_digits()
X=digits.images
X=X.reshape(-1,64) #8×8の画像データを1×64のデータに変換
y=digits.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
clf=svm.SVC()
clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)
print(accuracy_score(y_test,y_pred)) #正解率

from joblib import dump
dump(clf, r"C:/Users/1612h/Machine_learning/kujirahikou/OpenCV/digits.pkl") #モデルを保存
