import Inventario

class Amministrazione:
    
    def __init__(self, inventario):
        self.inventario = inventario
        
        
    def rapporto_vendite(self, clienti):
        pass
        #calcolare il totale venduto (prezzo * quantita)
        totale_venduto = 0
        n_articoli_venduti =0
        vendite = {} # nome: totale_venduto
        for cliente in clienti:
            for articolo in cliente.carrello:
                nome = articolo.nome
                prezzo = articolo.prezzo
                quantita = articolo.quantita
            
                totale_venduto += (prezzo * quantita)
                n_articoli_venduti +=quantita
            
                #inserisco i valori nella mio dizionario vendite
                if nome in vendite:
                    #aggiorno la quantita
                    vendite[nome] += quantita #accedo alla chiave nome
                else:
                    vendite[nome] = quantita
                    
        print("REPORT VENDITE GLOBALE")        
        print("Totale vendite", totale_venduto,"$")
        print("Totale articoli venduti", n_articoli_venduti)
        print("Totale dei clienti che hanno acquistato dal negozio", len(clienti))
        
        for nome,quantita in vendite.items():
            print("Articolo -", nome, "- Quantita", quantita)