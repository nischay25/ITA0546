import cv2
img = cv2.imread("C:/Users/aadhy/Desktop/water.jpg")
logo = cv2.imread("C:/Users/aadhy/Desktop/images.jpg")
logo = cv2.resize(logo, (100, 100))
h_logo, w_logo, _ = logo.shape
h_img, w_img, _ = img.shape
center_y = h_img // 2
center_x = w_img // 2
top_y = center_y - h_logo // 2
left_x = center_x - w_logo // 2
bottom_y = top_y + h_logo
right_x = left_x + w_logo
roi = img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(roi, 1, logo, 0.5, 0)
img[top_y:bottom_y, left_x:right_x] = result
cv2.imwrite("C:/Users/aadhy/Desktop/watermarked.jpg", img)
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
