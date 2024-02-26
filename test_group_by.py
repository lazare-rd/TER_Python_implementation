import pytest
from group_by import group_by

def test_group_by1():
    keys = ['A', 'A', 'B', 'C', 'A', 'C', 'B']
    values = [2, 4, 8, 9, 5, 3, 1]
    assert group_by(keys, values) == {'A': 11, 'B': 9, 'C': 12}

def test_group_by2():
    keys = ['A', 'A', 'B', 'C', 'A', 'C', 'B']
    values = [2, 4, 8, 9, 5, 3]
    with pytest.raises(ValueError):
        group_by(keys, values)