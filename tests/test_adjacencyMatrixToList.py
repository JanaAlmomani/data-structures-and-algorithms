from adjacencyMatrixToList.adjacencyMatrixToList import *
import pytest

def test_adjacency_matrix_to_list_num1():
    vertices= []
    matrix= []
    
    adj_list= adjacency_matrix_to_list(vertices, matrix)
    assert adj_list == {}

def test_adjacency_matrix_to_list_num2():
    vertices = ['J', 'A', 'N']
    matrix = [
        ['0', '1', '1'],
        ['1', '0', '1'],
        ['0', '1', '0']
    ]

    adj_list = adjacency_matrix_to_list(vertices, matrix)

    assert adj_list == {
        'J': ['A', 'N'],
        'A': ['J', 'N'],
        'N': ['A']
    }

def test_adjacency_matrix_to_list_num3():

    vertices = ['J', 'A', 'N', 'A']
    matrix = [
        ['0', '1', '1', '1'],
        ['1', '0', '1', '1'],
        ['0', '1', '0', '1']
    ]

    with pytest.raises(ValueError, match="Number of vertices must match the size of the matrix"):
        adjacency_matrix_to_list(vertices, matrix)