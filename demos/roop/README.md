# Roop Face Swapping

Leicht veraltet, funktioniert abe noch und liefert relativ schnell Ergebnisse.

- https://github.com/s0md3v/roop


## Erzeuge ein Arbeitsverzeichnis

```
mkdir roop_face_swap
cd roop_face_swap

````


## Clone repository and prepare venv and install requirements.txt
```

git clone https://github.com/s0md3v/roop.git
deactivate
python3.10 -m venv venv
source venv/bin/activate
cd roop
pip install -r requirements.txt

```

## Run the GUI

```
python run.py

```

## Headless, also ohne GUI


```

python run.py -s bild_vom_gesicht.png -t video_auf_das_gemapped_wird.mp4 -o ergebnis_video.mp4


```
