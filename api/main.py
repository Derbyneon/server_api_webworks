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

@app.get("/")
async def root():
    return {
        "message": "Bienvenue sur l'API d'inscription par email!",
        "description": "Cette API permet d'enregistrer des adresses email pour la souscription à des newsletters ou notifications.",
        "endpoints": {
            "/subscribe": "POST - Enregistrer une adresse email",
        },
        "note": "Pour enregistrer une adresse email, envoyez une requête POST au point de terminaison /subscribe avec le champ 'email' dans le corps de la requête."
    }