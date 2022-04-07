def selection_sort(array):
    N = len(array)
    for i in range(N):
        minimum = i
        for j in range(i+1, N):
            if array[j] < array[minimum]:
                minimum = j
        exchange(array, i, minimum)
    return array


def exchange(array, i, j):

    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def main():

    array = [6, 3, 9, 2, 1, 5]
    sorted_array = selection_sort(array)


main()
