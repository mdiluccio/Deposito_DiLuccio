""" Gestione di una lista dinamica in cui l'utente può:
- visualizzare i suoi impegni
- aggiungerli
- rimuoverli

"""

my_todo_list = ["Studiare le funzioni in Python", "Fare la spesa", "Andare ad allenamento", "Chiamare il dottore", "Preparare La cena"]


def visualizza_impegni(lista):
    for id, impegno in enumerate(lista):   # ho usato enumerate per associare un indice ad ogni elemento
        print(id+1, impegno)  
    return lista

def aggiungi_impegno(lista, elemento_da_aggiungere):
    lista.append(elemento_da_aggiungere)
    print("impegno aggiunto:", elemento_da_aggiungere)     
    return lista


def  elimina_impegno(lista, elemento_da_rimuovere):
    indice = elemento_da_rimuovere - 1 # perchè l'indice parte da 0
    
    if indice >=0 and  indice < len(lista): # controllo che l'indice non sia < 0 e che l'indice dell'elemento è incluso nella lista
        elemento = lista.pop(indice)
        print("Hai eliminato l'impegno:", elemento)
    else:
        print("L'impegno non esiste")
    return lista

   

controllo = True
while controllo:
    print("\n")
    
    print("1. Visualizza la lista degli impegni")
    print("2. Aggiungi un impegno")
    print("3. Elimina un impegno completato")
    print("e. Esci dal programma")
    scelta = input("Scegli cosa vuoi fare: ") 
      

    match scelta:
        case "1":
            print("\nMY TO-DO LIST")
            visualizza_impegni(my_todo_list)
        case "2":
            impegno_da_aggiungere = input("Inserisci il nuovo impegno: ")
            aggiungi_impegno(my_todo_list, impegno_da_aggiungere)  
        case "3":
            impegno_da_rimuovere = int(input("Inserisci il numero dell'impegno da eliminare: "))
            elimina_impegno(my_todo_list, impegno_da_rimuovere)
        case "e":
             controllo = False
             print("Esco...") 
        case _:
            print("hai scelto un comando errato. Riprova")
            
            
             
     