class HeapSort:
    __sorted_list = []

    def sort(self, unsorted_list: list):
        head = 0
        self.__create_max_heap(unsorted_list, head)
        return self.__sort(unsorted_list)

    def __sort(self, unsorted_list: list):
        last_index = len(unsorted_list) - 1
        if len(unsorted_list) == 0:
            return self.__sorted_list
        self.__swap(0, last_index, unsorted_list)
        self.__sorted_list.insert(0, unsorted_list[last_index])
        unsorted_list.pop(last_index)
        self.__create_max_heap(unsorted_list, 0)
        return self.__sort(unsorted_list)

    def __get_childeren(self, index: int):
        left_child = ((2 * index) + 1)
        right_child = ((2 * index) + 2)
        return left_child, right_child

    def __swap(self, first_index: int, second_index: int, unsorted_list: list):
        unsorted_list[first_index], unsorted_list[second_index] = (
            unsorted_list[second_index],
            unsorted_list[first_index]
        )

    def __get_parent(self, index: int):
        left_parent = ((index - 1) / 2)
        right_parent = ((index - 2) / 2)
        if index == 0:
            return 0
        if index % 2 == 0:
            """ Right node """
            return int(right_parent)
        elif index % 2 != 0:
            """ Left node """
            return int(left_parent)

    def __create_max_heap(self, unsorted_list: list, head: int):
        last_index = len(unsorted_list) - 1
        left_child, right_child = self.__get_childeren(head)
        if left_child > last_index:
            return
        if right_child > last_index:
            return
        if unsorted_list[left_child] > unsorted_list[head]:
            self.__swap(left_child, head, unsorted_list)
            parent = self.__get_parent(head)
            self.__create_max_heap(unsorted_list, parent)
        if unsorted_list[right_child] > unsorted_list[head]:
            self.__swap(right_child, head, unsorted_list)
            parent = self.__get_parent(head)
            self.__create_max_heap(unsorted_list, parent)
        self.__create_max_heap(unsorted_list, head + 1)
