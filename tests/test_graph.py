import pytest 
from graph.graph import *

def test_add_vertex():
    graph=Graph()
    vertex=graph.add_vertex("A")
    vertices=graph.get_vertices()

    assert vertex in vertices

def test_add_edge():
    graph=Graph()
    vertex1=graph.add_vertex("A")
    vertex2=graph.add_vertex("B")
    graph.add_edge(vertex1, vertex2)

    neighbors=graph.get_neighbors(vertex1)
    assert len(neighbors) == 1

def test_get_vertices():
    graph = Graph()
    vertex1=graph.add_vertex("A")
    vertex2=graph.add_vertex("B")
    vertices=graph.get_vertices()

    assert len(vertices) == 2

def test_get_neighbors():
    graph = Graph()
    vertex1 = graph.add_vertex("A")
    vertex2 = graph.add_vertex("B")
    graph.add_edge(vertex1, vertex2)
    neighbors = graph.get_neighbors(vertex1)

    assert len(neighbors) == 1

def test_size():
    graph = Graph()
    vertex1 = graph.add_vertex("A")
    vertex2 = graph.add_vertex("B")
    
    assert graph.size() == 2

def test_size_zero():
    graph = Graph() 
    assert graph.size() == 0

    