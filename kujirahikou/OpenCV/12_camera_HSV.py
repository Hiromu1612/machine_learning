import cv2, numpy as np

cap=cv2.VideoCapture(0)
while True:
    _, frame=cap.read()
    frame=cv2.resize(frame, (600, 400))

    #! 色空間をRGBからHSVに変換 Hue(色相) Saturation(彩度) Value(明度)
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)
    #HSVの各成分に分解
    hue=hsv[:,:,0] #色相
    sat=hsv[:,:,1] #彩度
    val=hsv[:,:,2] #明度
    img=np.zeros(hue.shape, dtype=np.uint8)#画像と同じサイズの配列を作成 dtype=np.uint8は配列の要素の型を8ビット符号なし整数にする
    img[((hue<50) |(hue>200)) & (sat>100) ]=255 #青色の部分を白(255)にする
    
    cv2.imshow('OpenCV Web Camera', img)
    key=cv2.waitKey(1)
    if key==27 or key==13:
        break
cap.release()
cv2.destroyAllWindows()