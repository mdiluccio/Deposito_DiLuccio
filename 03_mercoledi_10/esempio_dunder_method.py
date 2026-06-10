"""
trattini bassi prima e dopo il nome,
come __init__, __str__, __len__,
vengono chiamati metodi speciali o
anche dunder methods, da “double
underscore”.

__str__ è il toString
__len__ restituscie la lunghezza di una lista


Sono metodi che non vengono usati
quasi mai chiamandoli direttamente,
ma vengono richiamati
automaticamente da Python in
situazioni specifiche. """

class Esempio:

    def __init__(self, nome, eta, studenti):
        self.nome = nome
        self.eta = eta
        self.studenti = studenti
   
    def __len__(self):
        return len(self.studenti) 

    def __str__(self):
        return "Studente: " + self.nome + ", età: " + str(self.eta)


esempio = Esempio("1", 20, ["bbb"])
print(esempio)


class Moltiplicatore:

 def __init__(self, numero):
    self.numero = numero


 def __call__(self, valore): #permette di chiamare un'istanza di una classe esattamente come fosse una funzione
    return valore * self.numero

doppio = Moltiplicatore(2)
print(doppio(10))


class Prodotto:


 def __init__(self, nome, prezzo):

   self.nome = nome

   self.prezzo = prezzo


 def __eq__(self, altro): # definisce il comportamento di ==
   return self.nome == altro.nome and self.prezzo == altro.prezzo



prodotto1 = Prodotto("Mouse", 20)
prodotto2 = Prodotto("Mouse", 20)
prodotto3 = Prodotto("Tastiera", 35)

print(prodotto1 == prodotto2) #py confronta la loro identità in memoria ma con __eq__ decidiamo noi quando due oggetti sono uguali
print(prodotto1 == prodotto3)

class Squadra:


    def __init__(self, nome, giocatori):

        self.nome = nome
        self.giocatori = giocatori


    def __len__(self):
        return len(self.giocatori)



squadra1 = Squadra("Tigri", ["Luca", "Marco", "Anna"])
print(len(squadra1))