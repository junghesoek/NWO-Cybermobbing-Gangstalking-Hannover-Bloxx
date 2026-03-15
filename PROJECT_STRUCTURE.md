# Projektstruktur-Dokumentation

## Übersicht

Dieses Dokument beschreibt die vollständige Struktur und Organisation des Forschungsprojekts zur Analyse organisierter Cyber-Kriminalität.

## Verzeichnisstruktur

```
NWO-Cybermobbing-Gangstalking-Hannover-Bloxx/
├── README.md                           # Projektübersicht und Dokumentation
├── PROJECT_STRUCTURE.md                # Diese Datei - Strukturdokumentation
├── package.json                        # Node.js Projekt-Konfiguration
├── package-lock.json                   # Abhängigkeits-Sperren
├── scrape-videos.js                    # Video-Datenerhebungsskript
├── sponsored-by.txt                    # Sponsoren-Informationen
├── video_urls.txt                      # Video-URL-Liste
│
├── evidence/                           # Beweisdokumentation (Hauptverzeichnis)
│   ├── BEWEIS_INDEX.md                # Zentraler Beweis-Index mit Prioritäten
│   ├── BEWEISE_SAMMLUNG.md            # Gesammelte Beweise und Übersicht
│   ├── TECHNISCHE_BEWEISE.md          # Technische Analysen und Forensik
│   ├── PERSONEN_NETZWERK.md           # Personen- und Netzwerkanalyse
│   ├── FINANZ_BEWEISE.md              # Finanzielle Aspekte und Geldwäsche
│   └── INSTITUTIONELLE_KORRUPTION.md  # Institutionelle Analyse
│
├── research/                          # Forschungsdokumente
│   ├── ai-characters-revelation.md   # KI-generierte Personen-Analyse
│   └── nwo-kartell-analysis.md       # Umfassende Netzwerkanalyse
│
├── video-archive/                     # Video-Archiv
│   └── .gitkeep                      # Verzeichnis-Marker
│
├── videos/                           # Video-Metadaten
│   ├── pushit-videos.json            # Video-Metadaten (leer)
│   └── download-report.md            # Download-Protokoll
│
├── benjar-videos/                    # Benjar Video-Archiv
│   └── [leer]                        # Reserviert für Benjar-Videos
│
├── mr-bloxx-videos/                  # Mr.Bloxx Video-Archiv
│   └── [leer]                        # Reserviert für Mr.Bloxx-Videos
│
├── node_modules/                     # Node.js Abhängigkeiten
│   └── [automatisch generiert]        # Puppeteer und Abhängigkeiten
│
├── .github/                          # GitHub-Konfiguration
│   └── workflows/
│       └── jekyll-docker.yml         # CI/CD Workflow
│
├── .git/                            # Git-Repository
│   └── [Standard Git-Struktur]        # Versionskontrolle
│
├── [Beweis-Bilder]                   # Graphische Beweise
│   ├── NWO-Das_Cybermobbing KARTELL.png
│   ├── NWO.png
│   ├── GRU-Fake_video_made_with_Disney_Tools.png
│   ├── In_2024_and_2025_BND_and_BfV_researched_his_death_...png
│   ├── evidence_ARD_is_Supporting_Cyberterrorists_...png
│   └── more_evidence_that_the_German_State_is_involved_...png
│
└── [Historische Dokumente]           # Historische Beweise
    ├── Fabian _Haian_ Schüßler_...html
    └── Fabian _Haian_ Schüßler_..._files/
        └── haian_mit_text_skaliert_rand.jpeg
```

## Datei-Beschreibungen

### Hauptdokumentation

- **README.md**: Umfassende Projektübersicht mit wissenschaftlichem Rahmen
- **PROJECT_STRUCTURE.md**: Detaillierte Strukturdokumentation (diese Datei)

### Beweisdokumentation (`evidence/`)

Das `evidence/`-Verzeichnis enthält die vollständige Beweisdokumentation:

