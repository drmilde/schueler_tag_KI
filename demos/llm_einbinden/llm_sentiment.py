import ollama
import argparse

# 0) hier werden die Kommandozeilenargumente ausgewertet
parser = argparse.ArgumentParser(description='Test von ollama und python')
parser.add_argument('-t','--text', help='Kursbewertung, die eingeschätzt werden soll', required=True)
args = vars(parser.parse_args())
text = args["text"]


# 1) Konstruktion des strukturierten Prompts
prompt = f"""

#HIER MUSS EUER PROMPT ZUR ANALYSE HIN.

REVIEW:{text}
"""


###################### 2) Konfiguration des Systems ##############################

# System prompt: Hier beschreibt man genau, welche Rolle das System einnehmen soll. Es konfiguriert das Verhalten.
system_message = {
    "role": "system", 
    "content": "Du bist ein hilfreicher KI-Assistent, der eine Sentimentanalyse durchführen soll."
}

# User prompt: Das ist die eigentliche Anfrage, die der Anwender an das System stellt.
user_message = {
    "role": "user", 
    "content": f"{prompt}"
}

messages = [system_message, user_message]

##################### Ende Konfiguration ###############################


## 3) Die eigentliche Anfrage an das LLM über ollama stellen
result = ollama.chat(
    model='llama3.2', 
    messages=messages
)

## 4) Ausgabe des Antwort
print("Ergebnis:", result['message']['content'])
