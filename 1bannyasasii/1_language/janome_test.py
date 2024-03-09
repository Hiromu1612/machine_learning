from janome.tokenizer import Tokenizer

t=Tokenizer() #トークナイザーを作成 単語分割処理をするオブジェクト
text="東京都でおいしいビールを飲もう"
tokens=t.tokenize(text) #形態素解析を実行 形態素とは、言語学で、意味を持つ最小単位
for token in tokens:
    print(token) #形態素解析の結果を表示

tokens=t.tokenize(text, wakati=True) #!分かち書きだけを表示
print(list(tokens)) #形態素解析の結果をリストに変換して表示
print(len(list(tokens))) #形態素解析の結果の数を表示