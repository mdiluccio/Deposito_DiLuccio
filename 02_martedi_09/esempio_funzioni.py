""" Le funzioni sono la rappresentazione dell'astrazione. La capcita di scrivere elementi in un punto A e usarle in un punto B
organizzano il codice in unità modulari

Tipo di parametri:
 - posizionali: devono essere passati nell'ordine esatto
 - keyword: possono essere passati in qualsiasi ordine specificando il nome
 - default: specificano un valore predefinito che la funzione utlizzera se non viene fornito un argomento
 
 return di defult è nullo se non specificato
"""

def saluta(nome):
    print("Ciao", nome)
    
def somma(a,b):
    res = a+b
    print("La somma è:", res)
    
saluta("Massimo")
somma(5,2)

def saluta(nome:str, messaggio="Ciao"):
    print(messaggio, nome)
    
saluta("Mario")
saluta("Luigi", messaggio="Buongiorno")


def quadrato(numero):
    return numero*numero #valore di ritorno

risultato = quadrato(4)
print(risultato)