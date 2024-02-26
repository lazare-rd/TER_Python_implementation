from merge_sort import mergesort

def test_merge_sort():
    a = [5,9,1,3,4,6,6,3,2]
    assert mergesort(a) == [1, 2, 3, 3, 4, 5, 6, 6, 9]