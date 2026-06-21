# Progress Schema

## Markdown-Block

```markdown
## Fortschrittslog

Dokument: <Titel>
Aktuelle Sitzung: <Nummer>
Erledigt: <Liste>
Verstaendnis: <1-5>
Offene Fragen:
- ...
Schwierige Begriffe:
- ...
Naechster Schritt: ...
```

## YAML-Block

```yaml
progress:
  document: "<Titel>"
  completed_sessions:
    - session: 1
      title: "<Titel>"
      completed_at: "<Datum oder leer>"
      confidence_1_to_5: 4
  current_session: 2
  open_questions:
    - "<Frage>"
  difficult_terms:
    - term: "<Begriff>"
      status: "needs_review"
  next_recommendation: "Sitzung 2 hoeren und Checkfragen beantworten"
```

## Update-Regeln

- Nach jeder Sitzung kurz fragen: Was war klar? Was war unklar?
- Confidence nicht erzwingen; wenn unbekannt, leer lassen.
- Offene Fragen in der naechsten Sitzung wieder aufgreifen.
- Schwierige Begriffe nach Wiederholung als `reviewed` markieren.
