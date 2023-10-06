#!/usr/bin/env python3
""" Contains the make_multiplier function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multipier

    Args:
        multiplier(float): number to be multiplied with

    Return:
        A function that multiplies a float by the multiplier
    """
    def func(num: float) -> float:
        """
        Multiplies a float by a multiplier

        Args:
            num(float): the number to be multiplied with

        Return:
            The product of n and multiplier
        """
        return float(num * multiplier)

    return func
