import math

liczby = list(map(int, open('liczby.txt', 'r').readlines()))

def zad1(numbers):
    powers_of_3 = 0
    for number in numbers:
        for i in range(13):
            if number == 3**i: powers_of_3+=1
    return powers_of_3

def zad2(numbers):
    for number in numbers:
        if sum([math.factorial(x) for x in list(map(int, [str(a) for a in str(number)]))]) == number: print(number)

print('Zadanie 1:')
print(zad1(liczby))
print('\nZadanie 2:')
zad2(liczby)