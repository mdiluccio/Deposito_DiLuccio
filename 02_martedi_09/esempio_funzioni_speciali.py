""" generatori

"""
import time


def fibonacci(n):
    a =0
    b=1
    while a < n:
        yield a
        a = b 
        b = a+b
        

for numero in fibonacci(10):
    print(numero)


"""decoratori

modifica il comportamento di un'altra funzione
Prende un intera altra funzione e la passa come parametro

"""

def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione")
        funzione()
        print("Dopo l'esecuzione del funzione")
    return wrapper

@decoratore
def saluta():
    print("Ciao!")
saluta()



def calcola_tempo(funzione):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        risultato = funzione(*args, **kwargs)
        end_time = time.time()
        print(f"Tempo di esecuzione: {end_time - start_time} secondi")
        return risultato
    return wrapper

@calcola_tempo
def calcolo_lento():
    time.sleep(2)
    print("calcolo completato")
    
    
calcolo_lento()