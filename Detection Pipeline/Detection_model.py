from ultralytics import YOLO
import cv2

# Load your trained model
model = YOLO("../Detection Pipeline/best.pt")  # Path to your trained model

# Example: Load image for testing
img = cv2.imread(r"C:\Users\dinyz\Dinesh Ram\Pycharm - Projects\Wildlife Animal Detection\test_images\elephant road side.jfif")
#cap= cv2.VideoCapture()
#img=cap.read()
results = model(img)  # Inference

for result in results:
    boxes = result.boxes
    for box in boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        print(f"Detected: {model.names[cls_id]} with confidence {conf:.2f}")
results[0].show()  # Show detections
