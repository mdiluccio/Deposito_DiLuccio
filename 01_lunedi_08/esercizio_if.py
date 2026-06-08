#esercizio
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome:")
eta = int(input("Inserisci la tua età: "))
 
if nome =="Massimo" and cognome == "Di Luccio":
    print("Ciao", nome, cognome)
    if eta >= 30:
        print("eta", eta)
else:
    print("il nome o il cognome inseriti sono diversi da", nome, cognome)   
    

print("Menu di selezione: inserisci un valore tra aggiungi, modifica o ricerca")
valore = input("Inserisci il valore: ")
if valore == "ricerca" :
    print("Hai inserito ricerca");
elif valore == "aggiungi":
    print("hai selezionato aggiungi")
elif valore == "modifica":
    print("hai selezionato modifica")
    
#----------------------------------------------------------------------------------------#
print("Benvenuto, fai log in o registrati")
risposta = input("cosa vuoi fare?:")

if risposta == "log in":
    nome = input("Inserisci il tuo nome: ")
    password = input("Inserisci la tua password:")
    if nome == "" and password =="":
        print("errore, nome o password errati")
    else:
       print("Benvenuto", nome +"!")
else:
    print("crea il tuo account")
    nome = input("Inserisci il tuo nome: ")
    password = input("Inserisci la tua password:")
    print("Nuovo account creato")
