# Einbinden von LLM in Pythoncode

In diesem Beispiel wird gezeigt, wie man ollama in eigenen Pythonanwendungen nutzen kann. 


## Prepare venv and install requirements.txt
```
deactivate
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```


## Öffnen von VSCode

```
code .

```

## llm_einbinden.py

Das Beispiel zeigt, wie man den Aufruf für ollama in python konfiguriert und durchführt. Bei LLMs unterscheidet
man das System-Prompt und den User Prompt. 

## chat_ollama.py

Nachbau der Eingabeschleife von Ollama. Mann stellt eine Frage, das System antwortet entsprechend seiner Konfiguration:  
eine Kombination aus System-Prompt und User-Prompt inklusive der gestellten Frage.







