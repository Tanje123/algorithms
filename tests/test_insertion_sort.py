from unittest import TestCase

from algorithms.insertion_sort import InsertionSort


class TestSelectionSort(TestCase):
    def setUp(self):
        self._client = InsertionSort()

    def test_list_gets_sorted(self):
        self._client.append(5)
        self._client.append(12)
        self._client.append(1)
        self._client.append(6)
        self._client.append(94)
        self._client.append(1)
        self._client.append(6)
        self._client.append(83)
        assert self._client.get() == [1, 1, 5, 6, 6, 12, 83, 94]
