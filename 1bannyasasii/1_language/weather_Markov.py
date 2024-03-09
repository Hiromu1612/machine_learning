import random
current_weather="晴れ"
markov_weather_list=[current_weather]
weather_data={
    "晴れ":{"next_weather":["晴れ","曇り","雨"],"weights":[0.7,0.2,0.1]}, #weights:重み(確率)
    "曇り":{"next_weather":["晴れ","曇り","雨"],"weights":[0.3,0.4,0.3]},
    "雨":{"next_weather":["晴れ","曇り","雨"],"weights":[0.2,0.3,0.5]}
}
for i in range(10):
    next_weather=weather_data[current_weather]["next_weather"] #ネストした辞書の値を一気に取り出す
    weights=weather_data[current_weather]["weights"]
    current_weather=random.choices(next_weather,weights)[0]
    markov_weather_list.append(current_weather)
print(markov_weather_list) #マルコフ連鎖の結果を表示