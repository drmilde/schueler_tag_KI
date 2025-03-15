# Spracherkennung mit Whisper



## Installation und Aktivierung des venv


```
deactivate
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

## Spracherkennung auf einer wav-Datei

```
python whisper_test.py

```

Beim ersten Aufruf sollte das Programm das verwendete Modell herunterladen (hier medium.pt). Leider kommt es dabei auf dem Mac immer mal wieder zu Problemen, da entsprechende Rechte nicht gesetzt wurde. Ihr könnt das Modell über den Browser runterladen und dann in das Verzeichnis kopieren.

