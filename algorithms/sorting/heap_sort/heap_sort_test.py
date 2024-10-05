"""Tests for Heap Sort algorithm."""

import random

from heap_sort import heap_sort


def test_empty_list():
    """Test that an empty list returns an empty list."""
    assert heap_sort([]) == []


def test_single_element():
    """Test that a single element list returns the same single element."""
    assert heap_sort([7]) == [7]


def test_sorted_list():
    """Test that an already sorted list remains unchanged."""
    assert heap_sort([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]


def test_reverse_sorted_list():
    """Test that a reverse-sorted list is sorted correctly."""
    assert heap_sort([10, 8, 6, 4, 2]) == [2, 4, 6, 8, 10]


def test_duplicates():
    """Test that a list with duplicate elements is sorted correctly."""
    assert heap_sort([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]


def test_mixed_values():
    """Test that a list with mixed values is sorted correctly."""
    assert heap_sort([8, 1, 6, 4, 3]) == [1, 3, 4, 6, 8]


def test_negative_values():
    """Test that a list with negative values is sorted correctly."""
    assert heap_sort([-10, -30, -20, -50, -40]) == [-50, -40, -30, -20, -10]


def test_mixed_positive_and_negative_values():
    """Test that a list with both positive and negative values is sorted correctly."""
    assert heap_sort([-2, 4, -1, 5, -3]) == [-3, -2, -1, 4, 5]


def test_large_range():
    """Test that a list with a large range of values is sorted correctly."""
    assert heap_sort([100, -200, 0, 50, -100]) == [-200, -100, 0, 50, 100]


def test_small_range():
    """Test that a list with a small range of values is sorted correctly."""
    assert heap_sort([2, 1, 3, 0, 4]) == [0, 1, 2, 3, 4]


def test_all_same_elements():
    """Test that a list with all identical values is sorted correctly."""
    assert heap_sort([42] * 100) == [42] * 100


def test_random_large_list():
    """Test that a large randomly ordered list is sorted correctly."""
    random_list = random.sample(range(1000), 1000)
    sorted_list = sorted(random_list)
    assert heap_sort(random_list) == sorted_list


def test_random_small_list():
    """Test that a small randomly ordered list is sorted correctly."""
    random_list = random.sample(range(10), 10)
    sorted_list = sorted(random_list)
    assert heap_sort(random_list) == sorted_list
