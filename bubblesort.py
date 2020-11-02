def bubblesort(array = [4,1,3,5]):
    arrayLength = len(array)

    for i in range(arrayLength - 1):

        for j in range(arrayLength - 1 - i):

            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]

    return array

print(bubblesort())