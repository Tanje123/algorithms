class CountingSort:
    __min_value = 0
    __max_value = 0

    def sort(self, unsorted_list: []):
        self.__min_value = unsorted_list[0]
        self.__max_value = unsorted_list[0]

        for value in unsorted_list:
            if value < self.__min_value:
                self.__min_value = value
            if value > self.__max_value:
                self.__max_value = value
        list_size = (self.__max_value - self.__min_value) + 1
        index_list = list(range(self.__min_value, self.__max_value + 1))
        count_list = [0] * list_size
        sum_count_list = [0] * list_size

        for value in unsorted_list:
            index = self.__get_index_position(value)
            count_list[index] += 1

        for index, value in enumerate(index_list):
            if index == 0:
                sum_count_list.insert(index, count_list[index])
                continue
            count_value = count_list[index]
            sum_count_value = sum_count_list[index-1]
            sum_count_list.insert(index, (count_value + sum_count_value))

        sorted_input = [0] * len(unsorted_list)

        for value in unsorted_list:
            index = self.__get_index_position(value)
            sum_count_val = (sum_count_list[index] - 1)
            sorted_input[sum_count_val] = value
            sum_count_list[index] -= 1
        return sorted_input

    def __get_index_position(self, value: int):
        return value - self.__min_value
