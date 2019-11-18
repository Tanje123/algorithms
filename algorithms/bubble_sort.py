class BubbleSort:
    def sort(self, unsorted_list: list):
        last_index = len(unsorted_list) - 1
        return self.__sort(unsorted_list, last_index)

    def __sort(self, unsorted_list: list, last_index: int):
        swaps = 0
        for index, value in enumerate(unsorted_list):
            next_index = index + 1
            if index >= last_index:
                if swaps == 0:
                    return unsorted_list
                else:
                    return self.__sort(unsorted_list, last_index)
            if unsorted_list[index] > unsorted_list[next_index]:
                swap_value = unsorted_list[index]
                unsorted_list[index] = unsorted_list[next_index]
                unsorted_list[next_index] = swap_value
                swaps += 1
