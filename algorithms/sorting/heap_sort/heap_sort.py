"""Implementation of Heap Sort algorithm."""

from typing import List


def heapify(arr: List[int], n: int, i: int) -> None:
    """Heapify Function.

    This function ensures that the elements follow the max-heap property:
    each parent’s value is greater than or equal to its children's values.

    Parameters:
    arr (list): A list of numbers representing the heap.
    n (int): The number of elements in the heap.
    i (int): The index of the root of the subtree to heapify.

    """
    # Initialize largest as root, and set left and right child indices
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2

    # Check if left exists and greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right exists and greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not largest, swap with the largest child
    # Continue heapifying to maintain the max-heap property
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: List[int]) -> List[int]:
    """Heap Sort Function.

    Parameters:
    arr (list): A list of unordered numbers.

    Returns:
    list: The sorted list.
    """
    # Get the number of elements in the array
    n = len(arr)

    # Build a max heap from the array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    # Return the sorted array
    return arr
