import Articolo

class Inventario:
    
    def __init__(self):
        self.articoli = []
        
    def stampa_inventario(self):
        for articolo in self.articoli:
              print("Inventario - Articolo", articolo.nome, "Prezzo", articolo.prezzo, "Quantità", articolo.quantita)
              
    def rimuovi_articoli(self, articoli_selezionati):
        for articolo_selezionato in articoli_selezionati:
            self.articoli.remove(articolo_selezionato)
            print("Articolo", articolo_selezionato.nome, "rimosso")
            
            
            
    def aggiorna_articolo(self, articolo_modificato):
        for articolo_selezionato in self.inventario:
            if articolo_selezionato.nome == articolo_modificato.nome:
                articolo_selezionato.nome = articolo_modificato.nome
            if articolo_selezionato.prezzo == articolo_modificato.prezzo:
                articolo_selezionato.prezzo = articolo_modificato.prezzo
                
            self.aricoli.replace(articolo_selezionato)
            print("Articolo", articolo_selezionato.nome, "modificato")
            
            
    def aggiungi_articoli(self, articoli):
        for articolo in articoli:
            self.articoli.append(articolo)           
    
            

