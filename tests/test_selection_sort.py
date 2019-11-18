from unittest import TestCase

from algorithms.selection_sort import SelectionSort


class TestSelectionSort(TestCase):
    def setUp(self):
        self._numeric_unsorted_list = [11, 9, 24, 54, 2, 12, 834, 32]
        self._client = SelectionSort()

    def test_list_gets_sorted(self):
        assert self._client.sort(
            self._numeric_unsorted_list
        ) == [2, 9, 11, 12, 24, 32, 54, 834]

    def test_sorted_list_stays_sorted(self):
        sorted_list = [1, 2, 3]
        assert self._client.sort(sorted_list) == self._client.sort(sorted_list)
