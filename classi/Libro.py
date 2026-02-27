class Libro:
    def __init__(self,titolo,genere,autore,prezzo,trama):
        self.titolo=titolo
        self.genere=genere
        self.autore=autore
        self.prezzo=prezzo
        self.trama=trama
    def descrizione(self):
        print(f"Il libro {self.titolo} di {self.genere} scritto da {self.autore} costa {self.prezzo} e parla di {self.trama}")
l1=Libro("Ventimila leghe sotto i mari","Avventura","Verne",19.29,"Una spedizione a bordo di un sottomarino con il capitano Nemo")
l1.descrizione()