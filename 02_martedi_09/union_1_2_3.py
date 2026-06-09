controllo = True
while controllo:
    
    print("benvenuto: scegli tra 1, 2 e 3. 0 per uscire")
    risposta = int(input("Scegli: "))
    numeri = []
    #input
    nr_elementi = int(input("quanti elementi vuoi inserire: "))
    #append nella lista
    inseriti = 0
    
    while inseriti < nr_elementi:
        numero = int(input("numero: "))
        numeri.append(numero)
        inseriti += 1

    print(numeri)

    
    match risposta:
        case 1:
            n = int(input("numero: "))
            if n%2 == 0:
                print("numero pari")
            else:
                print("numero dispari")
            break
        case 2:
            while n < 0:
                n = int(input("inserisci n positivo: "))  
            #range
            for i in range(n, -1, -1): #decremento partendo da n, comprendo lo zero (-1 escluso) e decremento (-1)
                print(i)
            break
        case 3:
            for i in range(nr_elementi):
                n = int(input("inserisci n positivo: "))  
                quadrato = n**n
                numeri.append(quadrato)
            print(numeri)
            break
        case 0:   
            print("esco dal sistema")
            break
            
    if(risposta==0):
        controllo=False