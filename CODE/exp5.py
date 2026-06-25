import cv2
import numpy as np
img = cv2.imread(r"D:\@amazingsupercar LAMBORGHINI HURACAN.webp")
img = cv2.resize(img, (300, 200))
x = 0
while True:
    canvas = np.zeros((500, 800, 3), dtype=np.uint8)
    h, w = img.shape[:2]
    canvas[150:150+h, x:x+w] = img
    cv2.imshow("Moving Image", canvas)
    x = x + 5  
    if x > 800:
        x = -w  
    if cv2.waitKey(30) & 0xFF == 27:  
        break
cv2.destroyAllWindows()