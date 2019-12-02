liczby = list(map(int, open('liczby.txt', 'r').readlines()))

def zad1(numbers):
    powers_of_3 = 0
    for number in numbers:
        for i in range(13):
            if number == 3**i:
                powers_of_3+=1
    return powers_of_3

print(zad1(liczby))