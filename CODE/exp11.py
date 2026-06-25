import cv2
import numpy as np

image = cv2.imread(r"D:\local disk e\Downloads\p2.webp")

if image is None:
    print("Image not found!")
    exit()

angle = 45
scale = 1.0

height, width = image.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, scale)

output_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()