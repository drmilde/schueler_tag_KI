from gradio_client import Client, handle_file
import argparse
import shutil

parser = argparse.ArgumentParser(description='Test mit F5-API')
parser.add_argument('-t','--text', help='Text, der gesprochen werden soll', default="Hallo, ich bin F5-TTS.", required=True)
parser.add_argument('-p', '--play_audio', dest='play_audio', action='store_true', help='Play audio.')
args = vars(parser.parse_args())


client = Client("http://127.0.0.1:7860/")
result = client.predict(
		ref_audio_input=handle_file('./reference/de_angelina_hoerbuch_kurz.wav'),
		ref_text_input=" Freitag Morgen. Zehn Uhr Dreißig. Stehe am Hauptbahnhof in Witten und warte auf die S-Bahn.",
		gen_text_input=f" {args['text']}.",
		remove_silence=True,
		cross_fade_duration_slider=0.15,
		nfe_slider=12,
		speed_slider=1,
		api_name="/basic_tts"
)
print(result[0])
       
source = result[0] 
destination = './output.wav'
shutil.move(source, destination)

# for playing the audio file
if (args["play_audio"]):
    print('Elsa sagt: ')

    import simpleaudio as sa

    filename = destination
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing
