#画像のダウンロード
import urllib.request
url="https://th.bing.com/th/id/OIP.IdXm0Cfz3stvooDtW__BywHaE7?w=238&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
urllib.request.urlretrieve(url, 'test_1.png')

#OpenCVで画像を読み込む
import cv2
img=cv2.imread('test_1.png')
cv2.imshow('test_1',img)
cv2.waitKey(0)
print(img)