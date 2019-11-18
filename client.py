from algorithms.binary_search import BinarySearch
from algorithms.bubble_sort import BubbleSort
from algorithms.insertion_sort import InsertionSort
from algorithms.selection_sort import SelectionSort


def setup_insertion():
    insertion_client.append(5)
    insertion_client.append(12)
    insertion_client.append(5)
    insertion_client.append(9)
    insertion_client.append(22)

binary_client = BinarySearch()
selection_client = SelectionSort()
bubble_client = BubbleSort()
insertion_client = InsertionSort()

sorted_list = [1, 2, 6]
value = binary_client.binary_search(sorted_list, 6)
print("Binary search: ")
print(value)  # 2
print()

unsorted_selection_list = [7, 3, 12, 2, 8, 1]
sorted_list = selection_client.sort(unsorted_selection_list)
print("Selection sort: ")
print(sorted_list)  # [1, 2, 3, 7, 8, 12]
print()

unsorted_bubble_list = [2, 6, 1, 9, 3, 5]
sorted_bubble_list = bubble_client.sort(unsorted_bubble_list)
print("Bubble sort: ")
print(sorted_bubble_list)  # [1, 2, 3, 5, 6, 9]
print()

setup_insertion()
print("Insertion sort: ")
print(insertion_client.get())  # [5, 5, 9, 12, 22]
print()
