#!/usr/bin/env python3
""" Contains the function element_length """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Finds an element length
    """
    return [(i, len(i)) for i in lst]
