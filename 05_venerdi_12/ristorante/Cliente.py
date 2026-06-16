import Articolo
import pickle 
import os

class Cliente:
    
    utenti_loggati = []
    utenti_registrati = []
    
    FILE_DATI = "utenti.dat"
    
    def __init__(self, nome, username, password):
        self.username = username
        self.password = password
        self.nome = nome
        self.carrello = [] #lista di articoli
        
    @classmethod        
    def login(cls):
        print("\nLOG IN")
        is_logged = False
        while not is_logged:
            username_inserito = input("Inserisci username:")
            password_inserita = input("Inserisci password:")
        
            if username_inserito =="" or password_inserita =="":
                print("Devi inserire username o password corrette")
                continue   
            else:
                for cliente in Cliente.utenti_registrati:
                    if cliente.username == username_inserito :
                        cls.utenti_loggati.append(cliente)
                        
                        print("Log in effettuato con successo!")
                        print("\nCiao,", cliente.nome)
    
                        #is_logged = True
                        return cliente
                    else: 
                        print("username non registrato o incorretto. Registrati")
    
    @classmethod   
    def registrati(cls):
        print("BENVENUTO NELLA TUA AREA DI REGISTRAZIONE")
        nuovo_nome = input("Inserisci il tuo nome:")
        
        is_sign_up = False
        while not is_sign_up:
            nuovo_username = input("Inserisci nuova username:")
            nuova_password = input("Inserisci nuova password:")
        
            if nuovo_username =="" or nuova_password =="":
                print("Devi inserire username o password corrette")
                continue
            else:
                if nuovo_username in cls.utenti_registrati:
                    print("Username già esistente")
                    continue
                else:
                    nuovo_cliente = Cliente(nuovo_nome, nuovo_username, nuova_password)
                    cls.utenti_registrati.append(nuovo_cliente)
                    cls.salva_dati()
                    
                    print("Registrazione completata!")
                    is_sign_up = True
                    return nuovo_cliente
            
                      
    def log_out(self):
        for cliente in Cliente.utenti_loggati:
            Cliente.utenti_loggati.remove(cliente)
    
    
    def check_carrello(func):
        def wrapper(*args, **kwargs):
            cliente = args[0]
            
            print(f"\n--- [MONITORATO] Stato carrello PRIMA di '{func.__name__}' -")
            if not cliente.carrello:
                print("Il carrello è VUOTO.")
            else:
               for articolo in cliente.carrello:
                    print("Articolo:", articolo.nome, "Prezzo:", articolo.prezzo, "Quantità:", articolo.quantita)
                    
            risultato = func(*args, **kwargs)
            
            print(f"--- [MONITORATO] Stato carrello DOPO di '{func.__name__}' ---")
            if not cliente.carrello:
                print("Il carrello è VUOTO.")
            else:
                for art in cliente.carrello:
                    print("Articolo:", articolo.nome, "Prezzo:", articolo.prezzo, "Quantità:", articolo.quantita)
            return risultato
        return wrapper
    
         
    def visualizza_carrello(self):
        print("Sto guardando il mio carrello..")
        self.traccia_acquisti()
    
    def svuota_carrello(self):
        self.carrello = []
        
        
     
    @check_carrello       
    def acquista(self):
        if not self.carrello:
            print("carrello vuoto")
            return
        
        self.traccia_acquisti()
        print("Confermo pagamento per gli acquisti in elenco") 
        self.svuota_carrello() 
        
            
                        
    def aggiungi_al_carrello(self, nuovo_articolo, quantita_richiesta):
        if nuovo_articolo.quantita >= quantita_richiesta:
             
            nuovo_articolo_acquisto = Articolo.Articolo(nuovo_articolo.nome, nuovo_articolo.prezzo, quantita_richiesta)
            self.carrello.append(nuovo_articolo_acquisto)
            
            #decremento la quantita dell'invnetario
            nuovo_articolo.quantita -= quantita_richiesta 
            
            print("HO AGGIUNTO AL CARRRELLO", quantita_richiesta, nuovo_articolo_acquisto.nome)
            
        else:
            print("Quantità insufficiente in magazzino")
    
      
    def traccia_acquisti(self):
        print("----------------ARTICOLI NEL CARRELLO---------------")
        if not self.carrello:
            print("VUOTO")
            
        for articolo_in_carrello in self.carrello: 
            print("Articolo:", articolo_in_carrello.nome, "Quantità", articolo_in_carrello.quantita, "articolo/i",
                  "Totale:", articolo_in_carrello.prezzo*articolo_in_carrello.quantita, "$")  
            
            
            
   
            
    @classmethod
    def salva_dati(cls):
        """Prende la lista utenti_registrati e la salva sul disco fisso."""
        with open(cls.FILE_DATI, "wb") as file:  # "wb" significa Scrittura Binaria
            pickle.dump(cls.utenti_registrati, file)
        print("[Sistema] Dati salvati con successo sul disco!")

    @classmethod
    def carica_dati(cls):
        """Cerca il file sul disco. Se esiste, ripopola la lista utenti_registrati."""
        if os.path.exists(cls.FILE_DATI):
            with open(cls.FILE_DATI, "rb") as file:  # "rb" significa Lettura Binaria
                cls.utenti_registrati = pickle.load(file)
            print(f"[Sistema] Dati caricati! Ci sono {len(cls.utenti_registrati)} utenti registrati.")
        else:
            print("[Sistema] Nessun file di salvataggio trovato. Parto da zero.")
    
            
           
