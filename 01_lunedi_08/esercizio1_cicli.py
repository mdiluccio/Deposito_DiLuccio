"""
range()
Chiedi all'utente di inserire un numero. Il programma deve fare un conto alla rovescia 
a partire da quel numero fino a 0, stampando ogni numero e chiderti se vuoi riptere o no.

"""
controllo = True
while controllo:
    numero = int(input("Inserisci un numero: "))
    for i in range(numero, -1, -1): # parto dal mio numero fino a 0 (escludo il -1) e decremento
        print(i)
    
    scelta = input("vuoi ripetere?") #quando scelgo no
    if scelta == "no":
        controllo = False #imposto controllore a false, quindi quando ritorna al while controlle = False ed esce dal ciclo
    