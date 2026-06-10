"""
classe chiamata Garage. Questa classe dovrebbe avere:

Un attributo di istanza capienza (numero massimo di auto) passato al costruttore.

Un attributo di istanza auto_presenti (lista di stringhe con le targhe), inizialmente vuota.

Un metodo parcheggia che accetti una targa e aggiunga l'auto alla lista. Se il garage è pieno, stampa un messaggio di errore. Se la targa è già presente,
avvisa che l'auto è già in garage.

Un metodo rimuovi che accetti una targa e rimuova l'auto corrispondente. Se la targa non è presente, stampa un messaggio di errore.

Un metodo posti_liberi che restituisca il numero di posti ancora disponibili.

DA FARE Un metodo statico formato_targa_valido che accetti una stringa e restituisca True se la targa rispetta il formato italiano (2 lettere, 3 numeri, 2 lettere — es. "AB123CD"), False altrimenti. Suggerimento: si può usare il metodo .isalpha() e .isdigit() sulle sottostringhe.

DA FARE Il metodo parcheggia deve usare formato_targa_valido per rifiutare targhe non valide prima di aggiungerle.

"""

class Garage:
    
    def __init__(self, capienza):
        self.capienza = capienza
        self.auto_presenti = []
        
    def __len__(self):
        return len(self.auto_presenti) 
    
    def __eq__(self, altro):
        return self.targa == altro.targa
    
    """def __str__(self):
        return "Auto presenti nel garage ", """
        
    def parcheggia(self, targa):
        if len(self.auto_presenti) >= self.capienza: #da rivedere, non ho capito la differenza con __len__
            print("Hai raggiunto la capienza massima")
            return False
        if targa in self.auto_presenti: # in è il contains 
            print("Auto già in garage")
            return False
                
        self.auto_presenti.append(targa)  # non fa append, da verificare  
        return True
    
    def rimuovi(self, targa):
        if targa in self.auto_presenti: # in controlla in automatico la targa in una lista quindi non uso for ma if
            #indice = self.auto_presenti.index(auto) # prendo l'indice dell'auto
            self.auto_presenti.remove(targa) 
            return True
        else:
            print("L'auto non è presente")
            return False
    
    def posti_liberi(self):
        return print("Posti disponibili", self.capienza - len(self.auto_presenti))
    
garage = []   
 
garage1 = Garage(4)
garage1.parcheggia("CV223FJ")

garage2 = Garage(6)

garage.append(garage1)
garage.append(garage2)
    
print("auto presenti nel garage 1", garage1.auto_presenti)
print("auto presenti nel garage 2", garage2.auto_presenti)

"""for g in garage:
    for targa in g.auto_presenti:
        print(targa)"""
        
garage1.posti_liberi();
garage2.posti_liberi();