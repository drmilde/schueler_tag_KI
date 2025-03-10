import torch
import argparse
from TTS.api import TTS


parser = argparse.ArgumentParser(description='Test von pyttx3')
parser.add_argument('-t','--text', help='text, der gesprochen werden soll', required=True)
args = vars(parser.parse_args())

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS with the target model name
tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=False).to(device)

# Run TTS
tts.tts_to_file(text=args['text'], file_path="output.wav")
