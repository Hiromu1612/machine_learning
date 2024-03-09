from janome.tokenizer import Tokenizer
from collections import Counter
#! 1. 1つの文を3つの単語の組にする
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


#! 2. 複数の文章から単語の組の出現回数を数える
sentences=["おいしいビールを飲もう", "ビールを飲もう", "おいしいビールは生"]
three_words_list=[]
for sentence in sentences:
    three_words_list += get_three_words_list(sentence)
three_words_count=Counter(three_words_list) #単語の組の出現回数を数える
# print(three_words_count)


#! 3. マルコフ連鎖用辞書データを作る
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

markov_dict=generate_markov_dict(three_words_count)
import pprint
pprint.pprint(markov_dict)



#! 4. 最初の単語の出現回数を数える
from collections import defaultdict #キーが存在しない場合の辞書の初期値を設定できる
def get_first_word_count(three_words_count):
    first_word_count=defaultdict(int) #キーが存在しない場合の初期値を0に設定
    for three_words, count in three_words_count.items(): #itemsでキーと値を取り出す
        if three_words[0]=="__BEGIN__": #最初の単語が__BEGIN__で始まるもののみ取り出す
            next_word=three_words[1]
            first_word_count[next_word]+=count #出現回数をカウント
    return first_word_count
print(get_first_word_count(three_words_count)) 



#! 5. 4の辞書データを単語と出現回数のリストにする
def get_first_words_weights(three_words_count):
    first_word_count=get_first_word_count(three_words_count)
    words=[]
    weights=[]
    for word, count in first_word_count.items():
        words.append(word)
        weights.append(count)
    return words, weights

first_words, first_weights=get_first_words_weights(three_words_count)
print(first_words, first_weights)



#! 6. 文章の生成関数を作る
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



#! 7. 6の関数を使って文章を生成する
for i in range(5):
    text=generate_text(first_words, first_weights, markov_dict)
    print(text) #生成した文章を表示