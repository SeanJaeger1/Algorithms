def sorted_array_merge(first_array, second_array):
    first_index, second_index, merged_array = 0, 0, []

    while first_index < len(first_array) and second_index < len(second_array):
        if first_array[first_index] < second_array[second_index]:
            merged_array.append(first_array[first_index])
            first_index += 1
        else:
            merged_array.append(second_array[second_index])
            second_index += 1

    if first_index < len(first_array):
        merged_array = merged_array + first_array[first_index:]

    if second_index < len(second_array):
        merged_array = merged_array + second_array[second_index:]

    return merged_array


print(sorted_array_merge([0, 4, 7, 19], [1, 4, 5, 7, 8, 9]))
