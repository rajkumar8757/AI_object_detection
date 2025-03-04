from ultralytics import YOLO
import cv2

# Load YOLOv8 Model
model = YOLO("yolov8n.pt")

# Load Image
image_path = "test_image.jpg"
image = cv2.imread(image_path)

# Perform Object Detection
results = model(image)

# Draw Bounding Boxes
for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        label = result.names[int(box.cls[0])]
        confidence = box.conf[0].item()
        
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, f"{label} {confidence:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display Image
cv2.imshow("Object Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


