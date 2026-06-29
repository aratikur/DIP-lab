import cv2
from tkinter import filedialog, Tk

Tk().withdraw()

file = filedialog.askopenfilename()
img = cv2.imread(file)

result = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow("Original", img)
cv2.imshow("Filtered", result)

save = filedialog.asksaveasfilename(defaultextension=".jpg")
if save:
    cv2.imwrite(save, result)

cv2.waitKey(0)
cv2.destroyAllWindows()