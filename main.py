import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from google import genai
from google.genai.errors import APIError

# Lade Umgebungsvariablen aus der .env-Datei
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

app = FastAPI(title="Gemini Chat Assistant")

# Statische Dateien (HTML, CSS, JS) einbinden
static_dir = Path(__file__).resolve().parent / "static"
static_dir.mkdir(exist_ok=True)
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    reply: str


@app.get("/")
async def get_index():
    """Liefert die Hauptseite (Frontend) aus."""
    index_file = static_dir / "index.html"
    if not index_file.exists():
        raise HTTPException(
            status_code=404, detail="static/index.html nicht gefunden."
        )
    return FileResponse(str(index_file))


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Nimmt den Prompt vom Frontend entgegen, ruft Gemini auf und gibt die Antwort zurück."""
    prompt = request.prompt.strip()
    if not prompt:
        raise HTTPException(
            status_code=400, detail="Die Frage darf nicht leer sein."
        )

    # API-Key aus Umgebungsvariable lesen
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key or api_key == "DEIN_GEMINI_API_KEY_HIER":
        raise HTTPException(
            status_code=500,
            detail=(
                "Kein gültiger GEMINI_API_KEY gefunden!\n"
                "Bitte trage deinen echten API-Key in die Datei '.env' ein."
            ),
        )

    # Standard-Modell aus Umgebungsvariable oder Default
    model_name = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

    try:
        # Initialisiere den Google GenAI Client
        client = genai.Client(api_key=api_key)

        # Anfrage an Gemini stellen
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
        )

        reply_text = response.text or "Keine Antwort erhalten."
        return ChatResponse(reply=reply_text)

    except APIError as e:
        raise HTTPException(
            status_code=502,
            detail=f"Google Gemini API Fehler: {e.message or str(e)}",
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Interner Server-Fehler bei der Kommunikation mit Gemini: {str(e)}",
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
