import pytest
from hashmapLeftJoin.hashmapLeftJoin import left_join

def test_left_join():
    hashmap1 = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger"
    }

    hashmap2 = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight"
    }

    output = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", None],
        ["wrath", "anger", "delight"]
    ]

    new_hashmap = left_join(hashmap1, hashmap2)
    assert new_hashmap == output
