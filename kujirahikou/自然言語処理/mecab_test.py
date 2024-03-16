import MeCab
#MeCabのオブジェクトを作成
taggar=MeCab.Tagger("-Owakati") #-Oオプションで出力フォーマットを指定 -Owakatiは分かち書き -OchasenはChaSen互換形式 -Oyomiは読み
result=taggar.parse("メイがダンスを踊っている。")#形態素解析 parse()メソッドで形態素解析
print(result)
#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音