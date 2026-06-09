""" slide 102"""
 ##################### punto 1



"""def genera_positivo(nunero):
    while numero <= 0: 
        print("numero negativo")
        continue
    #qaundo ho trovato un postivo lo ritorno
    return numero


controllo = True
while controllo:
    numeri = []
    #input
    nr_elementi = int(input("quanti elementi vuoi inserire: "))

    #append nella lista
    inseriti = 0
    while inseriti < nr_elementi: #ciclo fino a quando inseriti non è uguale al numero di elementi che ho deciso di inserire
        numero = int(input("numero: "))
        numero_trovato = genera_positivo(numero)
        inseriti += 1
        numeri.append(numero_trovato)
    print(numeri)"""
    
    
 ##################### punto 2   
import random
def interi_casuali(n):
    lista =[]
    for i in range(n):
        numero_generato = random.randint(1, n)
        lista.append(numero_generato)
    return lista

def num_pari(numeri):
    lista_pari=[]
    for numero in numeri:
        if numero %2==0:
            lista_pari.append(numero)
    return lista_pari

def somma_valori(numeri):
    somma = 0
    for numero in numeri:
        somma += numero
    return somma
    

controllo = True
while controllo:
    scelta = input("Cosa vuoi fare? genera (g) o esci (e): ")
    
    if scelta == "e":
        controllo = False
        print("esco")
        continue # salto tutto il resto del codice e chiudo il ciclo
    
    nr_elementi = int(input("quanti elementi vuoi inserire: "))

    #punto 2   
    lista_generata = interi_casuali(nr_elementi)
    print("lista di interi", lista_generata)
    #punto 3
    lista_pari = num_pari(lista_generata)
    somma_pari = somma_valori(lista_pari)
    print("lista dei pari", lista_pari)
    print("somma dei pari:", somma_pari)
    
    
    


    
    