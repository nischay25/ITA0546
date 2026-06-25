import cv2

cap = cv2.VideoCapture(r"C:\Users\nnisc\Videos\Captures\VID_20230819_180516928.mp4")

if not cap.isOpened():
    print("Error loading video")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)

if fps == 0:
    fps = 30

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video", frame)

    delay = int(1000 / fps)

    if cv2.waitKey(delay) & 0xFF == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()