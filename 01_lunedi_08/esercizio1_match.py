
eta = int(input("inserisci la tua età"))

match eta:
    case _ if eta <18:
            print("Mi dispiace, non puoi vedere questo film.")
    case _:
        print("Puoi vedere questo film")
        
