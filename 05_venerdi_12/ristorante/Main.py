import Articolo
import Inventario
import Cliente
import Amministrazione

class Main:
    articolo1 = Articolo.Articolo("Maglietta Nike", 29.99, 10)
    articolo2 = Articolo.Articolo("Jeans Levi's", 79.90, 5)
    articolo3 = Articolo.Articolo( "Scarpe Adidas", 120.00, 3)

    
   
    inventario = Inventario.Inventario()
    inventario.aggiungi_articoli([articolo1,articolo2, articolo3])
    print("\n")
    
    
     
    print("\n")
    print("1- Log-In  2- Registrati")
    
    is_operazione_corretta = False
    while not is_operazione_corretta:
        operazione = int(input("Scegli il numero di operazione: "))
        cliente_loggato = None
        match operazione:
            case 1:
                cliente_loggato = Cliente.Cliente.login()
                break
            case 2: 
                cliente_registrato = Cliente.Cliente.registrati()
                cliente_loggato = Cliente.Cliente.login()
                break #salto le righe sotto, esco dal ciclo e vado alla riga 48
            case _:
                print("Hai inserito un'operazione che non esiste. Inserire 1 o 2") 
                continue #salto le righe sotto e richiedo l'operazione corretta alla riga 34
    
    # se sono nei casi 1/2       
    if cliente_loggato:       
        inventario.stampa_inventario()
        print("1- Acquista  2- visualizza il tuo carrello   3- visualizza il tuo storico ordini  4-Log Out")
        
        is_operazione_corretta = False
        while not is_operazione_corretta:
            operazione = int(input("Scegli il numero di operazione: "))
            match operazione:
                case 1:
                    cliente_loggato.aggiungi_al_carrello(articolo1, 5)
                    cliente_loggato.acquista()
                case 2:     
                    cliente_loggato.visualizza_carrello()
                case 3:
                    cliente_loggato.traccia_acquisti()
                case 4:
                    cliente_loggato.log_out()
            
    print("\n---INVENTARIO DOPO ACQUISTI-----")
    inventario.stampa_inventario()
        
            
    print("\n")
    amministrazione = Amministrazione.Amministrazione(inventario)
    amministrazione.rapporto_vendite([cliente_registrato])
    
    
    