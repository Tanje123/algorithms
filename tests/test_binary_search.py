from unittest import TestCase

from binary_search import BinarySearch


class TestBinarySearch(TestCase):
    def setUp(self):
        self._numeric_list = [1, 2, 3, 4, 5, 6, 7, 8]
        self._client = BinarySearch()

    def test_get_correct_index(self):
        assert self._client.binary_search(self._numeric_list, 1) == 0
        assert self._client.binary_search(self._numeric_list, 8) == 7
        assert self._client.binary_search(self._numeric_list, 2) == 1

    def test_get_no_index_when_no_result(self):
        assert self._client.binary_search(self._numeric_list, 0) == -1
        assert self._client.binary_search(self._numeric_list, 11) == -1
