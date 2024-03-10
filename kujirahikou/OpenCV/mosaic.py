import cv2

def mosaic(img, rect, size):
    #モザイクをかける領域を取得
    (x1, y1, x2, y2)=rect 
    w=x2-x1
    h=y2-y1
    img_rect=img[y1:y2, x1:x2] #[y1:y2, x1:x2]で切り取り
    #一度縮小して拡大する(モザイク処理)
    img_small=cv2.resize(img_rect, (size, size))
    img_mos=cv2.resize(img_small, (w, h), interpolation=cv2.INTER_AREA) #interpolation=cv2.INTER_AREAで縮小時の補完方法を指定 interpolation:内挿
    #モザイクを掛けたい部分に重ねる
    img2=img.copy() #copy()で画像をコピー
    img2[y1:y2, x1:x2]=img_mos
    return img2