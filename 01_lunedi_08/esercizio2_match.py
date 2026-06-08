#chiedo in input a e b
a = int(input("inserisci a"))
b = int(input("inserisci b"))

#quali operazione eseguire
operazione = input("inserisci l'operazione: +, - , *, /")

match operazione:
    case"+": #se ho scelto +
        print(a+b) #sommo a e b
    case  "-": #se ho scelto meno
        print(a-b) #sottraggo
    case  "*": #se ho scelto *
        print(a*b) #moltiplico
    case "/": 
        if b == 0: # se il divisore è 0
            print("Errore: Divisione per zero")
        else: #altrimenti faccio la divisione
            print(a/b)
    case _: # se non è nessuno dei casi sopra
        print("Operazione non valida")
