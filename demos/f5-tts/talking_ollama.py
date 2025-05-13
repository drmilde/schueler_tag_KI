import ollama
from gradio_client import Client, handle_file
import shutil
import simpleaudio as sa
import re

def ask(text):
    prompt = f"""

    Bitte beantworte die folgende Frage kurz und kompakt. 

    FRAGE:{text}
    """

    ###################### 2) Konfiguration des Systems ##############################

    # System prompt: Hier beschreibt man genau, welche Rolle das System einnehmen soll. Das Verhalten.
    system_message = {
        "role": "system", 
        "content": "Du bist ein hilfreicher KI-Assistent, der dem Anwender Fragen beantworten soll."
    }

    # User prompt: Das ist die eigentliche Anfrage, die der Anwender an das System stellt.
    user_message = {
        "role": "user", 
        "content": f"{prompt}"
    }

    messages = [system_message, user_message]
    ## 3) Die eigentliche Anfrage an das LLM über ollama stellen

    result = ollama.chat(
        #model='llama3.2', 
        model='gemma3', 
        messages=messages
    )

    return(result)

    ## 4) Ausgabe des Antwort
    ## print("Ergebnis:", result['message']['content'])



#### Sprachausgabe
client = Client("http://127.0.0.1:7860/")

def speak(text: str):
    result = client.predict(
            ref_audio_input=handle_file('./reference/de_angelina_hoerbuch_kurz.wav'),
            ref_text_input=" Freitag Morgen. Zehn Uhr Dreißig. Stehe am Hauptbahnhof in Witten und warte auf die S-Bahn.",
            gen_text_input=f" {text}.",
            remove_silence=True,
            cross_fade_duration_slider=0.15,
            nfe_slider=12,
            speed_slider=1,
            api_name="/basic_tts"
    )
    source = result[0] 
    destination = './output.wav'
    shutil.move(source, destination)

    # for playing the audio file
    print(text)
    filename = destination
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing

##################### Ende Konfiguration ###############################


prompt = "\nGemma Chat"
prompt += " (enter '/bye’ to end the program.)"
prompt += "\n>>> "

message = ""
while message != "/bye":
    message = input(prompt)
    message = message.strip();
    if (message != "/bye"):
        text = ask(message)["message"]["content"]
        #print(text)

        # clean String
        text = text.strip()
        text = re.sub("\*\*", "", text)
        text = re.sub("!", " !", text)
        text = re.sub(r"\b1\.", "erstens: ", text)
        text = re.sub(r"\b2\.", "zweitens: ", text)
        text = re.sub(r"\b3\.", "drittens: ", text)
        text = re.sub(r"\b4\.", "viertens: ", text)
        text = re.sub(r"\b5\.", "fünftens: ", text)

        speak(text)


#################################

