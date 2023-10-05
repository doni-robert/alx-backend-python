#!/usr/bin/env python3
""" Contains the function to_kv """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of k and the square of v

    Args:
        k(str): a string
        v(int | float): a number

    Return:
        a tuple of k and the square of v
    """
    mytuple: str | float = (k, v * v)
    return mytuple
