def quicksort(array):
    N = len(array)
    if N <= 1:
        return array
    else:
        pivot = array.pop()

    left_array = []
    right_array = []

    for i in array:
        if i > pivot:
            right_array.append(i)
        else:
            left_array.append(i)

    return quicksort(left_array) + [pivot] + quicksort(right_array)


def main():
    array = [3, 9, 6, 1, 2, 5, 4, 8]
    sortedArray = quicksort(array)
    print(sortedArray)


main()
