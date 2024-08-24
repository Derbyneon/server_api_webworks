from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os

app = FastAPI()

# Configurer les règles CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autoriser toutes les origines (peut être restreint à une URL spécifique)
    allow_credentials=True,
    allow_methods=["*"],  # Autoriser toutes les méthodes HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Autoriser tous les headers
)

# Modèle de données pour l'email
class Email(BaseModel):
    email: str

@app.post("/subscribe")
async def subscribe(email: Email):
    # Lire les emails existants dans le fichier JSON
    if os.path.exists('emails.json'):
        with open('emails.json', 'r') as file:
            emails = json.load(file)
    else:
        emails = []

    # Ajouter le nouvel email
    emails.append(email.dict())

    # Sauvegarder les emails dans le fichier JSON
    with open('emails.json', 'w') as file:
        json.dump(emails, file, indent=2)

    return {"message": "Email enregistré avec succès!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)