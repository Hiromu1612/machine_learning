import matplotlib.pyplot as plt
import pandas as pd

wine=pd.read_csv(r"C:\Users\1612h\Machine_learning\kujirahikou\excell\winequality-white.csv",sep=";",encoding="utf-8") #sep:区切り文字を読み込む デフォルトはカンマ


count_data=wine.groupby("quality")["quality"].count() #("quality")でグループ分けし、["quality"]でquality列を指定して、count()でデータ数を数える
print(count_data)