def get_user_input():
    return input("Provide numbers (space-separated) in one line: ").split()

def swap(a, b):

    temp = a
    a = b
    b = temp

def bubble_sort(arr):
    """
    Sorts a list using the Bubble Sort algorithm.

    :param arr: List of elements to be sorted
    :return: Sorted list
    """
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Flag to track if any swaps are made
        swapped = False
        # Last i elements are already sorted, so skip them
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                swap(arr[j], arr[j + 1])
                swapped = True
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break
    return arr

def validate_input(arr):
    """
    Validates the input array for the Bubble Sort algorithm.

    :param arr: Input array to be sorted
    :raises TypeError: If input is not a list
    :raises ValueError: If list contains non-comparable elements
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements in the list must be integers or floats.")