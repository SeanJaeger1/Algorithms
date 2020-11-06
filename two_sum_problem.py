def two_sum(array, sum):
    pairs = []
    number_of_duplicates = 0
    array_dict = {
        value: None for value in array
    }
    duplicate_number = sum // 2

    for value in array:
        required_pair_value = sum - value

        if required_pair_value in array_dict.keys():
            if value == required_pair_value:
                number_of_duplicates += 1
            else:
                pairs.append("{0} and {1} is a pair".format(
                    value, required_pair_value
                ))

    if number_of_duplicates > 0:
        # if there's any duplicates, generate the number of duplicate pairs and
        # append these pairs to the pairs array, removing the case where the value
        # matches with itself in the dict
        number_of_duplicate_sum_pairs = number_of_duplicates**2 - number_of_duplicates

        duplicate_pairs = [
            "{0} and {0} is a pair".format(
                duplicate_number
            ) for i in range(number_of_duplicate_sum_pairs)
        ]

        pairs += duplicate_pairs

    return pairs


print(two_sum([0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 1))
