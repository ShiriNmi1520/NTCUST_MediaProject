from tkinter import Tk
from tkinter.filedialog import askopenfilename

print(askopenfilename(filetypes=[("Image files", "*.jpg")]))