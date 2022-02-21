from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence, left=None, right=None) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param right:
    :param left:
    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    mid = left + (right - left) // 2
    print(left, right, mid)

    if left > right:
        return None
    if arr[mid] == elem:
        return mid
    elif elem < arr[mid]:
        binary_search(elem, arr, left, mid - 1)
    else:
        binary_search(elem, arr, mid + 1, right)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(10, l))
