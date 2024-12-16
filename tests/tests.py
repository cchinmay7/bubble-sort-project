from main import bubble_sort

def test_sort_numbers():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([]) == []
    assert bubble_sort([5, 5, 5]) == [5, 5, 5]
    assert bubble_sort([-1, 3, -2, 2]) == [-2, -1, 2, 3]
