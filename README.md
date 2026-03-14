# Room Reservation API

Eine asynchrone **FastAPI**-Anwendung zur Reservierung von Besprechungsräumen mit Benutzerverwaltung und optionalem Google-Sheets-Reporting.

## Überblick

Dieses Projekt stellt eine REST-API bereit, mit der man:

- Besprechungsräume anlegen, aktualisieren, anzeigen und löschen kann (Admin-Funktionen).
- Zeitfenster für Räume reservieren kann.
- Überschneidungen von Reservierungen verhindert.
- Eigene Reservierungen eines angemeldeten Benutzers abrufen kann.
- Einen Reservierungsbericht für einen Zeitraum in Google Sheets exportieren kann (Admin-Funktion).

## Kernfunktionen

- **Meeting-Room-Verwaltung** über `/meeting_rooms`.
- **Reservierungslogik** über `/reservations` inkl. Prüfung auf Zeitkonflikte.
- **Authentifizierung & Benutzer** über `fastapi-users` (JWT-Auth, Registrierung, Benutzer-Endpoints).
- **Google-Integration** über `/google` zur Erstellung eines Reports im Spreadsheet.
- **Asynchrone Datenbankanbindung** über SQLAlchemy (Standard: SQLite `fastapi.db`).

## Projektstruktur (Auszug)

- `app/main.py` – Einstiegspunkt der FastAPI-Anwendung.
- `app/api/endpoints/` – API-Endpunkte (Räume, Reservierungen, User, Google).
- `app/models/` – SQLAlchemy-Modelle.
- `app/schemas/` – Pydantic-Schemas für Request/Response.
- `app/crud/` – CRUD-Operationen und Datenzugriff.
- `app/api/validators.py` – Business-Validierungen (z. B. Konfliktprüfungen).
- `alembic/` – Datenbankmigrationen.

## Lokale Ausführung

### 1) Voraussetzungen

- Python 3.10+
- (Optional) Virtuelle Umgebung

### 2) Installation

```bash
pip install -r requirements.txt
```

> Hinweis: Für den Betrieb der API werden zusätzlich die im Projekt verwendeten FastAPI-/SQLAlchemy-Komponenten benötigt, falls sie nicht bereits in deiner Umgebung vorhanden sind.

### 3) Umgebungsvariablen

Die App liest Konfiguration aus `.env` (siehe `app/core/config.py`).
Wichtige Variablen sind u. a.:

- `APP_TITLE`
- `DATABASE_URL`
- `FIRST_SUPERUSER_EMAIL`
- `FIRST_SUPERUSER_PASSWORD`
- Google-Service-Credentials (`TYPE`, `PROJECT_ID`, `PRIVATE_KEY`, ...)

### 4) Migrationen ausführen (optional, empfohlen)

```bash
alembic upgrade head
```

### 5) Server starten

```bash
uvicorn app.main:app --reload
```

Danach ist die API typischerweise unter `http://127.0.0.1:8000` erreichbar.
Die interaktive Dokumentation findest du unter:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## Beispiel-Endpunkte

- `GET /meeting_rooms/` – Alle Räume abrufen.
- `POST /meeting_rooms/` – Raum anlegen (nur Superuser).
- `POST /reservations/` – Reservierung erstellen.
- `GET /reservations/my_reservations` – Eigene Reservierungen abrufen.
- `POST /google/` – Report für Zeitraum erzeugen (nur Superuser).

## Zweck des Projekts

Das Repository demonstriert eine praxisnahe FastAPI-Architektur mit Authentifizierung, asynchronem DB-Zugriff, Validierungslogik für Reservierungsintervalle und externer Service-Integration (Google API).
