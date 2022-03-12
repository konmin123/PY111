from typing import List

def merge_func(sorted_left: list[int], sorted_right: list[int]) -> list[int]:
    i = 0
    j = 0
    new_list = []
    while True:
        if sorted_left[i] <= sorted_right[j]:
            new_list.append(sorted_left[i])
            if i + 1 < len(sorted_left):
                i += 1
            else:
                new_list += sorted_right[j:]
                break
        if sorted_left[i] > sorted_right[j]:
            new_list.append(sorted_right[j])
            if j + 1 < len(sorted_right):
                j += 1
            else:
                new_list += sorted_left[i:]
                break
    return new_list


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) == 1:
        return container

    middle_index = len(container) // 2
    left_part = sort(container[:middle_index])
    right_part = sort(container[middle_index:])

    return merge_func(left_part, right_part)

