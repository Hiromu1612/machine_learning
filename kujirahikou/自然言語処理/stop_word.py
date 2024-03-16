import MeCab
tagger=MeCab.Tagger("-Owakati")
tagger.parse("") #parse()メソッドで形態素解析
node=tagger.parseToNode("メイがダンスを踊っている。") #parseToNode()メソッドで形態素解析
#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音

result=[]
while node is not None:
    #品詞情報取得
    hinshi=node.feature.split(",")[0] #featureで表層形以外の情報を文字列で取得 split()メソッドでカンマで分割 0番目が品詞
    if hinshi in ["名詞"]:
        result.append(node.surface) #surfaceで表層形を取得
    elif hinshi in ["動詞","形容詞"]:
        result.append(node.feature.split(",")[6]) #6番目が原形
    node=node.next 
print(result) #ストップワード(意味のない単語)を除き、精度を高める 