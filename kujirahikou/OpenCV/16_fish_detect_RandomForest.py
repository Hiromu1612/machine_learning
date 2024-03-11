import cv2, copy
import joblib

clf=joblib.load(r"C:\Users\1612h\Machine_learning\kujirahikou\OpenCV\fish.pkl")
img_last=None
fish_th=3 #画像を保存するかどうかの閾値
count=0
frame_count=0

cap=cv2.VideoCapture(r"C:\Users\1612h\Machine_learning\kujirahikou\OpenCV\fish.mp4")
while True:
    _, frame = cap.read()
    if not _:
        break  # 読み込むフレームがなかったら終了
    frame = cv2.resize(frame, (600, 400))
    frame2=copy.copy(frame)
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.GaussianBlur(img_gray, (15, 15), 0)  # ガウシアンフィルタでノイズを除去 (15,15)は(横, 縦)のフィルタサイズ
    img_b = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)[1]  # 二値化 127より大きい値は255(白)にする
    if not img_last is None:
        frame_diff = cv2.absdiff(img_last, img_b)  # img_lastとimg_bの差分を検出 absの略はabsolute(絶対値)
        contours = cv2.findContours(frame_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]  # 輪郭を抽出 RETR_EXTERNAL : 最も外側の輪郭のみ検出
        fish_count=0
        for i in contours:
            x, y, w, h = cv2.boundingRect(i)  # 差分があった点を画面に描く
            if w < 100 or w > 500:
                continue  # 小さい、大きい変更点は無視
            # 抽出した輪郭を矩形で囲み、保存
            img_fish = frame[y:y + h, x:x + w]  # [縦の範囲, 横の範囲]
            
            
            img_fish=cv2.resize(img_fish, (64, 64))
            img_fish=img_fish.reshape(-1,) #1次元配列に変換
            y_pred=clf.predict([img_fish]) 
            if y_pred[0]==1: #魚が写っている
                fish_count+=1
                cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2) #(画像, 左上の座標, 右下の座標, 色, 線の太さ)
        if fish_count>fish_th: #魚が3枚以上写っていたら画像を保存
            fname=r"C:\Users\1612h\Machine_learning\kujirahikou\OpenCV\fish\fish"+str(count)+".jpg"
            cv2.imwrite(fname, frame) #(ファイル名, 画像データ)
            count+=1
    if count == 3:
        break
    cv2.imshow('FISH!', frame2)
    
    
    if cv2.waitKey(1)==13: #Enterキーで終了
        break
    img_last=img_b #img_bの画像を記憶
cap.release()
cv2.destroyAllWindows()