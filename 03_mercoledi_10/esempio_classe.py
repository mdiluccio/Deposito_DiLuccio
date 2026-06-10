"""  La classe è un modello logico per definire un tipo non basilare. UNA SOLA CLASSE
Gli oggetti sono l’istanza reale della classe  INFINITI OGGETTI

Una classe definisce:
- tipo,
-  metodi speciali e non: sono le funzioni associate e descrivono il comportamento
-  attributi
Ogni oggetto avrà tutte queste cose
NON avranno in comune il nome, il valore degli attributi

self è il nome dell'oggetto
__init__ costruttore predefinito implicito, posso non esplicitarlo
"""

class Automobile:
    numero_di_ruote = 4
    
    def __init__(self, marca, modello):  # costruttore __nome__ vuol dire che esiste è può essere anche vuoto
        self.marca = marca #self dichiara quale oggetto è
        self.modello = modello

    def stampa_info(self):
        print("L'automobile è una", self.marca, self.modello)
        
        
auto1 = Automobile("Fiat", "500")
auto2 = Automobile("BMW", "X3")

auto1.stampa_info()
auto2.stampa_info()


#################àà classe 2
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome 
        self.eta = eta
        
p = Persona("Pippo", 30)
print(p.nome, p.eta)


###################################### metodo saluta di istanza
class Persona:
    def __init__(self, nome):
        self.nome = nome

        
    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome}")


# Creazione di un oggetto Persona
p = Persona("Luca")
p.saluta()  
# Output: Ciao, mi chiamo Luca 

class Calcolatrice:

    @staticmethod
    def somma(a, b):
        return a + b

#################à Uso del metodo statico senza creare un'istanza

risultato = Calcolatrice.somma(5, 3)
print(risultato)  
# Output: 8

class Contatore:
    numero_istanze = 0  # Attributo di classe

    def __init__(self):
        Contatore.numero_istanze += 1


    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")


c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze()  # Output: Sono state create 2 istanze.