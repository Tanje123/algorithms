from algorithms.binary_search import BinarySearch
from algorithms.bubble_sort import BubbleSort
from algorithms.selection_sort import SelectionSort

binary_client = BinarySearch()
selection_client = SelectionSort()
bubble_client = BubbleSort()

sorted_list = [1, 2, 6]
value = binary_client.binary_search(sorted_list, 6)
print(value)  # 2

unsorted_selection_list = [7, 3, 12, 2, 8, 1]
sorted_list = selection_client.sort(unsorted_selection_list)
print(sorted_list)  # [1, 2, 3, 7, 8, 12]

unsorted_bubble_list = [2, 6, 1, 9, 3, 5]
sorted_bubble_list = bubble_client.sort(unsorted_bubble_list)
print(sorted_bubble_list)  # [1, 2, 3, 5, 6, 9]
