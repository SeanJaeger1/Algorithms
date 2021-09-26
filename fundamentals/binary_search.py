def binary_search(value, array):
    # Either the final value in array is the wanted value, or it doesnt exist within the array.
    if len(array) == 1:
        if array[0] == value:
            return 0
        else:
            return -1

    pivot_index = len(array) // 2 - 1

    # If the value we're looking for is less than the pivot, cut the array in half and retry on the first half
    # otherwise, add one to the pivot index to account for this being the second half, and retry on the second half
    if array[pivot_index] > value:
        recursion_result = binary_search(value, array[:pivot_index])
        if recursion_result == -1:
            return -1
        else:
            return recursion_result
    elif array[pivot_index] == value:
        return pivot_index
    else:
        recursion_result = binary_search(value, array[pivot_index + 1 :])
        if recursion_result == -1:
            return -1
        else:
            return pivot_index + 1 + recursion_result


print(binary_search(2000, [i for i in range(2000)]))
