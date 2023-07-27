def adjacency_matrix_to_list(vertices, matrix):
    if len(vertices) != len(matrix):
        raise ValueError("Number of vertices must match the size of the matrix")
    adjacency_list = {}
    for i in range(len(vertices)):
        vertex = vertices[i]
        adjacency_list[vertex] = []

        for j in range(len(vertices)):
            if matrix[i][j] == "1":
                adjacent_vertex = vertices[j]
                adjacency_list[vertex].append(adjacent_vertex)

    return adjacency_list

# Input data 
vertices = ['J', 'A', 'N', 'A', 'A']
matrix = [
    ['0', '1', '0', '0', '1'],
    ['1', '0', '1', '1', '0'],
    ['0', '1', '0', '1', '0'],
    ['0', '1', '1', '0', '1'],
    ['1', '0', '0', '1', '0']
]
adj_list = adjacency_matrix_to_list(vertices, matrix)
# Print
for vertex, neighbors in adj_list.items():
    print(f"{vertex}| -> {' -> '.join(neighbors)}")
