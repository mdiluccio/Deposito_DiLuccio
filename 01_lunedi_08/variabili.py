nome = "Alice"
eta = 25
print("Il mio nome è", nome, "e ho", eta, "anni") # la virgola mette uno spazio tra le parole, è più comodo per concatenare stringhe e variabili

# nome = input("inserici il tuo nome: ") # input di default inserisce caratteri
# eta = int (input("inserici la tua età: ")) # quindi se voglio un intero lo converto
print ("Ciao, " + nome +"! Benvenuto in python!" ) # concatenazione di stringhe, con + NON mette lo spazio, quindi se voglio uno spazio devo metterlo tra virgolette

print("------------- operatori aritmetici-------")
print(1+5) #somma
print(6-5) # differenza
print(3*2) # moltiplicazione
print(4/2) # divisione
print(3**2) # potenza, 3 alla seconda

#variabili primitive
print("------------- variabili intere-------")
x = 10 # x è una variabile di tipo intero, che contiene il valore 10
y = -5 

print("------------- variabili con virgola mobile-------")
a = 3.14 # a è una variabile di tipo float, che contiene il valore 3.14
b = -1.0

print("------------- variabili stringhe-------")
# ogni lettera è un valore, quindi una stringa è una sequenza di valori
#possono accedere ai metodi e alle funzioni che operano sulle stringhe, come len(), upper(), lower(), replace(), split()
nome = 'Alice'
msg ="Ciao" 

s = "Python" # 6 POSIZIONI, 5 LETTERE
print(s[0]) # POSIZIONE 0, stampa la prima lettera della stringa, che è P
print(s[1]) # POSIZIONE 1, stampa la seconda lettera della stringa, che è y
print(s[2]) # POSIZIONE 2, stampa la terza lettera della stringa, che è t

# FUNZIONI E METODI sono seguiti dal nome e parentesi ()
print(len(s)) # funzione incorporata perchè non è richiamata da un oggetto
print(s.upper()) # metodo (perchè è richiamato da un oggetto) che converte stringa in maiuscolo, 
print(s.lower()) # metodo perchè è richiamato da un oggetto) che converte stringa in minuscolo, 
print(s.replace("P", "J")) # metodo che sostituisce la lettera P con la lettera J
print(s.split(",")) # metodo che divide la stringa in una lista di stringhe, usando la , come separatore

print("------------- variabili booleane-------")
# variabili che possono assumere solo due valori: True (1) o False (0)
# operatori di confronto <, >, ==, <=, >=, !=
print (3 < 5) # 3 < 5 true
print(3==5) # 3 è uguale a 5 false, stesso tipo e stesso valore
print(3>5) #3 è maggiore di 5 false
print(3<=5) #3 è minore o uguale a 5 true
print(3>=5) #3 è maggiore o uguale a 5 false
print(3!=5) #3 è diverso da 5 true

print("------------- operatori logici-------")
# operatori logici  and, or, not appartengono alla LOGICA
print (3 < 5 and 4 > 6) # true se entrambi i valori sono true
print (7>2 or 2>2) # true se almeno uno dei valori è true
print (not 7 > 3) # false se il valore è true, true se il valore è false

print(3<5 and 4>6 or 7>2) # l'ordine di precedenza è: not, and, or
print(3<5 or 4>6 and 7>2) # l'ordine di precedenza è: not, and, or

 
print("------------- liste o collezioni------")
# rappresentate dal tipo list e sono racchiuse da []. 
# TIPO OMOGENEO: tutti gli elementi sono dello stesso tipo
# TIPO MODIFICABILE: è possibile modificare gli elementi della collezione
# TIPO ORDINATO: gli elementi sono ordinati, quindi è possibile accedere agli elementi tramite l'indice che inizia da 0
# TIPO ETEROGENEO: gli elementi sono di tipi diversi
# NON SONO ARRAY. gLI ARRAY sono omogenei, hanno lunghezza fissa. Le liste sono eterogenee con len variabile

numeri = [1, 2, 3, 4, 5] # lista di numeri interi
nomi = ["Alice", "Bob", "Charlie"] # lista di stringhe, omegenea
misto = [1, "Alice", 3.14, True] # tipo eterogeneo

print("La lista dei numeri è:", numeri)
print("La lista dei nomi è:", nomi)
print("La lista mista è:", misto)
