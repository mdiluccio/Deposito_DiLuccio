""" un modulo è un file che contiene variabili, funzioni e classi
I moduli permettono di organizzare in unità logiche e riutilizzabili

"""

def saluta(nome):
    print("Ciao,", nome)

PI = 3.14159


class Cerchio:
    def __init__(self, raggio):
        self.raggio = raggio


    def area(self):
        return PI * self.raggio**2