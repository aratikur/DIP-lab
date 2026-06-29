import cv2
import matplotlib.pyplot as plt
from tkinter import filedialog, Tk

Tk().withdraw()

file = filedialog.askopenfilename()
img = cv2.imread(file, 0)

plt.hist(img.ravel(), 256, [0,256])
plt.title("Histogram")
plt.show()

save = filedialog.asksaveasfilename(defaultextension=".jpg")
if save:
    cv2.imwrite(save, img)