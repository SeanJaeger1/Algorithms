from collections import deque

graph = {
    "A": ["D", "C"],
    "B": ["F", "G", "E"],
    "C": ["A", "D", "F", "G"],
    "D": ["A", "C"],
    "E": ["B", "F"],
    "F": ["B", "C", "E"],
    "G": ["B", "C"]
}


def depth_first_search(starting_node, graph):
    queue, discovered = deque([starting_node]), []

    while queue:
        current_node = queue.pop()

        if current_node not in discovered:
            discovered.append(current_node)

            for neighbour in graph[current_node]:
                if neighbour not in discovered:
                    queue.append(neighbour)

    return discovered


print(depth_first_search("A", graph))
