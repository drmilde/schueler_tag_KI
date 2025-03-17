# Deep Live Cam


Mit DeepLiveCam kann man in Echtzeit (entsprechende Rechenleistung vorausgesetzt) Face Swapping machen.


- https://github.com/hacksider/Deep-Live-Cam


## Von Github runterladen und Installieren

```
git clone https://github.com/hacksider/Deep-Live-Cam.git
python3 -m venv venv
source venv/bin/activate
cd Deep-Live-Cam
pip install -r requirements.txt

```

## Modelle runterladen

Folgen Sie den Anweisungen im Verzeichenis und laden Sie die notwendigen Modell herunter:

- https://huggingface.co/hacksider/deep-live-cam/resolve/main/inswapper_128_fp16.onnx?download=true
- https://github.com/TencentARC/GFPGAN/releases/download/v1.3.4/GFPGANv1.4.pth

## Programm starten

```
python run.py

```
