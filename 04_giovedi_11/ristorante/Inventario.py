import Articolo

class Inventario:
    
    def __init__(self):
        self.articoli = []
        
    def stampa_inventario(self):
        for articolo in self.articoli:
              print("Inventario - Articolo", articolo.nome, "Prezzo", articolo.prezzo, "Quantità", articolo.quantita)
              
              
    def aggiungi_articoli(self, articoli):
        for articolo in articoli:
            self.articoli.append(articolo) 
            

