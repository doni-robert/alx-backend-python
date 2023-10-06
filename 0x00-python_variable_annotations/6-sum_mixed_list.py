#!/usr/bin/env python3
""" Contains a function sum_mixed_list """
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Sums up the number elements of a list

    Args:
        mxd_list(int | float): mixed list of integers and floats

    Return:
        the sum as a float
    """
    sum_numbers: float = 0
    for num in mxd_list:
        sum_numbers += num
    return sum_numbers
