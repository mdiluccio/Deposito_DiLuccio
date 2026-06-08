# Capacità alterare la lettura del codice ripetendo o escludendo parti di esse
#if
numero = 10
#stampa SOLO a
if (numero ==10):
    print("vero")#a
    
if(numero !=10): #se diverso da 10 
    print("falso") #b, non viene esguito perchè stampa solo se numero!=10 è true


#stampa a o b 
if numero > 0:
    print("il numero è positivo") #a
else:
    print("il numero è negativo o zero") #b


if numero > 0:
    print("il numero è positivo") #a
    if numero == 100:
        print("il numero è 100") #a.1
#elif è inclusivo cioè include qualcosa in piu rispetto a if
elif numero < 0: #altrimenti se numero è minore di 0
    print("il numero è negativo") #b
else: #altrimenti se non è nessuno dei due sopra
    print("il numero è zero") #c
    
    
#match, evita di avete tanti if con elif
comando = input("inserisci un comando: ")
match comando: 
    case "start":
        print("avvio del programma.")
    case "stop":
        print("Chiusura del programma.")
    case "pausa":
        print("Programma in pausa")
    case _: # _ è il default
        print("comando non riconosciuto")


