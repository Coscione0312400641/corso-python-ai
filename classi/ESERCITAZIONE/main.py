from classi.ESERCITAZIONE.Pipeline import Pipeline

pipeline = Pipeline("requests.csv")
pipeline.esegui()
pipeline.salva_json("output.json")

print("Richieste valide:", len(pipeline._richieste_valide))
print("Servizi unici:", pipeline._servizi_unici)
print("Conteggio servizi:", pipeline._conteggio_servizi)