import cv2
import numpy as np

if __name__ == '__main__':

    im_src = cv2.imread(r"D:\BMW M3 wallpaper 8k.webp")

    im_dst = cv2.imread(r"D:\BMW M3 wallpaper 8k.webp")

    if im_src is None or im_dst is None:
        print("Error loading images")
        exit()

    pts_src = np.array([
        [141, 131],
        [480, 159],
        [493, 630],
        [64, 601]
    ], dtype=np.float32)

    pts_dst = np.array([
        [318, 256],
        [534, 372],
        [316, 670],
        [73, 473]
    ], dtype=np.float32)

    h, status = cv2.findHomography(pts_src, pts_dst)

    im_out = cv2.warpPerspective(
        im_src,
        h,
        (im_dst.shape[1], im_dst.shape[0])
    )

    cv2.imshow("Source Image", im_src)
    cv2.imshow("Destination Image", im_dst)
    cv2.imshow("Warped Source Image", im_out)

    cv2.waitKey(0)
    cv2.destroyAllWindows()