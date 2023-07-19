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

def test_breadth_first_num1():
    graph = Graph()
    vertex1 = graph.add_vertex("A")
    vertex2 = graph.add_vertex("B")
    graph.add_edge(vertex1, vertex2)
    BFT = graph.breadth_first(vertex1)
    assert [str(node) for node in BFT] == ['A','B']


def test_breadth_first_num2():
    graph = Graph()
    vertex1 = graph.add_vertex("J")
    BFT = graph.breadth_first(vertex1)
    assert [str(node) for node in BFT] == ['J']


def test_breadth_first_num3():
    graph = Graph()
    BFT = graph.breadth_first(None)
    assert [str(node) for node in BFT] == []

    