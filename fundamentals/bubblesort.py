def bubble_sort(unsorted_array):
    array_length = len(unsorted_array)

    for i in range(array_length - 1):
        for j in range(array_length - i - 1):
            if unsorted_array[j] > unsorted_array[j + 1]:
                unsorted_array[j + 1], unsorted_array[j] = (
                    unsorted_array[j],
                    unsorted_array[j + 1],
                )

    return unsorted_array


print(
    bubble_sort(
        [9, 8, 7, -6, 5.2, 6, 2, 7, -8, 4, 6, 3, 7, 2, 9, 5, 8, 0, -4, 3, 3, 2, 1]
    )
)
