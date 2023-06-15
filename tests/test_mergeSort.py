import pytest
from Merge_Sort.Merge_Sort import merge_sort

def test_marge_sort():

    arr = [20,18,12,8,5,-2]
    merge_sort(arr)
    assert arr == [-2,5,8,12,18,20]

    arr = [5,12,7,5,5,7]
    merge_sort(arr)
    assert arr == [5,5,5,7,7,12]

    arr = [2,3,5,7,13,11]
    merge_sort(arr)
    assert arr == [2,3,5,7,11,13]
