from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Train the model on the COCO8 dataset for 100 epochs
train_results = model.train(
    data="euro_coco.yaml",  # Path to dataset configuration file
    epochs=200,  # Number of training epochs
    imgsz=1440,  # Image size for training
    device="mps",  # Device to run on (e.g., 'cpu', 0, [0,1,2,3])
)

# Evaluate the model's performance on the validation set
metrics = model.val()

# Perform object detection on an image
#results = model("path/to/image.jpg")  # Predict on an image
#results[0].show()  # Display results

# Export the model to ONNX format for deployment
path = model.export(format="onnx")  # Returns the path to the exported model
print (path)