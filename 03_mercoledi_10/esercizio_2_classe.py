"""Crea una classe chiamata Libro. 

Questa classe dovrebbe avere:

Tre attributi: titolo, autore e pagine.

Un metodo descrizione che restituisca una stringa del tipo "Il
libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine.".

Extra: permetti di creare quanti libri vuole l’utente"""

class Libro:
    
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
        
    def descrizione(self): # metodo di istanza
        print("il libro", self.titolo, "è stato scritto da", self.autore, "e ha", self.pagine, "pagine")
    
    def stampa(self): #metodo di istanza
        print("Libro:", self.titolo, "- Autore:", self.autore, "- Pagine:", self.pagine, "pagine")
        
    
        
libro1 = Libro("Impara a cucinare", "Antonino Cannavaciuolo", "125")
libro1.descrizione()

libri = []
nr_libri = int(input("Quanti libri vuoi creare?: "))

for i in range(nr_libri):
    print("Libro", i+1) 
    titolo = input("Titolo: ")
    autore = input("Autore: ")
    pagine = int(input("Pagine: "))
    
    libro = Libro(titolo, autore, pagine)
    libri.append(libro)
    
    
for libro in libri:
    libro.stampa()
        