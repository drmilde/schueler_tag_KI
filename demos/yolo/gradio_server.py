import gradio as gr
import PIL.Image as Image

from ultralytics import ASSETS, YOLO

model = YOLO("best.pt")

def predict_image(img, conf_threshold, iou_threshold):
    """Predicts objects in an image using a YOLO11 model with adjustable confidence and IOU thresholds."""
    results = model.predict(
        source=img,
        conf=conf_threshold,
        iou=iou_threshold,
        show_labels=True,
        show_conf=True,
        imgsz=640,
    )

    for r in results:
        im_array = r.plot()
        im = Image.fromarray(im_array[..., ::-1])

    return im


iface = gr.Interface(
    fn=predict_image,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Slider(minimum=0, maximum=1, value=0.25, label="Confidence threshold"),
        gr.Slider(minimum=0, maximum=1, value=0.45, label="IoU threshold"),
    ],
    outputs=gr.Image(type="pil", label="Result"),
    title="Ultralytics Gradio",
    description="Hier kann man Bilder zum Testen hochladen. Unser trainiertes best,pr model wird verwendet.",
    examples=[
        ["test_images" "/test_euro_20.jpg", 0.6, 0.1],
        ["test_images" "/test_euro_21.jpg", 0.5, 0.3],
    ],
)

if __name__ == "__main__":
    iface.launch()