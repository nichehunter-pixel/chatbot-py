import requests
import json
api_key = "VOTRE-CLE-API-ICI"


supported_models = [
    "gpt-4o-mini",
    "gpt-4o-mini-search-preview",
    "gpt-4o",
    "gpt-4o-search-preview",
    "gpt-4.1-nano",
    "gpt-4.1-mini",
    "o3",
    "o3-mini",
    "o4-mini",
    "gpt-5.4",
    "gpt-5.3",
    "gpt-5.2"
]


model = input(f"Veuillez entrer le modèle que vous voulez utiliser\nModèles supportés: {" ".join(supported_models)}\nVotre choix: ")
print()

while model not in supported_models:
    model = input(f"Modèle choisi invalide, modèles valides: ({", ".join(supported_models)})\n\nVotre choix: ")


system_prompt = input("Veuillez entrer le prompt système que vous voulez donner au modèle, laissez le vide pour ne donner aucun: ")


if len(system_prompt) <= 3 and len(system_prompt) != 0:
    print("Prompt système invalide.")
    exit()
    

historique = []

if len(system_prompt) != 0:
    historique.append({
        "role": "system",
        "content": system_prompt
    })


while True:

    print()
    question = str(input("Vous: "))
    historique.append({"role": "user", "content": question})
    response = requests.post(
        "https://api.voidai.app/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        data=json.dumps({
            "model": model,
            "messages": historique
        })
    )
    data = response.json()
    reponse = data["choices"][0]["message"]["content"]
    historique.append({"role": "assistant", "content": reponse})


    print("AI: " + reponse)
﻿

 
 
 
