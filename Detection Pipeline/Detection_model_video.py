from ultralytics import YOLO
import cv2

cap=cv2.VideoCapture(r"C:/Users/dinyz/Dinesh Ram/Pycharm - Projects/Wildlife Animal Detection/test_videos/er2.webm")
model = YOLO("../Detection Pipeline/best.pt")  # Path to your trained model

while cap.isOpened():
    success, img =cap.read()
    if not success:
        break  # Exit if the video ends
    results=model(img)
    # Get the annotated frame with bounding boxes
    annotated_frame = results[0].plot()  #Use .plot() to visualize detections

    # Display the frame with detections
    cv2.imshow("YOLO Detection", annotated_frame)  #Show the correct image format

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()