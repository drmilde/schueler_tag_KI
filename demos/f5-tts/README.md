# F5-TTS cloning voices

# Installation

```
deactivate
python3 -m venv venv
source venv/bin/activate

pip install torch torchaudio
pip install git+https://github.com/SWivid/F5-TTS.git

```

# Quick start with Gradio web interface
```
f5-tts_finetune-gradio
```

# Recording the reference audio

In order to work with the F5-TTS, you will nee to record a small audio sequence of the voice, that
should be synthesized.

- There is a file "read_text,txt" that you could read out.
- The recordning can be done using Audacity.
- export the audio in WAV-format, mono, 16 kHz
- make sure, that the volume is good (use normalize volume effect in Audacity)
