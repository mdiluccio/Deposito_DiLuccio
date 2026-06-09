"""
scrivi un sistema che prende in input una lista di numeri che è stata valorizzata dall'utente
1. ciclo for per trovare in max nella lista
2.while epr contare quanti numeri ci sono nella lista
3.if per stampare lista vuota se la lista è vuota altrimentistampare in max trovato e il numero di elementi    
    
"""
#dichiaro lista
numeri = []
#input
nr_elementi = int(input("quanti elementi vuoi inserire: "))

#append nella lista
inseriti = 0
while inseriti < nr_elementi:
    numero = int(input("numero: "))
    numeri.append(numero)
    inseriti += 1

print(numeri)

#for per trovare il max
max = numeri[0]
for num in numeri:
    if num > max:
        max = num
#while per contare quanti elementi
count = 0
while count < len(numeri):
    count +=1

#if check se lista è vuota e stampo lista vuota
if len(numeri) == 0:
    print("lista vuota")
#altrimenti numero massimo e quanti elementi
else:
    print("il numero massimo è:", max, "- elementi nella lista:", count )