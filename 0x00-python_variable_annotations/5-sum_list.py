#!/usr/bin/env python3
""" Contains function sum_list """
from typing import Iterable


def sum_list(input_list: list[float]) -> float:
    """
    Adds up the floats from a list

    Args:
        input_list(list): the list of floats

    Return:
        The sum of the floats
    """
    sum_floats: float = 0
    for num in input_list:
        sum_floats += num
    return sum_floats
