import cv2, numpy as np

#windowsのカメラの映像を取得 繰り返し画像を読み込むことで動画を作成
cap=cv2.VideoCapture(0) #(0)はカメラのデバイス番号 0はデフォルトのカメラ 1は2番目のカメラ
while True:
    #カメラの画像を読み込む
    _, frame=cap.read() #_は読み込んだ画像の有無を示す frameは読み込んだ画像
    frame=cv2.resize(frame, (600, 400)) #画像を縮小表示(横, 縦)
    frame[:,:,0]=0 #青を無くす [,,0]は青要素 [,,1]は緑要素 [,,2]は赤要素 [,,3]は透明度
    frame[:,:,1]=0 #緑を無くす
    cv2.imshow('OpenCV Web Camera', frame)
    key=cv2.waitKey(1) #1ミリ秒待つ ESCキーかEnterが押されたらループを抜ける
    if key==27 or key==13: #27はESCキー 13はEnterキー
        break
cap.release() #カメラを解放
cv2.destroyAllWindows() #ウィンドウを閉じる