# Kokoro TTS

Kokoro ist der aktuelle Stern am Himmel der TTS Systeme. Extrem klein, aber es bietet trotzdem eine unglaublich
gute Sprachqualität. 

- https://github.com/hexgrad/kokoro

## Prepare venv and install requirements.txt
```
deactivate
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

## Synthetisiere einen längeren Text

Hier werden eine Reihe von wav Dateien erzeugt, die man anschließen mit afplay wiedergeben kann. 

```
python do_speak.py
afplay 1.wav


```

## Start the Web interface

Im Web-Interface kann man die Stimme auswählen und text synthtisieren und wiedergeben.

```
python app.py


```

## Öffnen der Webanwendung

- http://0.0.0.0:40001
  


