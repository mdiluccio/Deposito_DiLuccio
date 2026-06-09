"""
pass è un modo per inserire l'architettura senza inserire nulla
continue salta il numero nella condizione if e passa al successivo
break si ferma e esce dal ciclo
* operatore splat, espande una lista [], una tupla o un range (crea valori progressivi da 1 a 10) secondo i valori in [*range(1,11)]
"""

for i in range(5):
    if i==3:
        pass
    print(i)
    
for i in range(5):
    if i==3:
        continue
    print(i)
    
for i in range(5):
    if i==3:
        break
    print(i)

print("esempi continue -----")
numeri = [1,2,3,4]
for numero in numeri:
    if numero == 2:
        continue
    print(numero)
    
print("esempi break -----")
numeri = [1,2,3,4]
for numero in numeri:
    if numero == 2:
        break
    print(numero)
    


numeri = [*range(1,11)]
print(numeri)