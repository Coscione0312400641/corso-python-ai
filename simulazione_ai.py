import json
prompt=f"""
Genera la descrizione di questo utente:
Si chiama Anna e ha 22 anni
"""
with open('utenti.json') as f:
    u=json.load(f)
def vincenzo_gpt(prompt,context):
    risposta="Ciao, ecco la tua descrizione: "

    descrizione=f"L'utente si chiama {context['nome']} e ha {context['eta']} anni"
    return risposta+descrizione
print(vincenzo_gpt(prompt,u[1]))