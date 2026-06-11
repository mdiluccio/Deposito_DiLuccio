import Libro

class Libreria:
    def __init__(self):
        self.catalogo = []
        
    def aggiungi_libro(self, libro):
        if libro not in self.catalogo:
            self.catalogo.append(libro)
        else:
            print("Libro gia presente")
        
    def rimuovi_libro(self, isbn):
        for libro in self.catalogo:
            if libro.isbn == isbn:
                self.catalogo.remove(isbn)
            else:
                print("libro non presente")
            
    def cerca_per_titolo(self, titolo):
        for libro in self.catalogo:
            if libro.titolo.lower() == titolo.lower():
                return libro
            
            
    def mostra_catalogo(self):
        for libro in self.catalogo:
            print("Catalogo dei libri", libro)   
        
        
        
libro1 = Libro.Libro("test", "test autore", "gdhhb213")
libro2 = Libro.Libro("test2", "test autore 2", "gddhb273")

libreria1 = Libreria()
libreria1.aggiungi_libro(libro1)
libreria1.aggiungi_libro(libro2)

libreria1.mostra_catalogo()
   
        
        