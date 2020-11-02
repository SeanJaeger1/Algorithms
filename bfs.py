graph = {
    "A": ["D", "C"],
    "B": ["F", "G", "E"],
    "C": ["A", "D", "F", "G"],
    "D": ["A", "C"],
    "E": ["B", "F"],
    "F": ["B", "C", "E"],
    "G": ["B", "C"]
}


def breadth_first_search(starting_node, graph):
    queue, discovered = [], []

    queue.append(starting_node)
    discovered.append(starting_node)

    while queue:
        s = queue.pop(0)

        for neighbour in graph[s]:
            if neighbour not in discovered:
                queue.append(neighbour)
                discovered.append(neighbour)

    return discovered


print(breadth_first_search("A", graph))
