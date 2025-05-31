from ultralytics import YOLO
import cv2

# IP Webcam stream URL (replace with your phone’s IP)
stream_url = 'http://192.168.31.114:8080/video'


cap = cv2.VideoCapture(stream_url)
model = YOLO("../Detection Pipeline/best.pt")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated_frame = results[0].plot()  # Draw detections
    cv2.imshow("Animal Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
