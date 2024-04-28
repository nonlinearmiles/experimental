def merge_sort(data):
  """Sorts a list of data using the merge sort algorithm.

  Args:
      data: A list of sortable elements.

  Returns:
      A new list containing the elements of data sorted in ascending order.
  """
  if len(data) <= 1:
    return data
   
  mid = len(data) // 2
  left = merge_sort(data[:mid])
  right = merge_sort(data[mid:])

  return merge(left, right)

def merge(left, right):
  """Merges two sorted lists into a single sorted list.

  Args:
      left: A list of sorted elements.
      right: A list of sorted elements.

  Returns:
      A new list containing the elements of left and right merged in ascending order.
  """
  merged = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1

  merged += left[i:]
  merged += right[j:]

  return merged