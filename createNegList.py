import os
import numpy as np
with open("neg.txt", "w") as file:
    for image in os.listdir("negative"):
        line = "negative/" + image + "\n"
        file.write(line)