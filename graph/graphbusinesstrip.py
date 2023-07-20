
def business_trip(graph, cities):

    total_cost = 0

    for i in range(len(cities) - 1):
        if cities[i] not in graph or cities[i + 1] not in graph[cities[i]]:
            return None

        total_cost += graph[cities[i]][cities[i + 1]]
    return total_cost

