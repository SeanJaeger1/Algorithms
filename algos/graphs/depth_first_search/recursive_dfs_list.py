graph = {
    "A": ["D", "C"],
    "B": ["F", "G", "E"],
    "C": ["A", "D", "F", "G"],
    "D": ["A", "C"],
    "E": ["B", "F"],
    "F": ["B", "C", "E"],
    "G": ["B", "C"],
}


def depth_first_search(graph, starting_node, visited=[]):
    if starting_node in visited:
        return []

    new_nodes = [starting_node]

    for node in graph[starting_node]:
        new_nodes += depth_first_search(graph, node, visited + new_nodes)

    return new_nodes


print(depth_first_search(graph, "A"))
