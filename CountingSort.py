def countingSort(array):

    indexArray = createIndexArray(array)
    sortedArray = createSortedArray(array, indexArray)
    restoreSorted(array, sortedArray)

    return array


def createIndexArray(array):
    indexRange = max(array) - min(array) + 1
    indexArray = []
    for i in range(indexRange):
        indexArray.append(0)

    initializeIndexArray(array, indexArray)

    return indexArray


def initializeIndexArray(array, indexArray):
    for number in array:
        indexArray[number - 1] += 1

    for index in range(1, len(indexArray)):
        indexArray[index] = indexArray[index] + indexArray[index - 1]


def createSortedArray(array, indexArray):
    sortedArray = []
    for i in range(len(array)):
        sortedArray.append(0)

    fillSortedArray(array, indexArray, sortedArray)

    return sortedArray


def fillSortedArray(array, indexArray, sortedArray):
    for item in array:
        sortedArray[indexArray[item - 1] - 1] = item
        indexArray[item - 1] -= 1


def restoreSorted(array, sortedArray):
    counter = 0
    for item in sortedArray:
        array[counter] = item
        counter += 1


def main():
    array = [2, 5, 4, 3, 3, 1, 8, 7, 9, 6, 7, 5, 5, 2]
    sortedArray = countingSort(array)
    print(sortedArray)


main()