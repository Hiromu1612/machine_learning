import cv2

cap=cv2.VideoCapture(0)
img_last=None #前回の画像を記憶する変数
green=(0, 255, 0)

while True:
    _, frame=cap.read()
    frame=cv2.resize(frame, (600, 400))
    img_gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_gray=cv2.GaussianBlur(img_gray, (9, 9), 0) #ガウシアンフィルタでノイズを除去
    img_b=cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)[1] #二値化
    if img_last is None:
        img_last=img_b
        continue #最初のフレームは何もしない
    frame_diff=cv2.absdiff(img_last, img_b) #img_lastとimg_bの差分を検出
    contours=cv2.findContours(frame_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] #輪郭を抽出 RETR_EXTERNAL : 最も外側の輪郭のみ検出
    #差分があった点を画面に描く
    for i in contours:
        x, y, w, h=cv2.boundingRect(i)
        if w<30:
            continue #小さな変更点は無視
        cv2.rectangle(frame, (x, y), (x+w, y+h), green, 2)
    img_last=img_b #img_bの画像を記憶
    cv2.imshow('Diff Camera', frame)
    key=cv2.waitKey(1)
    if key==27 or key==13: 
        break
cap.release()
cv2.destroyAllWindows()