from sorted_array_merge import sorted_array_merge


def merge_sort(unsorted_array):
    array_length = len(unsorted_array)

    if array_length < 2:
        return unsorted_array

    splitting_point = array_length // 2
    sorted_left = merge_sort(unsorted_array[:splitting_point])
    sorted_right = merge_sort(unsorted_array[splitting_point:])

    return sorted_array_merge(sorted_left, sorted_right)
