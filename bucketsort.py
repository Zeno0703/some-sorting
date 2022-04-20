from insetionsort import *


def quicksort(array):

    N = len(array)

    bucket_array = []
    for i in range(N):
        bucket_array.append([])

    for item in array:
        bucket_array[int(item // 0.10)].append(item)

    for bucket in bucket_array:
        insertion_sort(bucket)

    counter = 0
    for bucket in bucket_array:
        for item in bucket:
            array[counter] = item
            counter += 1

    return array


def main():
    array = [0.28, 0.34, 0.65, 0.12, 0.33, 0.88, 0.56, 0.55, 0.44, 0.78, 0.32, 0.37, 0.78, 0.99, 0.12, 0.93]
    sortedArray = quicksort(array)
    print(sortedArray)

main()