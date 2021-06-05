import cv2
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#不讓Tkinter主畫面顯示 :)
Tk().withdraw()

tsj_classifier = cv2.CascadeClassifier("data/cascade.xml")

print("processing image1...")
img_path = askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg")])
origin_image = cv2.imread(img_path)
image_1_gray = cv2.cvtColor(origin_image, cv2.COLOR_BGR2GRAY)
image_1 = cv2.resize(image_1_gray, (150, 150))
cv2.imwrite("images/image1.jpg", image_1)

tsj = tsj_classifier.detectMultiScale(image_1, 1.06, 1,minSize=(50, 50))
print(tsj)
if tsj.any():
    print("got tsj")
    tsj_image = Image.open(img_path)
    tsj_image = tsj_image.convert("RGBA")
    tsjWidth, tsjHeight = tsj_image.size
    watermark = Image.open("overlays/blow.png")
    watermark = watermark.convert("RGBA")
    watermarkWidth, watermarkHeight = watermark.size
    watermark = watermark.resize(tsj_image.size)
    tsj_image.paste(watermark, (25, 25), watermark)
    tsj_image = tsj_image.convert("RGB")
    tsj_image.save("tsjOutput.jpg")
else:
    print("no tsj")

