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

Andernfalls kann man sich das Modell auch mit dem kleinen Hilfprogramm holen

```
python getTheModel.py

```


## Aufruf über die Kommandozeile

Man kann whisper auch als Kommando direkt aufrufen. 

```
whisper --model medium --model_dir . --output_format txt begruessung.wav

```

Alternativ ist hier ein shell-Script zu finden, das man so aufruft:

```
sh ./do_it.sh

```

## Referenz whisper OpenAI

Whisper gilt aktuell als der Goldstandard im Bereich der STT Systeme. Es ist ausgerichtet auf die Erfassung von langen Sprachaufnahmen. 

- https://github.com/openai/whisper
  

