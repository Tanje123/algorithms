class RadixSort:
    __size = 0
    __max_digit = 0
    __zero = []
    __one = []
    __two = []
    __three = []
    __four = []
    __five = []
    __six = []
    __seven = []
    __eight = []
    __nine = []

    def sort(self, unsorted_list: [int]):
        self.__max_digit = self.__get_max_digit(unsorted_list)
        self.__size = len(unsorted_list)
        last_index = self.__max_digit - 1
        return self.__sort(unsorted_list, last_index)

    def __get_value(self, result: int, index: int):
        size_of_value = len(str(result))
        value = str(result)
        if size_of_value < self.__max_digit:
            needed = self.__max_digit - size_of_value
            for x in range(0, needed):
                value = "0" + value
        return value[index]

    def __sort(self, unsorted_list: list, digit: int):
        if digit == -1:
            return unsorted_list
        for value in unsorted_list:
            number = self.__get_value(value, digit)
            if number == "0":
                self.__zero.append(value)
            elif number == "1":
                self.__one.append(value)
            elif number == "2":
                self.__two.append(value)
            elif number == "3":
                self.__three.append(value)
            elif number == "4":
                self.__four.append(value)
            elif number == "5":
                self.__five.append(value)
            elif number == "6":
                self.__six.append(value)
            elif number == "7":
                self.__seven.append(value)
            elif number == "8":
                self.__eight.append(value)
            elif number == "9":
                self.__nine.append(value)
        new_max_digit = digit - 1
        return self.__sort(self.__retrieve_value(), new_max_digit)

    def __get_max_digit(self, unsorted_list: [int]):
        biggest_digit = 0
        for value in unsorted_list:
            size = len(str(value))
            if size > biggest_digit:
                biggest_digit = size
        return biggest_digit

    def __retrieve_value(self):
        sorted_list = []
        for index, value in enumerate(self.__zero):
            sorted_list.append(value)
        for index, value in enumerate(self.__one):
            sorted_list.append(value)
        for index, value in enumerate(self.__two):
            sorted_list.append(value)
        for index, value in enumerate(self.__three):
            sorted_list.append(value)
        for index, value in enumerate(self.__four):
            sorted_list.append(value)
        for index, value in enumerate(self.__five):
            sorted_list.append(value)
        for index, value in enumerate(self.__six):
            sorted_list.append(value)
        for index, value in enumerate(self.__seven):
            sorted_list.append(value)
        for index, value in enumerate(self.__eight):
            sorted_list.append(value)
        for index, value in enumerate(self.__nine):
            sorted_list.append(value)
        self.__clear_buckets()
        return sorted_list

    def __clear_buckets(self):
        self.__zero.clear()
        self.__one.clear()
        self.__two.clear()
        self.__three.clear()
        self.__four.clear()
        self.__five.clear()
        self.__six.clear()
        self.__seven.clear()
        self.__eight.clear()
        self.__nine.clear()
