import cv2

main_image = cv2.imread("C:/Users/aadhy/Desktop/images.jpg")

if main_image is not None:
    h, w, _ = main_image.shape

    cropped_region = main_image[0:80, 0:275]

    crop_h, crop_w, _ = cropped_region.shape

    paste_x = w - crop_w
    paste_y = h - crop_h

    if paste_x >= 0 and paste_y >= 0:
        main_image[paste_y:paste_y+crop_h,
                   paste_x:paste_x+crop_w] = cropped_region

        cv2.imshow("Result", main_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Cropped region is larger than image dimensions.")
else:
    print("Error loading image.")
