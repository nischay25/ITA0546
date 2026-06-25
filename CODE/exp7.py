import cv2
import numpy as np
image = cv2.imread("C:/Users/nnisc/OneDrive/Pictures/Saved Pictures/Instagram.webp", cv2.IMREAD_GRAYSCALE)
kernal = np.ones((5,5),np.uint8)
dilated_image = cv2.dilate(image,kernal,iterations=1)
cv2.imshow('original',image)
cv2.imshow('dilated',dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()