# test_merge_sort.py

import unittest
from merge_sort import merge_sort, merge

class TestMergeSort(unittest.TestCase):

  def test_empty_list(self):
    """Tests if an empty list is handled correctly."""
    self.assertEqual(merge_sort([]), [])

  def test_single_element_list(self):
    """Tests if a list with a single element is handled correctly."""
    self.assertEqual(merge_sort([5]), [5])

  def test_sorted_list(self):
    """Tests if a pre-sorted list is returned as-is."""
    data = [1, 2, 3, 4]
    self.assertEqual(merge_sort(data), data)

  def test_unsorted_list(self):
    """Tests if an unsorted list is sorted correctly."""
    data = [6, 5, 3, 1, 8, 7, 2, 4]
    sorted_data = sorted(data)
    self.assertEqual(merge_sort(data), sorted_data)

  def test_merge_sorted(self):
    """Tests if the merge function combines sorted lists correctly."""
    left = [1, 3, 5]
    right = [2, 4, 6]
    merged = merge(left, right)
    self.assertEqual(merged, [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
  unittest.main()