import ssl
import whisper

ssl._create_default_https_context = ssl._create_unverified_context

model = whisper.load_model("small")
