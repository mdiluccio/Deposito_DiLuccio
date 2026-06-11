"""
Ristorante
"""

class Piatto:
    
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo
        
    def __str__(self):
        return f"{self.nome} (Prezzo: {self.prezzo}€)"
    ##("Piatto",self.nome,"prezzo", self.prezzo) #  restituisce una tupla  TypeError: __str__ returned non-string (type tuple)
    
    
    
class Ristorante:
    
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = [] # voglio dire che devo avere una lista di piatti
        
    def descrivi_ristorante(self):
        print("Ristorante",self.nome,"Cucina", self.tipo_cucina)
        
    def stato_apertura(self):
        if self.aperto:
            print("Ristorante Aperto")
        else:
            print("Ristorante chiuso")
            
    def apri_ristorante(self):
        if not self.aperto:
            self.aperto = True
            print("Ristorante", self.nome ,"aperto")
        return self.aperto
    
    def chiudi_ristorante(self):
        if self.aperto:
            self.aperto = False
            print("Ristorante", self.nome ,"chiuso")
        return self.aperto
    
    def aggiugi_al_menu(self, piatti):
        for piatto in piatti:
            if piatto not in self.menu: # controllo che il piatto non sia già presente nel menu
                self.menu.append(piatto)
                print("Aggiunto piatto:", piatto, "al menù")
            else:
               print("Piatto già presente nel menù") 
        return piatti   
    
    def togli_dal_menu(self,piatti):
        for piatto in piatti:
            if piatto in self.menu: # controllo che il piatto sia nel menu
                self.menu.remove(piatto)
                print("Rimosso piatto:", piatto, "al menù")
            else:
                print("Piatto non presente nel menù")
    
    
    def stampa_menu(self):
        for piatto in self.menu:
            print("Piatti presenti nel menù:", piatto)
        
"""libri = []
nr_libri = int(input("Quanti libri vuoi creare?: "))

for i in range(nr_libri):
    print("Libro", i+1) 
    titolo = input("Titolo: ")
    autore = input("Autore: ")
    pagine = int(input("Pagine: "))
    
    libro = Libro(titolo, autore, pagine)
    libri.append(libro)   """
    
ristorante1 = Ristorante("Da Giuseppe", "Mediterranea")
ristorante2 = Ristorante("Sapori di mare", "Pesce")
ristorante3 = Ristorante("Trattoria Fratelli Rossi", "Locale")
ristorante4 = Ristorante("Sushiko", "Giapponese")


antipasto1 = Piatto("Tagliere di Salumi e Formaggi", 14.50)
antipasto2 = Piatto("Bruschette al Pomodoro", 6.00)
primo1 = Piatto("Carbonara", 12.00)
primo2 = Piatto("Amatriciana", 11.00)
primo3 = Piatto("Risotto ai Funghi Porcini", 15.00)
secondo1 = Piatto("Tagliata di Manzo con Rucola e Grana", 18.50)
secondo2 = Piatto("Cotoletta alla Milanese", 13.00)
dolce1 = Piatto("Tiramisù della Casa", 6.00)
dolce2 = Piatto("Panna Cotta ai Frutti di Bosco", 5.50)



ristorante1.aggiugi_al_menu([antipasto1,antipasto2,primo2,secondo1,secondo2,dolce1])
print("\n")
ristorante1.apri_ristorante()
ristorante1.stampa_menu()
print("\n")
ristorante1.togli_dal_menu([antipasto1,secondo2,dolce1])
print("\n")
ristorante1.stampa_menu()

            
        
        
        
    
    