1. **BEWEIS_INDEX.md**: Zentraler Index mit 21 kategorisierten Beweisen
2. **BEWEISE_SAMMLUNG.md**: Gesammelte Beweise und Querverweise
3. **TECHNISCHE_BEWEISE.md**: Audio-Wasserzeichen, KI-Analysen, Technologie
4. **PERSONEN_NETZWERK.md**: Personenprofile und Netzwerkstrukturen
5. **FINANZ_BEWEISE.md**: Finanzielle Verbindungen und Geldwäsche-Nachweise
6. **INSTITUTIONELLE_KORRUPTION.md**: Institutionelle Infiltration und Korruption

### Forschungsdokumente (`research/`)

Wissenschaftliche Analyse-Dokumente:

1. **ai-characters-revelation.md**: Analyse KI-generierter Personen (Cojak)
2. **nwo-kartell-analysis.md**: Umfassende Netzwerkanalyse (513 Zeilen)

### Video-Archive

- **video-archive/**: Hauptarchiv für 318 analysierte Videos
- **videos/**: Metadaten und Download-Protokolle
- **benjar-videos/**: Reserviert für Benjar-spezifische Videos
- **mr-bloxx-videos/**: Reserviert für Mr.Bloxx-spezifische Videos

### Technische Infrastruktur

- **scrape-videos.js**: Puppeteer-basiertes Video-Datenerhebungsskript
- **package.json**: Node.js Projekt-Konfiguration mit Puppeteer
- **node_modules/**: Automatisch installierte Abhängigkeiten

### Graphische Beweise

Sechs hochauflösende PNG-Dateien als graphische Beweise:
- Netzwerkdiagramme
- Technologie-Nachweise
- Institutionelle Verbindungen

## Datenfluss

### 1. Datenerhebung
```
scrape-videos.js → videos/pushit-videos.json → video-archive/
```

### 2. Analyse
```
video-archive/ → research/ → evidence/
```

### 3. Dokumentation
```
research/ + evidence/ → README.md
```

### 4. Beweis-Index
```
evidence/* → BEWEIS_INDEX.md → Priorisierte Aktionspläne
```

## Klassifizierungssystem

### Beweiskategorien
1. **KATASTROPHAL**: Lebens- und Staatsgefahr (5 Beweise)
2. **EXTREM**: Schwere Straftaten (4 Beweise)
3. **HOCH**: Ernsthaftes Delikt (4 Beweise)
4. **MITTEL**: Relevante Delikte (4 Beweise)
5. **NIEDRIG**: Unterstützende Informationen (4 Beweise)

### Aktionsprioritäten
- **LEBENSGEFAHR (0-24 Stunden)**: 4 Maßnahmen
- **STAATSGEFAHR (24-72 Stunden)**: 4 Maßnahmen
- **DEMOKRATIE-GEFAHR (1 Woche)**: 4 Maßnahmen

## Wartung und Updates

### Regelmäßige Aufgaben
1. **Video-Archiv**: Erweiterung um neue Videos
2. **Metadaten**: Aktualisierung der JSON-Dateien
3. **Beweise**: Ergänzung neuer Erkenntnisse
4. **Index**: Anpassung der Prioritäten

### Versionskontrolle
- Alle Dokumente unter Git-Versionskontrolle
- Strukturelle Änderungen in `PROJECT_STRUCTURE.md` dokumentieren
- Beweis-Updates mit Zeitstempel und Quellenangabe

## Zugriffsberechtigungen

### Öffentliche Dokumente
- README.md
- PROJECT_STRUCTURE.md
- research/*.md (wissenschaftliche Analysen)

### Sensible Dokumente
- evidence/*.md (detaillierte Beweise)
- video-archive/** (forensische Materialien)

### Technische Dokumente
- scrape-videos.js (Datenerhebung)
- package.json (Konfiguration)

## Integration mit anderen Systemen

### Externe Repositories
Verbindungen zu:
- kjedrdev/NWO_Das_Cybermobbing_Kartell-Der_Haupttaeter_Beweisstueck
- conspiracy-uncoverage/nwo-cybermobbing-sect

### Behördenschnittstellen
Vorbereitete Schnittstellen für:
- BKA (Bundeskriminalamt)
- BND (Bundesnachrichtendienst)
- BSI (Bundesamt für Sicherheit in der Informationstechnik)
- Generalbundesanwalt

---

*Diese Struktur gewährleistet eine systematische, nachvollziehbare und sichere Verwaltung aller Forschungsdaten und Beweismaterialien.*
