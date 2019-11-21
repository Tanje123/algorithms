from random import shuffle


class BogoSort:
    """
    Educational sort, should not be used in real life.
    """
    def sort(self, unsorted_list: list):
        return self.__sort(unsorted_list)

    def __sort(self, unsorted_list: list):
        if self.__is_sorted(unsorted_list):
            return unsorted_list
        shuffled_list = unsorted_list
        shuffle(shuffled_list)
        return self.__sort(shuffled_list)

    def __is_sorted(self, check_list: list):
        last_index = len(check_list) - 1
        for index, value in enumerate(check_list):
            if index == 0:
                continue
            if check_list[index] < check_list[index-1]:
                return False
            if index == last_index:
                break
            if check_list[index] > check_list[index+1]:
                return False
        return True
