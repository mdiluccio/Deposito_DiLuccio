class Libro:
    
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
        
        
    def __str__(self):
         return f"{self.titolo} - Autore: {self.autore} - Isbn: {self.isbn})"
     
    def __eq__(self, value):
        pass
        
    
    