import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read two images
img1 = cv2.imread('images.jpeg')
img2 = cv2.imread('flower1.jpg')

# Resize second image if sizes are different
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Image Addition
added = cv2.add(img1, img2)

# Convert to Grayscale
gray = cv2.cvtColor(added, cv2.COLOR_BGR2GRAY)

L = 256

# Histogram
hist = np.zeros(L)

for p in gray.flatten():
    hist[p] += 1

# Histogram Equalization
cdf = np.cumsum(hist / gray.size)
equalized = np.round((L - 1) * cdf).astype('uint8')[gray]

# Display
plt.figure(figsize=(12, 8))

plt.subplot(221)
plt.imshow(cv2.cvtColor(added, cv2.COLOR_BGR2RGB))
plt.title("Added Image")
plt.axis("off")

plt.subplot(222)
plt.hist(gray.flatten(), bins=256, range=(0, 256))
plt.title("Histogram Before Equalization")

plt.subplot(223)
plt.imshow(equalized, cmap='gray')
plt.title("Equalized Image")

plt.subplot(224)
plt.hist(equalized.flatten(), bins=256, range=(0, 256))
plt.title("Histogram After Equalization")

plt.tight_layout()
plt.show()