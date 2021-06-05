import cv2
import os
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename
 
# 創建圖片保存目錄
if not os.path.exists('images'):
    os.makedirs('images')

#不讓Tkinter主畫面顯示 :)
Tk().withdraw()

print("processing image1...")
image_1_gray = cv2.imread(askopenfilename(filetypes=[("Image files", "*.jpg")]), cv2.IMREAD_GRAYSCALE)
image_1 = cv2.resize(image_1_gray, (150, 150))
cv2.imwrite("images/image1.jpg", image_1)

print("processing image2...")
image_2_gray = cv2.imread(askopenfilename(filetypes=[("Image files", "*.jpg")]), cv2.IMREAD_GRAYSCALE)
image_2 = cv2.resize(image_2_gray, (150, 150))
cv2.imwrite("images/image2.jpg", image_2)

# 判斷兩張圖片是否完全一樣
def is_same_image(img_file1, img_file2):
    img1 = cv2.imread(img_file1)
    img2 = cv2.imread(img_file2)
    #判斷解析度
    if img1.shape == img2.shape and not (np.bitwise_xor(img1, img2).any()):
        return True
    else:
        return False

print(is_same_image("images/image1.jpg", "images/image2.jpg"))

