import whisper

model = whisper.load_model("medium")
result = model.transcribe("begruessung.wav")
print(result["text"])
