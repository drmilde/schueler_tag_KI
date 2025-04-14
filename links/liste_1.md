## Software

- brew
- espeak-ng
- ffmpeg
- sox
- cmake
- automake
- g++
  
## Kursstruktur

Zeitplanung ... In Summe 145 Minuten

1) Einführung 35 min :
  - Anmeldung Rechner 10 min
  - Begrüßung und Motivation 10 min
  - KI LLM Theorie 15 min

2) Praxis 70 min :

  - Bilder mit Foocus 20 min
  - Bilderkennung mit Mediapipe 10 min
  - Geräusche erkennen mit yamnet 10 min
  - Modell trainieren mit Techable Machines 15 min
  - Stimme clonen 15 min

3) Ethik und KI 15 min

4) Lernen mit KI 20 min

5) Zusammenfassung 5 min



Ich brauche ein Konzept für einen 2 h Kurs für Informatik Schüler der 12. Klasse eines Gymnasiums in dem ich die Grundlagen aktueller KI zeige. Es geht nicht darum aktuelle Algorithmen zu erklären, sondern ich möchte anwendungsorientiert zu erläutern, welche Möglichkeiten KI in unterschiedlichen Anwendungsbereichen hat. Es soll einfache praktische Übungen geben in den mit vorgegebenem  Python Code für KI experimentiert wird. Ich will yolo, foocus, yamnet, Ollama, zonos, hedra, whisper, sam2, molmo als Beispiele kurz zeigen. Schließlich will ich über die ethishen und gesellschaftlichen Auswirkungen diskutieren.

Absolut! Hier ist ein Konzept für einen 2-stündigen Kurs, der Schülern der 12. Klasse eines Gymnasiums die Grundlagen aktueller KI vermittelt, ohne tief in die Algorithmen einzutauchen:
Kursziel:
* Schüler sollen ein grundlegendes Verständnis für die Möglichkeiten und Anwendungsbereiche aktueller KI-Technologien entwickeln.
* Sie sollen durch praktische Übungen mit vorgefertigtem Python-Code ein Gefühl für die Funktionsweise von KI bekommen.
* Sie sollen sich der ethischen und gesellschaftlichen Auswirkungen von KI bewusst werden und diese kritisch reflektieren können.
Kursaufbau:
1. Einführung (15 Minuten)
* Was ist KI? Eine einfache, anwendungsbezogene Definition.
* Kurzer Überblick über die Entwicklung der KI (von den Anfängen bis heute).
* Warum ist KI aktuell so relevant? (Datenexplosion, Rechenleistung, Algorithmen).
* Vorstellung der verschiedenen Anwendungsbereiche (Bilderkennung, Spracherkennung, Textgenerierung, etc.).
2. Anwendungsbereiche und praktische Übungen (60 Minuten)
* Bilderkennung (YOLO, Foocus, SAM2):
  * Kurze Erklärung, was Objekterkennung ist und wo sie eingesetzt wird (z.B. autonome Fahrzeuge, Überwachung).
  * Praktische Übung: Vorgefertigten Python-Code nutzen, um Bilder zu analysieren und Objekte zu erkennen.
  * Foocus: Bildgeneration.
  * SAM2: Segmentierung von Bildern.
* Spracherkennung und -verarbeitung (Whisper, Yamnet, Ollama):
  * Erläuterung, wie Spracherkennung funktioniert und welche Anwendungen es gibt (z.B. Sprachassistenten, Transkription).
  * Praktische Übung: Audioaufnahmen analysieren und transkribieren lassen.
  * Yamnet: Erkennung von Geräuschen.
  * Ollama: Lokales Sprachmodell.
* Textgenerierung und -analyse (Molmo, Hedra, Zonos):
  * Vorstellung von Anwendungen wie Chatbots, Textzusammenfassung und automatischer Übersetzung.
  * Praktische Übung: Texte generieren oder analysieren lassen.
  * Hedra: Generierung von Code.
  * Zonos: Verarbeitung von großen Textmengen.
  * Molmo: Multimodales KI-Modell.
