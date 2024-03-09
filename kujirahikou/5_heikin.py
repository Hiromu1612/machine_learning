import pandas as pd
df=pd.read_csv(r"C:\Users\1612h\Machine_learning\kujirahikou\excell\output.csv", encoding="utf-8")

#!日付ごとの気温をリストにまとめる
date_temp={}
from tqdm import tqdm
for i,row in tqdm(df.iterrows()): #iterrows:データフレームの行を反復処理する
    m,d,v=(int(row["月"]),int(row["日"]),float(row["気温"])) #int:整数に変換 float:浮動小数点数に変換
    key=str(m)+"/"+str(d) #日付をキーにする
    if not key in date_temp: #そのキーが辞書になければ、キーを追加し、値はからのリスト
        date_temp[key]=[]
    date_temp[key]+=[v] #日付をキーにして、気温をリストに格納する

#!日付ごとの気温の平均を求める
avg_temp={}
for key in date_temp:
    v=avg_temp[key]=sum(date_temp[key])/len(date_temp[key]) #平均を求める
    # print("{0}:{1}".format(key,v)) #日付:平均気温

#! 月ごとの平均気温をグラフ化する
import matplotlib.pyplot as plt
month_temp=df.groupby("月")["気温"] #("月")でグループ分けし、["気温"]で気温列を指定して
month_avg_temp=month_temp.mean()
# print(month_avg_temp)
# month_avg_temp.plot()
# plt.show()

#!気温が30度を越えた日をフィルタリングする
hot_day=df[df["気温"]>30]
count=hot_day.groupby("年")["年"].count()
print(count)
count.plot()
plt.show()