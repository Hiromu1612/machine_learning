import cv2

img_last=None #前回の画像を記憶する変数
number=0 #画像の枚数


cap=cv2.VideoCapture(r"C:\Users\1612h\Machine_learning\kujirahikou\OpenCV\fish.mp4") #0ではなくファイル名を指定
count = 0
while True:
    _, frame = cap.read()
    if not _:
        break  # 読み込むフレームがなかったら終了
    frame = cv2.resize(frame, (600, 400))
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.GaussianBlur(img_gray, (15, 15), 0)  # ガウシアンフィルタでノイズを除去 (15,15)は(横, 縦)のフィルタサイズ
    img_b = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)[1]  # 二値化 127より大きい値は255(白)にする
    if not img_last is None:
        frame_diff = cv2.absdiff(img_last, img_b)  # img_lastとimg_bの差分を検出 absの略はabsolute(絶対値)
        contours = cv2.findContours(frame_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]  # 輪郭を抽出 RETR_EXTERNAL : 最も外側の輪郭のみ検出
        for i in contours:
            x, y, w, h = cv2.boundingRect(i)  # 差分があった点を画面に描く
            if w < 100 or w > 500:
                continue  # 小さい、大きい変更点は無視
            # 抽出した輪郭を矩形で囲み、保存
            img_fish = frame[y:y + h, x:x + w]  # [縦の範囲, 横の範囲]
            output_file = r"C:\Users\1612h\Machine_learning\kujirahikou\OpenCV\fish\\" + str(number) + ".jpg" #!\\は\をエスケープ文字として扱わないようにするため
            cv2.imwrite(output_file, img_fish)
            number += 1
    count += 1
    if count == 300:
        break
    img_last=img_b #img_bの画像を記憶
cap.release()
cv2.destroyAllWindows()