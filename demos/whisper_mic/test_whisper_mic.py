from whisper_mic import WhisperMic

mic = WhisperMic(model="small", implementation="whisper")


result = mic.listen()
print(f"ergbenis ist: {result}")
