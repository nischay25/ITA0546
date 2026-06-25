import cv2
import numpy as np

image = cv2.imread(r"D:\local disk e\Downloads\p2.webp")

if image is None:
    print("Image not found!")
    exit()

pts1 = np.float32([[50, 50], [300, 50], [50, 300], [300, 300]])

pts2 = np.float32([[0, 0], [300, 0], [100, 300], [300, 300]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

output = cv2.warpPerspective(image, matrix, (400, 400))

cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", output)

cv2.waitKey(0)
cv2.destroyAllWindows()