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

def zad3(numbers):
    first_number, length, gcd, max_length = 0, 0, 0, [0, 0, 0]
    for i in range(1, len(numbers)):
        first_number, gcd, length = numbers[i-1], math.gcd(numbers[i-1], numbers[i]), 1
        while gcd>1:
            length+=1
            try: gcd = math.gcd(gcd, numbers[i+length-1])
            except: break
        if length>max_length[1]: max_length = [first_number, length, gcd]
    print('Pierwsza liczba ciągu:', max_length[0], '\nDługość:', max_length[1], '\nNajwiększy wspólny dzielnik:', max_length[2])

print('Zadanie 4.1:')
print(zad1(liczby))
print('\nZadanie 4.2:')
zad2(liczby)
print('\nZadanie 4.3:')
zad3(liczby)