# coqui TTS 

Ein weiteres TTS, diesmal mit einer deutschen Stimme: Thorsten. Nein, nicht meine Stimme, sondern Thorsten Müller,
der sich enthusiastisch mit TTS beschäftigt und zudem aus Hessen kommt.

- https://github.com/thorstenMueller/Thorsten-Voice?tab=readme-ov-file


## Prepare venv and install requirements.txt
```
deactivate
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

## Sage etwas (generiert die Datei output.wav)

```
python do_speak.py -t "Hallo Zusammen. ich freue mich, dass ihr hier seid."
afplay output.wav

```

## Kunst und Kultur ist wichtig

```
sh ./abschied_goethe.sh

```
