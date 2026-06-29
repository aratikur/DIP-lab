import cv2
import matplotlib.pyplot as plt

# Read two images
img1 = cv2.imread('images.jpeg')
img2 = cv2.imread('flower1.jpg')

# Resize second image to match first image size
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Image Addition
added = cv2.add(img1, img2)

# Image Subtraction
subtracted = cv2.subtract(img1, img2)

# Display
plt.figure(figsize=(12, 8))

plt.subplot(221)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("Image 1")


plt.subplot(222)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("Image 2")


plt.subplot(223)
plt.imshow(cv2.cvtColor(added, cv2.COLOR_BGR2RGB))
plt.title("Added Image")


plt.subplot(224)
plt.imshow(cv2.cvtColor(subtracted, cv2.COLOR_BGR2RGB))
plt.title("Subtracted Image")


plt.tight_layout()
plt.show()