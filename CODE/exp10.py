import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
cv2.namedWindow("Webcam VIDEO")
specified_factor = 1.0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Webcam VIDEO", frame)
    key = cv2.waitKey(1)
    if key == ord('+'):
        specified_factor += 5.0
    elif key == ord('-'):
        specified_factor -= 5.0
    elif key ==ord('q'):
        break
    cap.set(cv2.CAP_PROP_FPS,30*specified_factor)
cap.release()
cv2.destroyAllWindows()