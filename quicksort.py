def quicksort(array):
    N = len(array)
    pivot_idx = N // 2
    pivot = array[pivot_idx]
    for i in range(N):
        if array[i] >= pivot:
            j = N - 1
            while array[j] > pivot:
                j -= 1
            swap(array, i, j)
        if i == N // 2:
            break
    return quicksort(array[:N//2]) + pivot + quicksort(array[N//2 + 1:])


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def main():
    array = [3, 9, 6, 1, 2, 5, 4, 8]
    sortedArray = quicksort(array)
    print(sortedArray)


main()
