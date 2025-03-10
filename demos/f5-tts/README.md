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
- url(http://127.0.0.1:7860)


# Recording the reference audio

In order to work with the F5-TTS, you will nee to record a small audio sequence of the voice, that
should be synthesized.

- There is a file **"read_text,txt"** that you could read out.
- The recording can be done using **Audacity**.
- export the audio in WAV-format, mono, 16 kHz
- make sure, that the volume is good (use normalize volume effect in Audacity)
