def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array.pop()

    left_array = []; right_array = []

    for i in array:
        place_in_array(left_array, right_array, i, pivot)

    return quicksort(left_array) + [pivot] + quicksort(right_array)


def place_in_array(smaller, greater, item, pivot):
    if item > pivot:
        greater.append(item)
    else:
        smaller.append(item)


def main():
    array = [3, 9, 6, 1, 2, 5, 4, 8]
    sortedArray = quicksort(array)
    print(sortedArray)


main()
