import matplotlib.pyplot as plt, numpy as np

plt.subplots(figsize=(15,5))

#np.colormeshを使うとグラフをマス目上に区切れる 3×3, 8×8, 100×100で粗さを増やすと滑らかになる
sizelist=[3,8,100] #粗さのリスト
for i in range(3):
    size=sizelist[i]
    X,Y=np.meshgrid(
        np.linspace(0,10,size+1), #x軸の0-10の範囲 linspace:等間隔の数列を生成 linear space
        np.linspace(0,10,size+1) #y軸の範囲
    )
    C=np.linspace(0,100,size*size).reshape(size,size) #reshape:配列の形を変える
    plt.subplot(1,3,i+1) #1行3列のグラフのi+1番目
    plt.pcolormesh(X,Y,C,cmap="rainbow") #pcolormesh:マス目上に区切る cmap:色の指定(カラーマップ)

plt.show()