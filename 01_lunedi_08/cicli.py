#while, ripete qualcosa quando la condizione nel while è vera. 
# si usa QUANDO NON SO NON o NON VOGLIO QUANTE VOLTE SI DEVE RIPETERE ( CONTESTI INDEFINITI)
conteggio = 0
while conteggio < 5:
    print(conteggio)
    conteggio+= 1
    
print(conteggio)

controllore = True
while controllore:
    print("ciao")
    
    #esercizi
    
    
    scelta = input("vuoi continuare?") #quando scelgo no
    if scelta == "no":
        controllore=False #imposto controllore a false, quindi quando ritorna al while controlle = False ed esce dal ciclo
    

#for
#ciclo su qualcosa di DEFINITO. LISTA, STRINGHE, TUPLE, OGGETTI
numeri =[1,2,3]
for elemento in numeri:
    print(elemento)

print("range")   
#range([start], stop, [step])
print("primo range")
for i in range(5):
    print(i)
print("secondo range")    
for i in range(2,8):
    print(i) #stampa da 2 a 7, 8 escluso
print("terzo range")  
for i in range(1,10,2):
    print(i) #stampa da 1 fino a 9 con un salto di 2