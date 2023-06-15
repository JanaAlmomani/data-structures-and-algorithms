import pytest
from Insertion_Sort.Insertion_Sort import InsertionSort

def test_Insertion_Sort():
    arr = [20,18,12,8,5,-2]
    sorted_arr = InsertionSort(arr)
    assert  sorted_arr == [-2,5,8,12,18,20]

    arr = [5,12,7,5,5,7]
    sorted_arr = InsertionSort(arr)
    assert  sorted_arr == [5,5,5,7,7,12]

    arr = [2,3,5,7,13,11]
    sorted_arr = InsertionSort(arr)
    assert  sorted_arr == [2,3,5,7,11,13]

