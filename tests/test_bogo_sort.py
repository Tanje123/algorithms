from unittest import TestCase

from algorithms.bogo_sort import BogoSort


class TestBogoSort(TestCase):
    def setUp(self):
        self._numeric_unsorted_list = [3, 2, 1]
        self._client = BogoSort()

    def test_list_gets_sorted(self):
        assert self._client.sort(
            self._numeric_unsorted_list
        ) == [1, 2, 3]

    def test_sorted_list_stays_sorted(self):
        sorted_list = [1, 2, 3]
        assert self._client.sort(sorted_list) == self._client.sort(sorted_list)
