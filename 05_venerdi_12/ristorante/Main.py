import Articolo
import Inventario
import Cliente
import Amministrazione

class Main:
    
    clienti =[]
    clienti1 = Cliente.Cliente("Mario Rossi", "ciccio988", "miapass34")
    ##clienti2 = Cliente.Cliente("Giuseppe verdi", "bbb", "miapass35" ) non funziona il login con questo
    clienti.append(clienti1)
    clienti.append(clienti1)
    
    
    articolo1 = Articolo.Articolo("Maglietta Nike", 29.99, 10)
    articolo2 = Articolo.Articolo("Jeans Levi's", 79.90, 5)
    articolo3 = Articolo.Articolo( "Scarpe Adidas", 120.00, 3)

    inventario = Inventario.Inventario()
    amministrazione = Amministrazione.Amministrazione(inventario)
    
    inventario.aggiungi_articoli([articolo1,articolo2, articolo3])
    print("\n")
    
    inventario.stampa_inventario()
    
    print("\n")
    print("BENVENUTO NELLA TUA AREA DI LOGIN")
    
    username = input("Inserisci username:")
    password = input("Inserisci password:")
    
    
    for cliente in clienti:
        if(cliente.is_logged(username, password)):
            cliente.acquista(articolo1, 5)

            print("\n")
            cliente.visualizza_articoli()
            print("\n---TRACCIAMENTO ACQUISTI-----")
            cliente.traccia_acquisti()
            
            print("\n---INVENTARIO DOPO ACQUISTI-----")
            inventario.stampa_inventario()
            break
        
            
    print("\n")
    amministrazione.rapporto_vendite([clienti1])
    
    
    