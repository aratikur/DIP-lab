import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img_color = cv2.imread('images.jpeg')
img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

L = 256

# Histogram
hist = np.zeros(L)
for p in img.flatten():
    hist[p] += 1

# Histogram Equalization
cdf = np.cumsum(hist / img.size)
equalized = np.round((L - 1) * cdf).astype('uint8')[img]

# Display
plt.figure(figsize=(12,8))

plt.subplot(221)
plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))



plt.subplot(222)
plt.hist(img.flatten(), 256)


plt.subplot(223)
plt.imshow(equalized, cmap='gray')



plt.subplot(224)
plt.hist(equalized.flatten(), 256)


plt.tight_layout()
plt.show()