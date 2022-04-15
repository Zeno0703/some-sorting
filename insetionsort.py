def insertion_sort(array):
    for i in range(len(array)):
        j = i
        while j > 0 and less(array[j], array[j-1]):
            exch(array, j, j-1)
            j -= 1
    return array


def less(i, j):
    return i < j


def exch(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def main():
    array = [3, 8, 1, 9, 6, 4, 5, 2, 7]
    sortedArray = insertion_sort(array)
    print(sortedArray)


main()
