import Articolo

class Cliente:
    
    def __init__(self, nome, username, password):
        self.username = username
        self.password = password
        self.nome = nome
        self.carrello = [] #lista di articoli
        
        
    def is_logged(self, username, password):
        if self.username == username and self.password == password:
            print("Benvenuto", self.nome)
            
            return True
        else:
            print("Username o password errati")
            return False
        
    #def registrati(self, cliente):
     #   cliente = Cliente()
        
        
    def visualizza_articoli(self):
        for articolo in self.carrello:
            print(self.nome, ":\n- Articolo:", articolo.nome, "Prezzo:", articolo.prezzo, "Quantità:", articolo.quantita)
            
        if self.carrello == []:
            print(self.nome, ":\n nessun articolo")    
          
    def acquista(self, nuovo_articolo, quantita_richiesta):
        if nuovo_articolo.quantita >= quantita_richiesta:
             
            nuovo_articolo_acquisto = Articolo.Articolo(nuovo_articolo.nome, nuovo_articolo.prezzo, quantita_richiesta)
            self.carrello.append(nuovo_articolo_acquisto)
            
            #decremento la quantita dell'invnetario
            nuovo_articolo.quantita -= quantita_richiesta 
    
    
    def tracking(func):
        def wrapper(*args, **kwargs):
            print("Sto tenendo traccia degli acquisti")
            risultato = func(*args, **kwargs)
            return risultato
        return wrapper 
    
                
    @tracking        
    def traccia_acquisti(self):
        for articolo_in_carrello in self.carrello: 
            print("Il cliente", self.nome, "ha acquistato", articolo_in_carrello.quantita, "articolo/i")  
        
        if self.carrello == []:
            print("Il cliente", self.nome, "non ha effettuato nessun acquisto")
    
            
           
