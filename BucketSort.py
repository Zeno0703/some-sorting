from InsertionSort import *


def bucketSort(array):

    bucketArray = createBucketArray(len(array))
    appendItemsInBuckets(array, bucketArray)
    sortBuckets(bucketArray)
    restoreSortedItems(array, bucketArray)

    return array


def createBucketArray(N):
    bucketArray = []
    for i in range(N):
        bucketArray.append([])
    return bucketArray


def appendItemsInBuckets(array, bucketArray):
    for item in array:
        bucketArray[int(item // 0.10)].append(item)


def sortBuckets(bucketArray):
    for bucket in bucketArray:
        insertionSort(bucket)


def restoreSortedItems(array, bucketArray):
    counter = 0
    for bucket in bucketArray:
        for item in bucket:
            array[counter] = item
            counter += 1


def main():
    array = [0.28, 0.34, 0.65, 0.12, 0.33, 0.88, 0.56, 0.55, 0.44, 0.78, 0.32, 0.37, 0.78, 0.99, 0.12, 0.93]
    sortedArray = bucketSort(array)
    print(sortedArray)


main()
