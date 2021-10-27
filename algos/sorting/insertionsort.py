def insertion_sort(array):
    for index in range(1, len(array)):
        inserted_variable_index = index

        while (
            inserted_variable_index > 0
            and array[inserted_variable_index] < array[inserted_variable_index - 1]
        ):
            array[inserted_variable_index], array[inserted_variable_index - 1] = (
                array[inserted_variable_index - 1],
                array[inserted_variable_index],
            )
            inserted_variable_index = inserted_variable_index - 1

    return array


print(insertion_sort([7, 1, 7, 3, 8, 4, 25, 8, 2, 4]))
