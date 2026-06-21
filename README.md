# PDF Hoerbuch Lerncoach DE

Skill-Name: `pdf-hoerbuch-lerncoach-de`

## Beschreibung

Verwende diesen Skill, um hochgeladene PDF-Buecher, Handbuecher, Berichte, Kurse oder lange Dokumente in gefuehrte Vorlese- und hoerbuchartige Lernerlebnisse zu verwandeln: Struktur erkennen, Hoersitzungen planen, sprachfreundliche Vorleseskripte erstellen, Kapitel zusammenfassen, schwierige Passagen erklaeren, Lernfortschritt verfolgen und Voice Mode, Read Aloud oder externe TTS-Tools vorbereiten. Nicht verwenden fuer kurze Einzeltexte, reine PDF-Bearbeitung, urheberrechtlich geschuetzte Volltext-Reproduktion oder Aufgaben ohne audiobasiertes Lernziel.

## Nutzen

Dieser Skill macht aus einem hochgeladenen PDF-Buch, Handbuch, Bericht, Kurs oder langen Dokument ein gefuehrtes Audio-Lernerlebnis. Er erzeugt keine Audiodatei, sondern die Struktur, Skripte, Sitzungsplaene und Prompts, die in ChatGPT Voice Mode, Read Aloud oder externen TTS-Tools genutzt werden koennen.

## Typische Ergebnisse

- Audio-Lernkarte fuer das ganze Dokument
- Hoersitzungsplan mit 10- bis 30-Minuten-Einheiten
- sprachfreundliche Vorleseskripte
- 30-Sekunden-, 3-Minuten- und Vertiefungszusammenfassungen
- Erklaerungen schwieriger Passagen
- Mini-Quiz und Reflexionsfragen
- Fortschrittslog fuer mehrtaegiges Lernen
- TTS-freundliche Chunks fuer externe Tools

## Dateien

```text
pdf-hoerbuch-lerncoach-de/
|-- SKILL.md
|-- README.md
|-- agents/openai.yaml
|-- assets/
|   |-- progress-log-template.md
|   |-- session-plan-template.md
|   `-- voice-mode-starter-prompts.md
|-- references/
|   |-- audio-didaktik.md
|   |-- copyright-und-sicherheit.md
|   |-- progress-schema.md
|   `-- tts-style-guide.md
`-- scripts/
    |-- make_audio_learning_plan.py
    |-- split_tts_chunks.py
    `-- validate_audio_plan.py
```

## Beispielprompt

```text
Bitte verwandle dieses PDF in einen Hoersitzungsplan fuer 20 Minuten pro Sitzung. Erstelle zuerst eine Audio-Lernkarte, dann Sitzung 1 mit sprachfreundlichem Vorleseskript, Erklaerungen schwieriger Begriffe, Checkfragen und Fortschrittslog.
```

## Externe TTS-Nutzung

1. Erstelle zuerst eine Hoersitzung.
2. Nutze `split_tts_chunks.py`, um lange Skripte in Chunks zu teilen.
3. Kopiere die Chunks in ein TTS-Tool oder nutze ChatGPT Read Aloud.
4. Trage gehoerte Sitzungen im Fortschrittslog nach.

## Hinweis zu urheberrechtlich geschuetzten Texten

Der Skill ist fuer Lernen, Zusammenfassung, Erklaerung und gefuehrte Moderation gedacht. Er soll keine vollstaendigen copyrighted Buecher oder Kapitel als Ersatz-Hoerbuch reproduzieren.
