import Articolo

class Cliente:
    
    def __init__(self, nome):
        self.nome = nome
        self.carrello = [] #lista di articoli
        
    def visualizza_articoli(self):
        for articolo in self.carrello:
            print("Cilente", self.nome, "- Articolo", articolo.nome, "Prezzo", articolo.prezzo, "Quantità", articolo.quantita)
            
          
    def acquista(self, articolo, quantita_richiesta):
        if articolo.quantita >= quantita_richiesta:
             
            articolo_da_comprare = Articolo.Articolo(articolo.nome, articolo.prezzo, quantita_richiesta)
            self.carrello.append(articolo_da_comprare)
            
            #decremento la quantita
            articolo.quantita -= quantita_richiesta 
            
            
    def traccia_acquisti(self):
        for articolo_in_carrello in self.carrello: 
            print("Il cliente", self.nome, "ha acquistato", articolo_in_carrello.quantita)  
        
        if self.carrello == []:
            print("Il cliente", self.nome, "non ha effettuato nessun acquisto")
    
            
            
