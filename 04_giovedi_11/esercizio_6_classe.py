""" Crea una classe chiamata Animale. Questa classe deve avere:

Un attributo di classe numero_animali, inizializzato a 0.

Due attributi di istanza: nome e specie, passati al costruttore.

Il costruttore deve incrementare numero_animali di 1 ogni volta che viene creato un nuovo animale.

Un metodo di classe quanti_animali che stampi una stringa del tipo "Numero di animali creati: 'numero_animali'".

Crea almeno 3 oggetti Animale e poi chiama quanti_animali direttamente dalla classe, senza usare nessuna delle istanze create."""


class Animale:
    
    numero_animali = 0
    
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie
        #self.numero_animali +=1 #SBAGLIATO! perchè crea per ogni istanza una nuova variabile locale e quella globale rimane a zero
        #print(self.numero_animali) #OUTPUT (1,2,3) se non commento la riga sotto ma mi aspettavo 1,1,1
        Animale.numero_animali +=1 # DA RICORDARE Animale.numero_animali perchè devo riferirmi alla variabile di classe globale
    
    def __str__(self):
        #print(f"Animale: {self.nome} - {self.specie}") NON DEVO USARE PRINT
        return(f"Animale: {self.nome} - {self.specie}") #MA RETURN
    
    @classmethod
    def quanti_animali(cls):
        print("Numero animali creati: ", cls.numero_animali)
        

animale1 = Animale("gatto", "Felino")
animale2 = Animale("delfino", "Mammifero")
animale3 = Animale("pinguino", "Mammifero")

print(animale1)
print(animale2)
print(animale3)

Animale.quanti_animali()