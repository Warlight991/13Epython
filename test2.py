#Töltösön fel egy listát 20 véletlen számmal 1-50 között
import random
lista = []
def veletlen():
    hossz = 20
    

  
    for item in range(hossz):
        lista.append(random.randint(1,50))

    return lista  
    
def kiir():
    for item in lista:
        print(item, end=" ")


def osszeAd():
    sum = 0
    for item in lista:
        sum = sum + item
    return sum

def kiirVeletlen():
    for i in range(20):
        print(veletlen(i))

def legnagyobbElem():
    max = lista[0]


    for item in lista:
        if item > max:
            max = item

    return max        
    


veletlen()
kiir()
print()
print(f"A lista elelmeinek összege: {osszeAd()}")
print(f"A lista elelmeinek legnagyobb értéke : {legnagyobbElem()}")