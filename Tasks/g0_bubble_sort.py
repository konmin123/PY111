from typing import List
from operator import lt, gt


def sort(container: List[int], ascending: bool = True, inplace: bool =True) -> List[int]:
    """
    Sort input container with bubble sort

    :param inplace:
    :param ascending:
    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if not inplace:
        container = container.copy()
    compare_operator = gt if ascending else lt
    offset = 1
    for _ in container:
        is_change = False
        for i in range(len(container) - offset):
            if compare_operator(container[i], container[i+1]):
                container[i], container[i+1] = container[i+1], container[i]
                is_change = True
        offset += 1
        if not is_change:
            break
    return container


if __name__ == '__main__':
    list_ = [3, 2, 1]
    sorted_copy = sort(list_, inplace=False)

    print(list_)
    print(sorted_copy)