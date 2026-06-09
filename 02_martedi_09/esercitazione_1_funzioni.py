""" """
import random
print(" fibonacci------------------------")
def fibonacci(n):
# (a)1 + (b)1 = 2
# (a)1 + (b)2 = 3
# 2+ 3 = 5
    a=0, b=1
    serie = []
    while a < n:
        serie.append(a)
        
        prossimo = a + b
        
        a = b
        b = prossimo   
    return serie

for numero in fibonacci(15):
    print(numero)


###############################################################################################

print(" indovina numero------------------------")
def indovinaNumero(n):
    if n == numero_casuale:
        print("Bravo! hai indovinato")
        return n
    elif n < numero_casuale:
        print("il numero generato è più alto")
    else:
        print("numero generato più basso")
        
    
numero_casuale = random.randint(1,100)
print("il numero casuale scelto è:", numero_casuale)

controllo = True
while controllo:
    scelta = input("inserisci il tuo numero: ")
    
    numero_inserito = int(scelta) # ilnumero che inserisco
    indovinato = indovinaNumero(numero_inserito) #controllo se l'ho indovinato e ritorno il valore solo in quel caso
    
    if scelta == "esci" or indovinato: #esco dal gioco se scrivo esci o indovinato è diverso da null
        controllo =False
        print("il numero era", indovinato)
    
    




        
    