def quick_sort(unsorted_array):
    if len(unsorted_array) < 2:
        return unsorted_array

    pivot_value, left_array, equal_array, right_array = (
        unsorted_array[len(unsorted_array) // 2],
        [],
        [],
        [],
    )

    for value in unsorted_array:
        if value < pivot_value:
            left_array.append(value)
        elif value == pivot_value:
            equal_array.append(value)
        else:
            right_array.append(value)

    return quick_sort(left_array) + equal_array + quick_sort(right_array)


print(
    quick_sort(
        [9, 8, 7, -6, 5.2, 6, 2, 7, -8, 4, 6, 3, 7, 2, 9, 5, 8, 0, -4, 3, 3, 2, 1]
    )
)
