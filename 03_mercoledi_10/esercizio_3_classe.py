"""Questa classe dovrebbe avere:

Due attributi di istanza: intestatario e saldo (il saldo iniziale deve essere passato al costruttore, con valore di default 0).

Un metodo deposita che accetti un importo e lo aggiunga al saldo. Se l'importo è negativo o zero, stampa un messaggio di errore senza modificare il saldo.

Un metodo preleva che accetti un importo e lo sottragga dal saldo. Se il saldo non è sufficiente, stampa un messaggio di errore senza modificare il saldo.

Un metodo stampa_saldo che stampi una stringa del tipo "Il saldo di 'intestatario' è: 'saldo' €"."""

import random


class ContoCorrente:
    
    def __init__(self, intestatario):
        self.intestatario = intestatario
        self.saldo = 0
        
    def deposita(self, importo_da_depositare):
        if importo_da_depositare <=0:
             print("Devi inserire un importo valido")
        self.saldo += importo_da_depositare
        return self.saldo
    
    def preleva(self, importo_da_prelevare):
        if importo_da_prelevare <=0 and self.saldo < importo_da_prelevare:
             print("Devi inserire un importo valido oppure saldo insufficiente")
        self.saldo -= importo_da_prelevare
        return self.saldo
    
    def stampa(self):
        print("Il saldo di", self.intestatario, "è:", self.saldo, "€")
        


conti_correnti = []
c1 = ContoCorrente("Massimo Di Luccio")
c2 = ContoCorrente("Giorgia Rossi")
c3 = ContoCorrente("Marco Verdi")
c4 = ContoCorrente("Giuseppe Anastasi")

conti_correnti.append(c1)
conti_correnti.append(c2)
conti_correnti.append(c3)
conti_correnti.append(c4)

#for conto in conti_correnti:
#   print(conto.intestatario)
nr_conto = random.randint(1, len(conti_correnti))
conto = conti_correnti[nr_conto]

controllo = True
while controllo:
    
    print("Benvenuto", conto.intestatario, "nel tuo conto")
    print("1-Preleva, 2-Deposita, 3-stampa saldo, e- Esci")
    scelta = int(input("Scegli: "))
    
    match scelta:
        case 1:
            importo_inserito = int(input("importo: "))
            conto.preleva(importo_inserito)
            conto.stampa()  
        case 2:
            importo_inserito = int(input("importo: "))
            conto.deposita(importo_inserito)
            conto.stampa()  
        case 3:
             conto.stampa()    
        case "e":
            controllo = False
            print("esco..")
        case _:
            pass
        
    
    