* Wichtig: Bei den praktischen Übungen den Fokus auf das Ausprobieren und Experimentieren legen, nicht auf das Verständnis des Codes im Detail.
3. Ethische und gesellschaftliche Auswirkungen (30 Minuten)
* Diskussion über Themen wie:
  * Datenschutz und Überwachung.
  * Arbeitsplatzverlust durch Automatisierung.
  * Verantwortung und Bias in KI-Systemen.
  * Deepfakes und Desinformation.
  * Künstliche Intelligenz im Krieg.
* Offene Fragerunde und Diskussion.
4. Zusammenfassung und Ausblick (15 Minuten)
* Kurze Zusammenfassung der wichtigsten Erkenntnisse.
* Ausblick auf zukünftige Entwicklungen im Bereich der KI.
* Möglichkeiten für Schüler, sich weiter mit KI zu beschäftigen (z.B. Online-Kurse, Projekte).
Materialien:
* Präsentation mit anschaulichen Beispielen und Bildern.
* Vorgefertigte Python-Code-Snippets für die praktischen Übungen (z.B. Jupyter Notebooks).
* Beispielbilder und Audioaufnahmen für die Übungen.
* Materialien für die ethische Diskussion (z.B. Artikel, Videos).
Hinweise:
* Den Kurs interaktiv gestalten und die Schüler aktiv einbeziehen.
* Komplexe technische Details vermeiden und stattdessen auf anschauliche Beispiele setzen.
* Die ethische Diskussion offen und kontrovers führen.
Ich hoffe, dieses Konzept hilft Ihnen bei der Vorbereitung Ihres Kurses!


## Ethik: Einkaufen mit Bonus-App

Wie kann man Gradient Boost einsetzten um die Einkäufe von Menschen so, auszuwerten, dass man deren Lebensgewohnheiten Vorhersagen kann. Kann das System selbständig Gewohnheiten finden ? Welche Daten muss ich dazu bereitstellen?

1. Grundprinzip von Gradient Boosting:
* Gradient Boosting ist ein Machine-Learning-Algorithmus, der mehrere "schwache" Modelle (meist Entscheidungsbäume) kombiniert, um ein starkes Vorhersagemodell zu erstellen.
* Der Algorithmus arbeitet iterativ: Jedes neue Modell korrigiert die Fehler des vorherigen Modells, wodurch die Vorhersagegenauigkeit schrittweise verbessert wird.
* Durch die Fähigkeit, komplexe, nichtlineare Beziehungen in den Daten zu erkennen, eignet sich Gradient Boosting gut für die Analyse von Einkaufsmustern.
2. Anwendung auf Einkaufsmuster:
* Datenerfassung:
  * Zunächst werden umfangreiche Daten über die Einkäufe der Kunden gesammelt.
  * Diese Daten können Informationen wie gekaufte Produkte, Kaufzeitpunkte, Einkaufshäufigkeit, Einkaufswert und Filialstandorte enthalten.
  * Zusätzlich können demografische Daten (Alter, Geschlecht, Wohnort) und externe Daten (Wetter, Feiertage) einbezogen werden.
* Datenvorverarbeitung:
  * Die Rohdaten werden bereinigt und in ein geeignetes Format für den Algorithmus umgewandelt.
  * Dies kann die Umwandlung von Textdaten in numerische Daten, die Behandlung fehlender Werte und die Erstellung neuer Merkmale (z. B. "Wochentag des Einkaufs") umfassen.
* Modelltraining:
  * Der Gradient-Boosting-Algorithmus wird mit den vorbereiteten Daten trainiert.
  * Das Modell lernt, Muster in den Einkaufsdaten zu erkennen und diese mit bestimmten Lebensgewohnheiten in Verbindung zu bringen.
  * Beispielsweise könnte das Modell feststellen, dass Kunden, die regelmäßig Bio-Produkte kaufen, tendenziell einen gesunden Lebensstil pflegen.
