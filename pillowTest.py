from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()

tsj_image = Image.open(askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg")]))
tsj_image = tsj_image.convert("RGBA")
tsjWidth, tsjHeight = tsj_image.size
watermark = Image.open("overlays/blow.png")
watermark = watermark.convert("RGBA")
watermarkWidth, watermarkHeight = watermark.size
watermark = watermark.resize(tsj_image.size)
tsj_image.paste(watermark, (25, 25), watermark)
tsj_image = tsj_image.convert("RGB")
tsj_image.save("tsjOutput.jpg")