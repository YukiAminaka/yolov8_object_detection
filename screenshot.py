import numpy as np
import cv2

def pil2cv(image):
    ''' PIL型 -> OpenCV型 '''
    new_image = np.array(image, dtype=np.uint8)
    if new_image.ndim == 2:  # モノクロ
        print('モノクロ')
        pass
    elif new_image.shape[2] == 3:  # カラー
        print('カラー')
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)
    elif new_image.shape[2] == 4:  # 透過
        print('透過')
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGBA2BGRA)
    return new_image

from PIL import ImageGrab

img = ImageGrab.grab()

# スクリーンショットをMAT型に変換
new_img = pil2cv(img)
## 透過

# ファイルに保存
cv2.imwrite('new_img.jpg', new_img)