* Vorhersage von Lebensgewohnheiten:
  * Nach dem Training kann das Modell verwendet werden, um die Lebensgewohnheiten neuer Kunden auf der Grundlage ihrer Einkäufe vorherzusagen.
  * Dies kann für verschiedene Zwecke genutzt werden, z. B. für personalisierte Marketingkampagnen oder zur Verbesserung des Produktangebots.
3. Selbstständige Erkennung von Gewohnheiten:
* Gradient-Boosting-Modelle können in gewissem Maße selbstständig Gewohnheiten erkennen.
* Durch die Analyse der Daten können sie Muster und Zusammenhänge aufdecken, die für den Menschen möglicherweise nicht offensichtlich sind.
* Allerdings ist die Interpretation der Ergebnisse oft komplex und erfordert Fachwissen.
* Zusätzlich ist es wichtig zu beachten, dass die Modelle nur Korrelationen und keine Kausalitäten erkennen können.
* Die Modelle können durch die Feature importance ausgeben, welche Datenpunkte besonders wichtig für die vorhersage sind.
4. Benötigte Daten:
* Einkaufsdaten:
  * Produkte (Name, Kategorie, Marke)
  * Kaufzeitpunkt (Datum, Uhrzeit)
  * Einkaufshäufigkeit
  * Einkaufswert
  * Filialstandort
* Kundendaten:
  * Alter
  * Geschlecht
  * Wohnort
  * Kundenkarteninformationen
* Externe Daten:
  * Wetterdaten
  * Feiertage
  * Veranstaltungen
5. Ethische Überlegungen:
* Die Analyse von Einkaufsmustern wirft wichtige Fragen zum Datenschutz und zur Privatsphäre auf.
* Es ist wichtig, sicherzustellen, dass die Daten verantwortungsbewusst und im Einklang mit den geltenden Gesetzen verwendet werden.
* Zudem muss man sich bewusst sein, dass die Modelle Vorurteile enthalten können, die in den Trainingsdaten vorhanden sind.
Ich hoffe, diese Informationen sind hilfreich.


## Links


- https://www.kdnuggets.com/creating-useful-voice-activated-fully-local-rag-system
- https://towardsdatascience.com/build-a-decision-tree-in-polars-from-scratch/
- https://www.heise.de/news/Twister-Aufklaerungsdrohne-KI-Sensor-lokalisiert-Artilleriefeuer-nach-Geraeusch-10279259.html
- https://github.com/christianwarmuth/openhpi-kipraxis
- https://medium.com/@atulkumar_68871/building-a-streaming-speech-to-text-application-with-fastapi-and-amazon-transcribe-6203d857375a
- https://www.kdnuggets.com/building-multilingual-applications-hugging-face-transformers
- https://www-marktechpost-com.cdn.ampproject.org/v/s/www.marktechpost.com/2025/02/20/building-an-ideation-agent-system-with-autogen-create-ai-agents-that-brainstorm-and-debate-ideas/?amp=&amp_gsa=1&amp_js_v=a9&usqp=mq331AQGsAEggAID#amp_tf=Von%20%251%24s&aoh=17402070205131&csi=0&referrer=https%3A%2F%2Fwww.google.com&ampshare=https%3A%2F%2Fwww.marktechpost.com%2F2025%2F02%2F20%2Fbuilding-an-ideation-agent-system-with-autogen-create-ai-agents-that-brainstorm-and-debate-ideas%2F
- https://huggingface.co/NousResearch/DeepHermes-3-Llama-3-3B-Preview-GGUF
- https://www.iese.fraunhofer.de/blog/large-action-models-multi-agents/
- https://www.derstandard.at/story/3000000260977/ki-agenten-ai-agents?ref=niewidget
- https://t3n.de/news/ki-fuer-den-matheunterricht-warum-forschende-die-blickrichtungen-von-schulkindern-analysieren-1678948/
- https://github.com/hacksider/Deep-Live-Cam
- https://huggingface.co/spaces/hesamation/primer-llm-embedding?section=what_makes_a_good_embedding?
- https://admantium.medium.com/llm-agents-multi-agent-chats-with-autogen-6c82e89f618e
- 

