import cv2
import os
import numpy as np
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
 
# 創建圖片保存目錄
if not os.path.exists('images'):
    os.makedirs('images')

#不讓Tkinter主畫面顯示 :)
Tk().withdraw()

tsj_classifier = cv2.CascadeClassifier("data/cascade.xml")

print("processing image1...")
image_1_gray = cv2.imread(askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg")]), cv2.IMREAD_GRAYSCALE)
image_1 = cv2.resize(image_1_gray, (150, 150))
cv2.imwrite("images/image1.jpg", image_1)

# 判斷兩張圖片是否完全一樣
def is_same_image(img_file1, img_file2):
    img1 = cv2.imread(img_file1)
    img2 = cv2.imread(img_file2)
    #判斷解析度
    if img1.shape == img2.shape and not (np.bitwise_xor(img1, img2).any()):
        return True
    else:
        return False

tsj = tsj_classifier.detectMultiScale(image_1, 1.06, 1,minSize=(50, 50))

if tsj:
    print("got tsj")
    # tsj_image = Image.open("images/image1.jpg")
    # tsj_image = tsj_image.convert("RGBA")
    # tsjWidth, tsjHeight = tsj_image.size
    # watermark = Image.open("overlays/blow.png")
    # watermark = watermark.convert("RGBA")
    # watermarkWidth, watermarkHeight = watermark.size
else:
    print("no tsj")

