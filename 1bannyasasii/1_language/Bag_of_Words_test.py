from janome.tokenizer import Tokenizer

#! 1. 複数の文章を単語に分割する
t=Tokenizer() #トークナイザーを作成 単語分割処理をするオブジェクト
sentences=["おいしいビールを飲む", "コーヒーを飲む", "おいしいクラフトビールを買う"]
words_list=[]
for sentence in sentences:
    words_list.append(list(t.tokenize(sentence, wakati=True)))
print(words_list) #形態素解析の結果をリストに変換して表示


#! 2. 重複のない単語のリストを作る
unique_words=[]
for words in words_list:
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
print(unique_words) #重複のない単語のリストを表示


#! 3. Bag of Wordsのデータを作成する
bow_list=[]
for words in words_list:
    Bag_of_Words=[]
    for unique_word in unique_words:
        Bag_of_Words.append(words.count(unique_word)) #重複のない単語の出現回数を数える
    bow_list.append(Bag_of_Words)
print(bow_list) #Bag of Wordsのデータを表示


#! 4. IDFを計算する Internet Document Frequency 単語が出現する文章の数
from math import log
idf_list=[]
for i in range(len(unique_words)):
    count=0
    for BoW in bow_list:
        if BoW[i]>0:
            count+=1 #単語が出現する文章の数を数える
    idf=log((len(sentences)+1)/(count+1)) #IDFを計算する
    idf_list.append(idf)
print(idf_list) #IDFを表示


#! 5. TF-IDFを計算する Term Frequency - Internet Document Frequency 単語の出現回数とIDFを掛け合わせる
BoW_TFIDF_list=bow_list[1]
num_of_words=sum(BoW_TFIDF_list)
tfidf_list=[]
for i,value in enumerate(BoW_TFIDF_list):
    tfidf_list.append((value/num_of_words)*(idf_list[i]+1))
print(tfidf_list) #TF-IDFを表示