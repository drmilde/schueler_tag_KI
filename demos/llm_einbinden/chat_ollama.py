import ollama
import argparse

# 0) hier werden die Kommandozeilenargumente ausgewertet
parser = argparse.ArgumentParser(description='Test von ollama und python')
parser.add_argument('-t','--text', help='Kursbewertung, die eingeschätzt werden soll', required=True)
args = vars(parser.parse_args())
text = args["text"]

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


##################### Ende Konfiguration ###############################


prompt = "\nGemma Chat"
prompt += " (enter '/bye’ to end the program.)"
prompt += "\n>>> "

message = ""
while message != "/bye":
    message = input(prompt)
    message = message.strip();
    if (message != "/bye"):
        print(ask(message)["message"]["content"])


#################################

