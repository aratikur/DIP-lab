import cv2
import matplotlib.pyplot as plt
from tkinter import filedialog, Tk

# Hide Tkinter window
Tk().withdraw()

# Select image
file = filedialog.askopenfilename(title="Select a Color Image")

# Read color image
img = cv2.imread(file)

# Convert BGR to YCrCb
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# Equalize only the Y channel
ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])

# Convert back to BGR
equalized = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Equalized Image", equalized)

# Show Histograms (Y channel)
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).ravel(), 256, [0, 256])
plt.title("Original Histogram")

plt.subplot(1, 2, 2)
plt.hist(cv2.cvtColor(equalized, cv2.COLOR_BGR2GRAY).ravel(), 256, [0, 256])
plt.title("Equalized Histogram")

plt.tight_layout()
plt.show()

# Save equalized image
save = filedialog.asksaveasfilename(
    title="Save Equalized Image",
    defaultextension=".jpg",
    filetypes=[("JPEG Image", "*.jpg"), ("PNG Image", "*.png")]
)

if save:
    cv2.imwrite(save, equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()