class Node:
    def __init__(self,value=None):
        self.value=value
    def __str__(self):
        return self.value

class Edge:
    def __init__(self,vertex, weight=0):
        self.vertex = vertex
        self.weight = weight
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, value):
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex
    
    def add_edge(self,vertex1, vertex2, weight=0):

        if not vertex1 in self.adj_list.keys():
            return("this node does not exist")
        
        if not vertex2 in self.adj_list.keys():
            return("this node does not exist")
        
        edge1 = Edge(vertex2, weight)
        self.adj_list[vertex1].append(edge1)

        edge2 = Edge(vertex1, weight)
        self.adj_list[vertex2].append(edge2)

    
    def get_vertices(self):
        return list(self.adj_list.keys())
    
    def get_neighbors(self,vertex):
        if vertex in self.adj_list.keys():
            return self.adj_list[vertex]
        else:
            return []
        
    def size(self):
        return len(self.adj_list.keys())

    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge.vertex} -----> '
            output += '\n'
        return output
        