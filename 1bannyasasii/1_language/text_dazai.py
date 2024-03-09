
#! 1. zipファイルをダウンロードする
import requests
url="https://www.aozora.gr.jp/cards/000035/files/301_ruby_5915.zip"
read=requests.get(url)
content=read.content


#! 2. zipファイルを読み込む
import io, zipfile
file=io.BytesIO(content) #ファイルのようなオブジェクトを作成
zipfile=zipfile.ZipFile(file) #zipファイルを読み込む  
namelist=zipfile.namelist() #zipファイル内のファイル名を取得
# print(namelist)


#! 3. テキストファイルを読み込む
data=zipfile.read(namelist[0]) #zipファイル内のテキストファイルを読み込む
original_text=data.decode("shift_jis") #shift_jisでデコード デコード:バイト列を文字列に変換
# print(original_text[:500])


#! 4. 文章を前処理する
import re
first_sentence="私は、その男の写真を三葉、見たことがある。"
last_sentence="神様みたいないい子でした"
text=original_text.split(first_sentence)[-1].split(last_sentence)[0]
text=first_sentence+text+last_sentence

text=text.replace("|","").replace(" ","")
# text=re.sub("《\w+》","",text) #ルビを削除する
# text=re.sub("[#\w+]","",text) #入力注を削除する
text=re.sub("\u3000","",text) #全角スペースを削除する
text=text.replace("\r","").replace("\n","")
text=re.sub("[、「」?]","",text)
# text=re.sub("([^)]+)","",text)
# text=re.sub("[[^)]+]","",text)

sentences=text.split("。") #文章を分割する
# print("文の数",len(sentences))
# print(sentences[:10])



from janome.tokenizer import Tokenizer
#! 5. 1つの文を3つの単語の組にする
def get_three_words_list(sentence):
    BEGIN="__BEGIN__" #文章の先頭を表す文字列
    END="__END__"

    # sentence="おいしいビールを飲もう" 
    t=Tokenizer() #トークナイザーを作成 単語分割処理をするオブジェクト
    words=list(t.tokenize(sentence, wakati=True)) #形態素解析を実行 形態素とは、言語学で、意味を持つ最小単位
    words=[BEGIN]+words+[END] #文章の先頭と末尾に__BEGIN__と__END__を追加

    three_words_list=[]
    for i in range(len(words)-2): #3つの単語を1つずつずらしながらリストに追加 -2はBEGINとENDを除くため
        three_words_list.append(tuple(words[i:i+3])) #3つの単語をリストに追加 0:3は0,1,2番目の要素 tupleにするのは、24行目のCounterでリストをキーにするため
    return three_words_list



#! 6. 大量データの処理中に進捗バーを表示する
from tqdm import tqdm
from collections import Counter
import time
three_words_list=[]
for sentence in tqdm(sentences):
    three_words_list += get_three_words_list(sentence)
three_words_count=Counter(three_words_list) #単語の組の出現回数を数える
print(len(three_words_count))


#! 7. マルコフ連鎖用辞書データを作る
#キーとして前半2つの単語、値として次の単語とその出現回数(重み)を持つ辞書
def generate_markov_dict(three_words_count):
    markov_dict={}
    for three_words, count in three_words_count.items():
        two_words=three_words[:2] #3つの単語のうち、最初の2つを取り出す
        next_word=three_words[2]
        if two_words not in markov_dict: #2つの単語が辞書にない場合は空のデータを作成
            markov_dict[two_words]={"words":[], "weights":[]}
        markov_dict[two_words]["words"].append(next_word) #次の単語を追加
        markov_dict[two_words]["weights"].append(count) #出現回数(重み)を追加
    return markov_dict

from collections import defaultdict #キーが存在しない場合の辞書の初期値を設定できる
def get_first_word_count(three_words_count):
    first_word_count=defaultdict(int) #キーが存在しない場合の初期値を0に設定
    for three_words, count in three_words_count.items(): #itemsでキーと値を取り出す
        if three_words[0]=="__BEGIN__": #最初の単語が__BEGIN__で始まるもののみ取り出す
            next_word=three_words[1]
            first_word_count[next_word]+=count #出現回数をカウント
    return first_word_count
print(get_first_word_count(three_words_count)) 

def get_first_words_weights(three_words_count):
    first_word_count=get_first_word_count(three_words_count)
    words=[]
    weights=[]
    for word, count in first_word_count.items():
        words.append(word)
        weights.append(count)
    return words, weights

markov_dict=generate_markov_dict(three_words_count)
print(len(markov_dict))
first_words, first_weights=get_first_words_weights(three_words_count)
print(len(first_words))


#! 8. 文章を自動生成する
import random
def generate_text(first_words, first_weights, markov_dict):
    first_word=random.choices(first_words, first_weights)[0] #最初の単語をランダムに選ぶ
    BEGIN="__BEGIN__" #文章の先頭を表す文字列
    END="__END__"
    generate_words=[BEGIN, first_word] #文章の先頭に__BEGIN__を追加
    while True:
        pair=tuple(generate_words[-2:]) #最後の2つの単語を取り出す
        words=markov_dict[pair]["words"] #次の単語のリスト
        weights=markov_dict[pair]["weights"] #重みのリスト
        next_word=random.choices(words, weights)[0] #次の単語をランダムに選ぶ
        if next_word==END:
            break #文章が終了したらループを抜ける
        generate_words.append(next_word)
    return "".join(generate_words[1:]) #文章の先頭の__BEGIN__を除いて結合

for i in range(5):
    text=generate_text(first_words, first_weights, markov_dict)
    print(text) #生成した文章を表示