from random import choice, randint
from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    # if not container:
    #     return container
    #
    # middle_value = container[0]
    # left_list = sort([x for x in container if x < middle_value])
    # middle_list = [x for x in container if x == middle_value]
    # right_list = sort([x for x in container if x > middle_value])
    #
    # return left_list + middle_list + right_list

    def _sort(left_boarder, right_border):
        if left_boarder >= right_border:
            return None
        i, j = left_boarder, right_border

        pivot_index = randint(left_boarder, right_border)
        pivot = container[pivot_index]

        while i <= j:
            while container[i] < pivot:
                i += 1
            while container[j] > pivot:
                j -= 1

            if i <= j:
                container[i], container[j] = container[j], container[i]
                i += 1
                j -= 1

        _sort(left_boarder, j)
        _sort(i, right_border)


    _sort(0, len(container) - 1)
    return container
