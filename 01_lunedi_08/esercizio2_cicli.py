"""
    chiedi all'utente di inserire un numero.
    il programma deve controllare se il numero inserito è primo/pari o no.
    Se è primo, lo salva e stampa "Il numero è pari". Altrimenti stampa "Il numero non è primo".
    si ferma il tutto quando ha 5 numeri primi.
"""
#chiedo un numero
controllo= True
while controllo:
    numero = int(input("Inserisci un numero: "))
    numeri = [];
    if numero % 2 == 0:
        print("il numero è pari")
        numeri.append(numero)
    else:
         print("il numero non è pari")
       
    if len(numeri) == 5:
        controllo = False
        print(numeri)

    