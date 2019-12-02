lista = [5, 99, 3, 7, 111, 13, 4, 24, 4, 8]


def zad1(A):

    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] % 2 != 0:
            left = mid + 1
        else:
            right = mid
    return A[right]


print(zad1(lista))
