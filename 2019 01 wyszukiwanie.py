A = [5, 99, 3, 7, 111, 13, 4, 24, 4, 8]

def zad1(array):
    left = 0
    right = len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] % 2 != 0:
            left = mid + 1
        else:
            right = mid
    return array[right]

print(zad1(A))