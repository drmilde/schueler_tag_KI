# F5-TTS cloning voices

# Installation


## Prepare venv and install requirements.txt
```
deactivate
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```


# Quick start with Gradio web interface
```
f5-tts_infer-gradio

```

# This starts a webinterface

```
http://127.0.0.1:7860
```

(CMD+CLick opens a new tab): http://127.0.0.1:7860

# Recording the reference audio

In order to work with the F5-TTS, you will nee to record a small audio sequence of the voice, that
should be synthesized.

- There is a file **"read_text.txt"** that you could read out.
- The recording can be done using **Audacity**.
- export the audio in WAV-format, mono, 16 kHz
- make sure, that the volume is good (use normalize volume effect in Audacity)


# F5-TTS auf Deutsch

Normalerweise läuft F5-TTS auf Englisch. Sie können aber ein eigenes Modell erzeugen (über finetuning). 
Dazu gibt es entsprechende vorbereitete Scripte. Für die deutsche Sprache findet sich ein hervoragendes Modell
auf Huggingface unter der folgenden Adresse: 

- https://huggingface.co/aihpi/F5-TTS-German

Bitte laden Sie zwei Dateien herunter (das Modell und die Beschreibung der bekannten Zeichen/Grapheme)

model_295000.safetensors
  - https://huggingface.co/aihpi/F5-TTS-German/tree/main/F5TTS_Base

vocab.txt
  - https://huggingface.co/aihpi/F5-TTS-German/tree/main

## Verwendung in F5-TTS

Um das Model zu nutzen, schalten Sie in der Gradio Oberfläche von F5-TTS auf den Reiter "custom"
und 

1) geben dann die Pfade der Dateien in das jeweilige EIngabefeld ein. Leider ist das etwas umständlich.
2) Sie laden die Audio Referenz hoch
3) Unter "advanced" geben Sie den Text des Referenzaudios ein
4) Schliesslich können Sie zu synthetisierten Text ein und drücken den Button "synthesize"

 






# Referenz F5-TTS

Den Code zu dem F5-TTS Systeme findet man unter

- https://github.com/SWivid/F5-TTS
  
