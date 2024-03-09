input_file=r"C:\Users\1612h\Machine_learning\kujirahikou\excell\weather_data.csv"
output_file=r"C:\Users\1612h\Machine_learning\kujirahikou\excell\output.csv"

#csvファイルを一行ずつ読込み、リストに格納する
with open(input_file, "rt", encoding="shift-jis") as f: #rt:読み込みモード
    lines=f.readlines() #readlines:ファイルを読み込んで、1行ずつリストに格納する

#ヘッダーをそぎ落として、新たなヘッダーをつける
lines=["年,月,日,気温,品質,均質\n"]+lines[5:]
lines=map(lambda v: v.replace("/",","), lines) #map:リストの各要素に関数を適用する lambda:無名関数 v:引数 lines:リスト
result="".join(lines).strip() #join:リストを結合する

#結果をファイルに書き込む
with open(output_file, "wt", encoding="utf-8") as f: #wt:書き込みモード
    f.write(result) #write:ファイルに書き込む
    print("書き込み完了")