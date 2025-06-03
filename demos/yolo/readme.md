# Bilderkennung mit yolo


## Euro coco

Dieser kleine Datensatz zeigt, wie man den den kompletten Datenerfassungs-, Annotierungs- und Trainingsprozess mit yolo durchführen kann.
Mit gerade mal 13 Aufnahmen erreicht das System eine erstaunliche Qualität in der Erkennung der Münzen. Natürlich nicht perfekt,
aber überraschend gut für den geleisteten Aufwand.

## Installation

Das Übliche:

```
deactivate
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

## Labelstudio

Die Daten wurden mit Labelstudio annotiert

- https://github.com/HumanSignal/label-studio

## Training

Zum Training muss das zip-Archiv im Verzeichnis **datasets** expandiert werden. 

```
python erkenner.py

```

## Test mit Einzelbild

```
python test_model.py

```

## Test mit Live Cam

```
python test_live_cam.py

```



