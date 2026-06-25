import cv2
import numpy as np

img1 = cv2.imread(r"C:\Users\nnisc\OneDrive\Pictures\Saved Pictures\Aesthetic Computer 4k Wallpaper.jpg")
img2 = cv2.imread("C:/Users/nnisc/OneDrive/Pictures/Saved Pictures/Instagram.webp")

if img1 is None or img2 is None:
    print("Error loading images")
    exit()

pts1 = np.float32([[50, 50],
                   [200, 50],
                   [50, 200],
                   [200, 200]])

pts2 = np.float32([[100, 100],
                   [300, 100],
                   [100, 300],
                   [300, 300]])

H = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Perspective Transformed Image', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()