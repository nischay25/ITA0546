import cv2
image = cv2.imread(r"D:\BMW M3 wallpaper 8k.webp")
rotated = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated Image',rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()