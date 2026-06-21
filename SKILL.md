---
name: pdf-hoerbuch-lerncoach-de
description: Verwende diesen Skill, um hochgeladene PDF-Buecher, Handbuecher, Berichte, Kurse oder lange Dokumente in gefuehrte Vorlese- und hoerbuchartige Lernerlebnisse zu verwandeln: Struktur erkennen, Hoersitzungen planen, sprachfreundliche Vorleseskripte erstellen, Kapitel zusammenfassen, schwierige Passagen erklaeren, Lernfortschritt verfolgen und Voice Mode, Read Aloud oder externe TTS-Tools vorbereiten. Nicht verwenden fuer kurze Einzeltexte, reine PDF-Bearbeitung, urheberrechtlich geschuetzte Volltext-Reproduktion oder Aufgaben ohne audiobasiertes Lernziel.
---

# PDF Hoerbuch Lerncoach DE

## Zweck

Dieser Skill verwandelt hochgeladene PDF-Buecher, Handbuecher, Berichte, Kurse und andere lange Dokumente in ein gefuehrtes Vorlese- und hoerbuchartiges Lernerlebnis. Er erkennt die Dokumentstruktur, erstellt Hoersitzungen, bereitet sprachfreundliche Vorleseskripte vor, fasst Kapitel zusammen, erklaert schwierige Passagen, verfolgt Lernfortschritt und bereitet die Nutzung von ChatGPT Voice Mode, Read Aloud oder externen TTS-Tools vor.

Der Skill erzeugt normalerweise keine fertige Audiodatei. Er erstellt stattdessen strukturierte, sprechbare Skripte, Prompts und Lernplaene, die direkt vorgelesen oder in TTS-Tools uebernommen werden koennen.

## Wann verwenden

Verwende diesen Skill, wenn der Nutzer eines der folgenden Ziele hat:

- ein hochgeladenes PDF oder langes Dokument audiobasiert lernen
- aus einem Buch, Bericht, Kurs oder Handbuch Hoersitzungen erstellen
- Kapitel in sprechbare Lernskripte, Zusammenfassungen oder Voice-Mode-Prompts umwandeln
- schwierige Textstellen langsam, einfach und mit Beispielen erklaert bekommen
- Lernfortschritt, offene Fragen und Wiederholungen nachhalten
- eine dokumentbasierte Lernroutine fuer Read Aloud, Voice Mode oder externe Text-to-Speech-Tools vorbereiten

## Nicht verwenden

Nicht verwenden fuer:

- kurze Einzeltexte, bei denen ein normaler Chat ausreichend ist
- reine PDF-Bearbeitung wie Zusammenfuegen, Drehen, Wasserzeichen, Formularbefuellung oder Layout-Reparatur
- die vollstaendige oder nahezu vollstaendige Wiedergabe urheberrechtlich geschuetzter Buecher, Kapitel oder Kursmaterialien
- das Umgehen von Paywalls, DRM, Zugriffsbeschraenkungen oder Lizenzbedingungen
- medizinische, rechtliche, finanzielle oder sicherheitskritische Entscheidungen ohne professionelle Pruefung
- Aufgaben ohne audiobasiertes Lernziel

## Erforderliche Eingaben

Falls vorhanden, ermittle:

- Dokument oder Dokumentauszug
- gewuenschter Umfang: gesamtes Dokument, Kapitel, Seitenbereich oder Thema
- Lernziel: Ueberblick, Pruefungsvorbereitung, praktische Anwendung, Wiederholung oder tiefes Verstehen
- Zielmodus: ChatGPT Voice Mode, Read Aloud, externer TTS-Dienst oder stilles Mitlesen
- gewuenschte Sitzungslaenge, z. B. 10, 20 oder 30 Minuten
- Sprachniveau und Stil: einfach, akademisch, locker, sachlich, motivierend
- Fortschrittsstatus: bereits gehoerte Sitzungen, offene Fragen, schwierige Begriffe

Wenn Angaben fehlen, nutze sinnvolle Defaults: 20-Minuten-Sitzungen, klares Deutsch, kurze TTS-freundliche Absaetze, aktive Lernfragen und ein kompakter Fortschrittsblock.

## Arbeitsablauf

### 1. Dokument triagieren

- Erkenne Titel, Autor oder Quelle, wenn sichtbar.
- Bestimme Dokumenttyp: Buch, Handbuch, Bericht, Kurs, Paper, Skript oder gemischtes Material.
- Identifiziere Inhaltsverzeichnis, Kapitel, Abschnitte, Seitenbereiche, Tabellen, Abbildungen und Anhaenge.
- Markiere unklare Bereiche, fehlende Seiten, Scan- oder OCR-Probleme.
- Bei langen Dokumenten zuerst eine Lernkarte erstellen, nicht sofort das ganze Dokument umschreiben.

### 2. Lernkarte erstellen

Erzeuge eine kompakte Lernkarte mit:

- Hauptteilen und Kapitelstruktur
- Kernfragen des Dokuments
- empfohlenem Lernpfad
- ungefaehrer Schwierigkeit je Abschnitt
- Vorschlag fuer Hoersitzungen
- Stellen, die visuell statt rein auditiv gelernt werden sollten, z. B. Tabellen, Formeln oder Diagramme

### 3. Hoersitzungen planen

