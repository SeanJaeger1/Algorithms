from heapq import heappush, heapify, heappop

graph = {
    "A": {"B": 3, "C": 8},
    "B": {"A": 3, "C": 4, "D": 12},
    "C": {"A": 8, "B": 4},
    "D": {"B": 12}
}


def prims_mst(graph):
    starting_vertex = list(graph.keys())[0]
    discovered_vertices = set([starting_vertex])
    mst = {}
    edges_to_investigate = []

    for destination, distance in graph[starting_vertex].items():
        heappush(edges_to_investigate, (distance, starting_vertex, destination))

    while edges_to_investigate:
        distance, start, end = heappop(edges_to_investigate)

        if end in discovered_vertices:
            continue

        discovered_vertices.add(end)

        if start in mst:
            mst[start].append(end)
        else:
            mst[start] = [end]

        for destination, distance in graph[end].items():
            if destination not in discovered_vertices:
                heappush(edges_to_investigate,
                         (distance, end, destination))

    return mst


print(prims_mst(graph))
