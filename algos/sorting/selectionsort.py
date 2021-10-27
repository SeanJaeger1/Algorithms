def selection_sort(unsorted_array):
    sorted_array = []

    while len(unsorted_array) > 0:
        smallest_value_index = 0

        for index in range(len(unsorted_array)):
            if unsorted_array[smallest_value_index] > unsorted_array[index]:
                smallest_value_index = index

        sorted_array.append(unsorted_array.pop(smallest_value_index))

    return sorted_array


print(selection_sort([1, 7, 3, 7, 8, 3, 1, 34, 8, 4, 26, 2]))
