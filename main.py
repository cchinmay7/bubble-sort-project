def get_user_input():
    return input("Enter numbers separated by spaces: ").split()

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
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break
    return arr