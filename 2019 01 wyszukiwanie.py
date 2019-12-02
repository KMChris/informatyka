
"""
Małgosia i Jaś lubią liczby. Małgosia lubi liczby nieparzyste, a Jaś lubi liczby parzyste. Każde
z dzieci zapisało po kilka spośród swoich ulubionych liczb na jednej wspólnej kartce. Najpierw
Małgosia zapisała wszystkie swoje liczby, a potem Jaś dopisał swoje. 

Napisz algorytm (w postaci listy kroków, w pseudokodzie lub w wybranym języku
programowania), który dla danego ciągu liczb zapisanych przez dzieci znajdzie pierwszą liczbę
zapisaną przez Jasia. Zakładamy, że każde z dzieci zapisało co najmniej jedną liczbę.
Przy ocenie będzie brana pod uwagę złożoność czasowa Twojego algorytmu. Maksymalną
liczbę punktów uzyskasz za algorytm o złożoności lepszej niż liniowa.
Uwaga: W zapisie algorytmu możesz wykorzystać tylko operacje arytmetyczne (dodawanie,
odejmowanie, mnożenie, dzielenie, dzielenie całkowite, reszta z dzielenia), instrukcje
porównania, instrukcje sterujące i przypisania do zmiennych lub samodzielnie napisane
funkcje, wykorzystujące wyżej wymienione operacje
"""

from random import randint


A = []

# Małgosia 
for x in range(randint(2,8)):
    k = randint(1,100)
    while k % 2 == 0:
        k = randint(1,100)
    A.append(k)



#Jaś
for x in range(randint(2,8)):
    k = randint(1,100)
    while not (k % 2 == 0):
        k = randint(1,100)
    A.append(k)

#print(A)

if randint(0,1):
    A.reverse()

n = len(A)-1 #podadzą w zadaniu

def zad1(A):
    if (A[0] %2 ==0):
        return A[0]

    left = 1 
    right = n
    while left < right:
        mid = (left+right)//2
        if A[mid]%2 != 0:  
            left = mid + 1
        else:                 
            right = mid
    return A[right]


print(A)
print(zad1(A))
