graph = {
    "A": ["D", "C"],
    "B": ["F", "E"],
    "C": ["A", "F", "G"],
    "D": ["A", "C"],
    "E": ["B"],
    "F": ["B"],
    "G": ["B", "C"],
}


def reverse_adjacency_list(adjacency_list):
    new_adjacency_list = {}

    for key in adjacency_list:
        for edge in adjacency_list[key]:
            if edge in new_adjacency_list:
                if key not in new_adjacency_list[edge]:
                    new_adjacency_list[edge].append(key)
            else:
                new_adjacency_list[edge] = [key]

    return new_adjacency_list


print("starting adjacency list:")
print(graph)
print("reversed adjacency list:")
print(reverse_adjacency_list(graph))
