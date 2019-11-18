class InsertionSort:
    __sorted_list = []

    def get(self):
        return self.__sorted_list

    def append(self, value: any):
        if self.__size() == 0:
            self.__sorted_list.append(value)
            return 0
        for index, found_value in enumerate(self.__sorted_list):
            if value <= found_value:
                self.__sorted_list = (
                        self.__sorted_list[0:index] +
                        [value] +
                        self.__sorted_list[index:]
                )
                break
        if value > self.__sorted_list[self.__size()-1]:
            self.__sorted_list.append(value)

    def __size(self):
        return len(self.__sorted_list)
