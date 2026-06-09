""" utilizzo while e range
un sistema che prende in input un numero intero positvo n e stampa tutti i numeri da n a 0 (compreso), decrementando di 1. Deve ripetersi all'infinito

"""

#while
controllo = True
while controllo:
    #input
    #inserisco n che sarà quante volte dovrò ciclare
    n = int(input("inserisci n da decrementare a 0: "))
    #controllo che sia > 0 altrimenti richiedo il numero
    while n < 0:
        n = int(input("inserisci n positivo: "))  
   
    #range
    for i in range(n, -1, -1): #decremento partendo da n, comprendo lo zero (-1 escluso) e decremento (-1)
        print(i)
      
    #condizione di uscita dal while
    """if(i==0):
        n = int(input("inserisci il nuovo valore n da decrementare a 0: "))"""