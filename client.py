from algorithms.binary_search import BinarySearch
from algorithms.bubble_sort import BubbleSort
from algorithms.heap_sort import HeapSort
from algorithms.insertion_sort import InsertionSort
from algorithms.radix_sort import RadixSort
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
heap_client = HeapSort()
radix_client = RadixSort()

print("Binary search: ")
sorted_list = [1, 2, 6]
print("Input: " + str(sorted_list))
print("Value: 6")
value = binary_client.binary_search(sorted_list, 6)
print("Output: "+ str(value))  # 2
print()


print("Selection sort: ")
unsorted_selection_list = [7, 3, 12, 2, 8, 1]
print("Input: " + str(unsorted_selection_list))
sorted_list = selection_client.sort(unsorted_selection_list)
print("Output: " + str(sorted_list))  # [1, 2, 3, 7, 8, 12]
print()

unsorted_bubble_list = [2, 6, 1, 9, 3, 5]
print("Bubble sort: ")
print("Input: " + str(unsorted_bubble_list))
sorted_bubble_list = bubble_client.sort(unsorted_bubble_list)
print("Output: " + str(sorted_bubble_list))  # [1, 2, 3, 5, 6, 9]
print()

setup_insertion()
print("Insertion sort: ")
print("Input: [5, 12, 5, 9, 22]")
print("Output: " + str(insertion_client.get()))  # [5, 5, 9, 12, 22]
print()

unsorted_heap_list = [10, 42, 35, 33, 26, 19, 27, 10, 35, 44, 60, 1]
print("Heap sort: ")
print("Input: " + str(unsorted_heap_list))
print("Output: " + str(heap_client.sort(unsorted_heap_list)))
print()

unsorted_radix_list = [10, 15, 1, 60, 5, 100, 25, 50]
print("Radix sort: ")
print("Input: " + str(unsorted_radix_list))
print("Output: " + str(radix_client.sort(unsorted_radix_list)))
print()
