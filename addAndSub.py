import cv2
from tkinter import filedialog, Tk

Tk().withdraw()

# Select two images
img1 = cv2.imread(filedialog.askopenfilename(title="Select First Image"))
img2 = cv2.imread(filedialog.askopenfilename(title="Select Second Image"))

# Resize second image to match first image
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Perform operations
add = cv2.add(img1, img2)
sub = cv2.subtract(img1, img2)

# Display results
cv2.imshow("Addition", add)
cv2.imshow("Subtraction", sub)

# Save Addition image
save_add = filedialog.asksaveasfilename(
    title="Save Addition Image",
    defaultextension=".jpg",
    filetypes=[("JPEG Image", "*.jpg"), ("PNG Image", "*.png")]
)
if save_add:
    cv2.imwrite(save_add, add)

# Save Subtraction image
save_sub = filedialog.asksaveasfilename(
    title="Save Subtraction Image",
    defaultextension=".jpg",
    filetypes=[("JPEG Image", "*.jpg"), ("PNG Image", "*.png")]
)
if save_sub:
    cv2.imwrite(save_sub, sub)

cv2.waitKey(0)
cv2.destroyAllWindows()