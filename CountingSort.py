def countingSort(array):
    N = len(array)

    indexRange = max(array) - min(array) + 1
    indexArray = []
    for i in range(indexRange):
        indexArray.append(0)

    for number in array:
        indexArray[number - 1] += 1

    for index in range(1, len(indexArray)):
        indexArray[index] = indexArray[index] + indexArray[index - 1]

    sortedArray = []
    for i in range(N):
        sortedArray.append(0)

    for item in array:
        sortedArray[indexArray[item - 1] - 1] = item
        indexArray[item - 1] -= 1

    counter = 0
    for item in sortedArray:
        array[counter] = item
        counter += 1

    return array


def main():
    array = [2, 5, 4, 3, 3, 1, 8, 7, 9, 6, 7, 5, 5, 2]
    sortedArray = countingSort(array)
    print(sortedArray)


main()