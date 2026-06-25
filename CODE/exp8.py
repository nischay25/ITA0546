import cv2
import numpy as np
image = cv2.imread("C:/Users/nnisc/OneDrive/Pictures/Saved Pictures/Instagram.webp")
kernal = np.ones((5,5),np.uint8)
eroded_image = cv2.erode(image,kernal,iterations=1)
cv2.imshow('original',image)
cv2.imshow('eroded',eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()