Teile den Stoff in kleine, abschliessbare Sitzungen. Jede Sitzung soll enthalten:

- Sitzungsnummer und Titel
- Seiten- oder Kapitelbereich
- Lernziel in einem Satz
- geschaetzte Dauer
- Vorwissen oder Begriffe, die vorab geklaert werden sollten
- Hoerablauf mit Orientierung, Hauptteil, Pausen und Abschluss
- Mini-Quiz oder Reflexionsfragen
- Empfehlung fuer Wiederholung

### 4. Sprachfreundliches Vorleseskript schreiben

Schreibe nicht wie in einem gedruckten Skript, sondern wie fuer die Stimme:

- kurze Saetze und klare Abschnitte
- natuerliche Ueberleitungen
- Begriffe zuerst ankündigen, dann erklaeren
- Tabellen, Listen und Formeln in gesprochene Sprache umwandeln
- visuelle Inhalte beschreiben und sagen, wann der Nutzer ins Dokument schauen sollte
- Pausenmarken einfuegen, z. B. `[Pause: 5 Sekunden]`
- Zwischenfragen einbauen, z. B. `Was ist die zentrale Idee dieses Abschnitts?`
- keine Fussnoten-, Quellen- oder Seitenzahlenflut im Vorlesefluss

### 5. Schwierige Passagen erklaeren

Fuer schwierige Stellen nutze das Muster:

1. **Kernaussage:** Was wird behauptet?
2. **Einfach erklaert:** Was heisst das in normaler Sprache?
3. **Warum wichtig:** Welche Rolle spielt die Stelle im Kapitel?
4. **Beispiel oder Analogie:** Ein konkretes Bild oder Mini-Szenario.
5. **Hoerhinweis:** Worauf soll der Nutzer beim erneuten Hoeren achten?

### 6. Kapitel zusammenfassen

Erstelle Kapitelzusammenfassungen in drei Tiefen:

- **30-Sekunden-Version:** fuer schnelle Wiederholung
- **3-Minuten-Version:** fuer normales Hoeren
- **Vertiefung:** fuer Pruefung, Anwendung oder Diskussion

### 7. Fortschritt verfolgen

Fuehre einen Fortschrittsblock, wenn der Nutzer mit mehreren Sitzungen arbeitet:

```yaml
progress:
  document: "<Titel oder Dateiname>"
  completed_sessions: []
  current_session: 1
  confidence_1_to_5: null
  open_questions: []
  difficult_terms: []
  next_recommendation: "Sitzung 1 starten"
```

Aktualisiere diesen Block nach jeder Sitzung, wenn der Nutzer Antworten, Notizen oder neue Fragen gibt.

### 8. Voice Mode, Read Aloud und externe TTS vorbereiten

Gib je nach Zielmodus aus:

- **Voice Mode:** kurze Moderationsprompts und dialogische Lernfragen
- **Read Aloud:** sauber gegliederte Textbloecke mit natuerlicher Interpunktion
- **Externes TTS:** Chunks mit stabilen Ueberschriften, ohne komplexe Tabellen und ohne ueberlange Absaetze

## Urheberrecht und Quellenumgang

- Gib keine ganzen urheberrechtlich geschuetzten Kapitel, Buecher oder langen Passagen als Vorleseskript wieder.
- Erstelle stattdessen paraphrasierte Lernskripte, Zusammenfassungen, Erklaerungen, Lernfragen und eigene Moderation.
- Verwende kurze Zitate nur, wenn sie fuer die Erklaerung notwendig sind.
- Wenn der Nutzer eigenes Material hochlaedt, darf es verarbeitet werden, aber die Ausgabe sollte weiterhin lernorientiert und nicht bloss eine Volltextkopie sein.
- Bei gemeinfreien oder eindeutig selbst erstellten Materialien kann die Ausgabe ausfuehrlicher sein; achte trotzdem auf TTS-Nutzbarkeit.

## Ausgabeformate

### Standardausgabe fuer ein neues Dokument

```markdown
# Audio-Lernkarte
## Dokumentstruktur
## Empfohlener Hoerpfad
## Hoersitzungsplan
## Start: Sitzung 1
## Fortschrittslog
```

### Standardausgabe fuer eine Sitzung

```markdown
# Hoersitzung <Nummer>: <Titel>
Dauer: <Minuten>
Ziel: <ein Satz>

## 1. Orientierung
## 2. Vorleseskript
## 3. Schwierige Stellen einfach erklaert
## 4. Kurzzusammenfassung
## 5. Checkfragen
## 6. Naechster Schritt
```

### Kompakte Ausgabe

Wenn der Nutzer wenig Zeit hat, liefere nur:

1. Hoerziel
2. 5-Minuten-Zusammenfassung
3. drei Kernbegriffe
4. drei Prueffragen
5. naechste empfohlene Sitzung

## Qualitaetscheck

Vor der finalen Antwort pruefen:

- Ist die Ausgabe sprechbar, nicht nur lesbar?
- Sind lange Absaetze in TTS-freundliche Bloecke geteilt?
- Sind visuelle Inhalte auditiv erklaert oder als Blick-ins-Dokument-Hinweis markiert?
- Ist der Fortschritt nachvollziehbar?
- Wurde urheberrechtlich geschuetzter Volltext nicht unnoetig reproduziert?
- Gibt es einen klaren naechsten Schritt?
