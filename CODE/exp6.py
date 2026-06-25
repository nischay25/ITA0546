import cv2
image = cv2.imread(r"D:\local disk e\Downloads\p2.webp")
edged = cv2.Canny(image,threshold1=100,threshold2=200)
cv2.imshow('Original Image',image)
cv2.imshow('Edged Image',edged)
cv2.waitKey(0)
cv2.destroyAllWindows()