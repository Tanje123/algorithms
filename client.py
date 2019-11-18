from binary_search import BinarySearch
from selection_sort import SelectionSort

binary_client = BinarySearch()
selection_client = SelectionSort()

sorted_list = [1, 2, 6]
value = binary_client.binary_search(sorted_list, 6)
print(value)  # 2

unsorted_list = [7, 3, 12, 2, 8, 1]
sorted_list = selection_client.sort(unsorted_list)
print(sorted_list)  # [1, 2, 3, 7, 8, 12]
