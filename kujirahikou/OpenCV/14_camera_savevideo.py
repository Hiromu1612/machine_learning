import cv2, numpy as np

cap=cv2.VideoCapture(0)
#動画ファイル保存用のオブジェクトを生成
fmt=cv2.VideoWriter_fourcc('m', 'p', '4', 'v') #動画保存時のfourccコードを指定
fps=20.0 #FPS フレームレート
size=(640, 360) #動画の画面サイズ
writer=cv2.VideoWriter('test1.m4v', fmt, fps, size)

while True:
    _, frame=cap.read()
    frame=cv2.resize(frame, size)
    writer.write(frame) #動画を1フレームずつ保存
    cv2.imshow('frame', frame) #(ウィンドウ名, 画像データ)
    if cv2.waitKey(1)==27: #ESCキーで終了
        break
    
writer.release() #動画ファイルを閉じる
cap.release() #カメラデバイスを閉じる
cv2.destroyAllWindows() #ウィンドウを閉じる