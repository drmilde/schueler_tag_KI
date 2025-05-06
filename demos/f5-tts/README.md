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


# F5-TTS auf Deutsch

Normalerweise läuft F5-TTS auf Englisch. Sie können aber ein eigenes Modell erzeugen (über finetuning). 
Dazu gibt es entsprechende vorbereitete Scripte. Für die deutsche Sprache findet sich ein hervoragendes Modell
auf Huggingface unter der folgenden Adresse: 


- https://huggingface.co/aihpi/F5-TTS-German
  


# Recording the reference audio

In order to work with the F5-TTS, you will nee to record a small audio sequence of the voice, that
should be synthesized.

- There is a file **"read_text.txt"** that you could read out.
- The recording can be done using **Audacity**.
- export the audio in WAV-format, mono, 16 kHz
- make sure, that the volume is good (use normalize volume effect in Audacity)

# Referenz F5-TTS

Den Code zu dem F5-TTS Systeme findet man unter

- https://github.com/SWivid/F5-TTS
  
