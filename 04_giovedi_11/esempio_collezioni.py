"""
le tuple sono rappresentate dal tipo di dato tuple e racchiuse da ()
è eterogenea
non modificabile
ordinato
"""

punto = (3,4)
colore = (255,128,0)

#a differenza delle liste una volta creata la tupla non può essere modificata, SONO COSTANTI
punto = (3,4)
#punto[0] = 5 #errore

""" insiemi
sets: 
- tipo di dato set
- {}
- non è ordinato
- modifcabile
-eterogeneo di base ma omogeneo perchè deve fare die confornti
"""

set1 = set([1,2,3,4,5])
set2 = {2,3,4,5}
print(set1)
print(set2)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print("\n")
print(set1.union(set2)) #tutti
print(set1.intersection(set2)) #solo quelli in comune
print(set1.difference(set2)) # quelli non in comune
print(set1.symmetric_difference(set2)) # unione dei non in comune

"""dizionari sono strutture chiave: valore
tipo dict
"""
studente = {
    "nome": "Alice",
    "eta": 20,
    "sesso": "Femmina"
}

print(studente["nome"]) # ricerca per chiave per valorizzare gli elementi
studente["eta"] = 21 # assegnare un nuovo valore
print(studente["eta"])
studente["citta"] = "Roma" #aggiungo un nuovo elemento
print(studente) 

print(studente.keys())
print(studente.values())

for x,y in studente.items(): #ciclare un dizionario con items()
    print(x,y)