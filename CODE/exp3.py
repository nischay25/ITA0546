import cv2
import numpy as np
kernel = np.ones((25,25),np.uint8)
img = cv2.imread(r"C:\Users\nnisc\OneDrive\Pictures\Saved Pictures\Aesthetic Computer 4k Wallpaper.jpg")
cv2.imshow("original image",img)
cv2.waitKey(0)
img = cv2.resize(img,(200,200))
cv2.imshow("image",img)
cv2.waitKey(0)