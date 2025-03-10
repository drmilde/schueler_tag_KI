# Import the required module for text  
# to speech conversion
import pyttsx3
import argparse

# hier kann man die Stimme ändern
def change_voice(engine, language, gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))
 


parser = argparse.ArgumentParser(description='Test von pyttx3')
parser.add_argument('-t','--text', help='text, der gesprochen werden soll', required=True)
args = vars(parser.parse_args())


# die Sprachsynthese wird initialisiert
engine = pyttsx3.init()

# Konfiguriere die Stimme
change_voice(engine, "de_DE", "VoiceGenderFemale")
engine.setProperty('rate', 185)
 
# Synthetisiere den gesprochenen Text
#engine.say('Guten Tag. Ich hoffe, es geht Euch gut.')
engine.say(args['text']) 


# hiermit startet die Verarbeitung
engine.runAndWait()
