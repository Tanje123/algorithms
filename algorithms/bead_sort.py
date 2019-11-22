class BeadSort:
    __bead_list = []
    __max_value = 0

    def sort(self, unsorted_list: list):
        self.__max_value = unsorted_list[0]
        for value in unsorted_list:
            if value > self.__max_value:
                self.__max_value = value
        self.__bead_list = unsorted_list
        return self.__sort()

    def __sort(self):
        falls = 0
        last_index = len(self.__bead_list) - 1
        for index, value in enumerate(self.__bead_list):
            if index == last_index and falls == 0:
                return self.__bead_list
            if index == last_index:
                return self.__sort()
            next_index = index + 1
            if self.__bead_list[index] > self.__bead_list[next_index]:
                value = self.__bead_list[index] - self.__bead_list[next_index]
                self.__bead_list[index] -= value
                self.__bead_list[next_index] += value
                falls += 1
