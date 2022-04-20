def selectionSort(array):
    for i in range(len(array)):
        minimum = getMinimum(array, i)
        exchange(array, i, minimum)
    return array


def getMinimum(array, i):
    minimum = i
    for j in range(i + 1, len(array)):
        if array[j] < array[minimum]:
            minimum = j
    return minimum


def exchange(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def main():

    array = [6, 3, 9, 2, 1, 5]
    sortedArray = selectionSort(array)
    print(sortedArray)


main()
