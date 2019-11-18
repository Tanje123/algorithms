class SelectionSort:
    __sorted_list = []

    def sort(self, unsorted_list: list):
        """
        Sort a list using selection sort.
        :param unsorted_list: List that is not sorted.
        :return: A sorted list.
        """
        self.__sorted_list.clear()
        return self.__sort(unsorted_list)

    def __sort(self, unsorted_list: list):
        if len(unsorted_list) == 0:
            return self.__sorted_list
        lowest_value = unsorted_list[0]
        lowest_value_index = 0
        for index, value in enumerate(unsorted_list):
            if value < lowest_value:
                lowest_value = value
                lowest_value_index = index
        self.__sorted_list.append(lowest_value)
        unsorted_list.pop(lowest_value_index)
        return self.__sort(unsorted_list)
