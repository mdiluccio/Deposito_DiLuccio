"""chiamata Convertitore. Questa classe dovrebbe avere:

Un metodo statico euro_in_dollari che accetti un importo in euro e restituisca il valore convertito in dollari, usando un tasso fisso di 1.08.

Un metodo statico km_in_miglia che accetti una distanza in chilometri e restituisca il valore convertito in miglia, usando un fattore fisso di 0.621371."""

class Convertitore:
    
    @staticmethod
    def euro_in_dollari(importo):
        return importo * 1.08
    
    @staticmethod
    def km_in_miglia(distanza):
        return distanza * 0.621371
    
    def __call__(self,valore):
        pass
    
    
dollari = Convertitore.euro_in_dollari(20.78)
print(f"20.78 Euro corrispondono a: {dollari:.2f} Dollari")
miglia = Convertitore.km_in_miglia(100)
print(f"100 Km corrispondono a: {miglia:.2f} Miglia")



        