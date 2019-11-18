from typing import List


class BinarySearch:
    sorted_list = []

    def binary_search(self, sorted_list: List, key: any):
        """
        :param sorted_list: A sorted list where the key needs to be found.
        :param key: The key which needs to be found.
        :return: Index of the found key, if the key is not found -1 will be
        returned.
        """
        first_element = 0
        last_element = (len(sorted_list)) - 1
        self.sorted_list = sorted_list

        return self.__binary_search(
            first_element,
            last_element,
            key
        )

    def __binary_search(
            self,
            first_element: int,
            last_element: int,
            key: any
    ) -> int:
        pointer = int(round((first_element + last_element) / 2, 1))
        sub_list_size = (last_element-first_element)

        if last_element == -1 or sub_list_size == -1:
            return -1

        if self.sorted_list[pointer] == key:
            return pointer
        if key > self.sorted_list[pointer]:
            return self.__binary_search(pointer + 1, last_element, key)
        elif key < self.sorted_list[pointer]:
            return self.__binary_search(0, pointer - 1, key)

        return -1
