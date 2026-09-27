# 🌟 Gemini AI Chat Assistant (Local Web App)

Eine einfache und moderne Webanwendung, um über einen lokalen HTTP-Server (`localhost:8000`) Fragen an die Google Gemini API zu stellen.

---

## 🏗️ Architektur & Ablauf

1. **Frontend (Browser):** HTML5 + CSS3 + Vanilla JavaScript unter `http://localhost:8000`.
2. **Backend (Python):** FastAPI Web-Server (`main.py`).
3. **Sicherheit:** Der `GEMINI_API_KEY` wird über die `.env`-Datei eingelesen und verlässt niemals deinen Rechner Richtung Browser.
4. **Verwaltung:** `uv` als ultraschneller Paket- und Umgebungsmanager (`.venv`, `pyproject.toml`, `uv.lock`).

---

## 🚀 Schnellstart

### 1. Gemini API-Key eintragen
Öffne die Datei [`.env`](file:///c:/Antigravity/Roni/Vibe%20Coding/Try1/.env) und trage deinen Google Gemini API-Key ein:
```env
GEMINI_API_KEY=AIzaSy...
```
*(Einen kostenlosen Key erhältst du in [Google AI Studio](https://aistudio.google.com/app/apikey).)*

### 2. Server starten
Starte den Server mit `uv`:
```bash
uv run main.py
```
*(Alternativ: `uv run uvicorn main:app --reload`)*

### 3. Im Browser öffnen
Öffne deinen Webbrowser unter:
👉 **[http://localhost:8000](http://localhost:8000)** oder **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 📁 Projektstruktur

```text
Try1/
├── .venv/                # Virtuelle Python-Umgebung (automatisch von uv verwaltet)
├── .env                  # Dein geheimer API-Key (wird von Git ignoriert)
├── .env.example          # Beispiel-Konfiguration
├── .gitignore            # Ignoriert .env, .venv, Cache-Dateien
├── pyproject.toml        # Projektkonfiguration & Abhängigkeiten
├── uv.lock               # Exakte Lockfile für reproduzierbare Builds
├── main.py               # FastAPI-Backend & Gemini-Integration
├── README.md             # Diese Anleitung
└── static/
    ├── index.html        # Web-Frontend (Eingabefeld, Button, Chat-Fenster)
    └── style.css         # Modernes Dark-Mode Chat-Styling
```
