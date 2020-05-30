from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    def split_binary(left_border, right_border):
        middle = left_border + (right_border - left_border) // 2

        if arr[middle] == elem:
            if arr[middle - 1] != elem:
                return middle

        if left_border == right_border:
            return None

        if elem > arr[middle]:
            left_border = middle + 1
        else:
            right_border = middle - 1

        return split_binary(left_border, right_border)

    if elem < arr[0]:
        return None

    if elem > arr[-1]:
        return None

    left = 0  # левая граница
    right = len(arr) - 1  # правая граница

    return split_binary(left, right)
