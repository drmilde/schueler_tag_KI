from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("best.pt")

# Perform object detection on an image
results = model("test_images/test_euro_22.jpg")  # Predict on an image
results[0].show()  # Display results
