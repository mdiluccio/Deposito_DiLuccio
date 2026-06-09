
""" slide 79"""


controllo = True
while controllo:
    numeri = []
    #input
    nr_elementi = int(input("quanti elementi vuoi inserire: "))

    #append nella lista
    inseriti = 0
    while inseriti < nr_elementi: #ciclo fino a quando inseriti non è uguale al numero di elementi che ho deciso di inserire
        numero = int(input("numero: "))
        if numero <= 0: 
            print("hai inserito un numero negativo")
            continue
        #qaundo ho trovato un postivo lo inserisco
        numeri.append(numero)
        inseriti += 1

    print(numeri)
    
    #creo delle liste per ogni casistica
    lista_pari = []
    lista_dispari = []
    lista_primi = []
    
    somma_pari = 0
    for numero in numeri:
        #se il numero è pari
        if numero %2 == 0:
            #salvo nella lista
            lista_pari.append(numero)
            #sommo i numeri
            somma_pari +=numero
        else:
            #salvo nella lista dei dispari
            lista_dispari.append(numero)
    
    #check se i numeri sono primi o meno
    for i in range(2, numero):
        if numero % i == 0:
            print("Il numero non è primo")
        else:
            print("Il numero è primo")
            lista_primi.append(i)
        
    #somma dei numeri pari 
    print("somma pari:", somma_pari)  
     
    print("lista dei dispari:", lista_dispari) 
    print("lista dei primi:", lista_primi) 
    
    

    if inseriti == nr_elementi:
        print("Terminato")
