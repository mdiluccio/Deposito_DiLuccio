import Articolo
import Inventario
import Cliente

class Main:
    
    articolo1 = Articolo.Articolo("Maglietta Nike", 29.99, 10)
    articolo2 = Articolo.Articolo("Jeans Levi's", 79.90, 5)
    articolo3 = Articolo.Articolo("Scarpe Adidas", 120.00, 3)

    inventario = Inventario.Inventario()
    inventario.aggiungi_articoli([articolo1,articolo2, articolo3])
    
    inventario.stampa_inventario()

    clienti1 = Cliente.Cliente("Mario Rossi")
    clienti2 = Cliente.Cliente("Giuseppe verdi")

    clienti1.acquista(articolo1, 5)
    clienti1.visualizza_articoli()
    clienti1.traccia_acquisti()
    clienti2.traccia_acquisti()
    
    