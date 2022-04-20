def quickSort(array):
    if len(array) <= 1:
        return array

    pivot = array.pop()

    leftArray = []; rightArray = []

    for i in array:
        placeInArray(leftArray, rightArray, i, pivot)

    return quickSort(leftArray) + [pivot] + quickSort(rightArray)


def placeInArray(left, right, item, pivot):
    if item > pivot:
        right.append(item)
    else:
        left.append(item)


def main():
    array = [3, 9, 6, 1, 2, 5, 4, 8]
    sortedArray = quickSort(array)
    print(sortedArray)


main()