# Bilderkennung mit TeachableMachines

Mit Teachablemachines lassen sich sehr schnell und einfach Demonstrationssysteme für die Erkennung von
Bildern, Sprache und Bewegungen erstellen. Die Modelle lassen sich herunterladen und in den eigenen Systemen einsetzen.


- https://teachablemachine.withgoogle.com/


## Prepare venv and install requirements.txt
```
deactivate
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

## Testen des Bildmodells


```
python keras_opencv.py

```


## Patch bei python version > 3.8

Sollte beim Starten der Anwendung ein Ladefehler angezeigt werden, der sich auf "groups" bezieht, dann muss dieser Eintrag während des Ladens
entfernt werden. 

Öffnet die Datei

```
 code ./venv/lib/python3.10/site-packages/keras/src/ops/operation.py

```
Fügt den folgenden code in Datei ein:

```
if "groups" in config:
    config.pop("groups")

```

!(operation.py.screenshot.png "Gepatchte Datei")






