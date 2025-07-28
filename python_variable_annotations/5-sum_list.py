#!/usr/bin/env python3
"""Module sum_list
Defines a function that returns the sum of a list of floats.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """Return the sum of all floats in the input list.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of all values in the list.
    """
    return sum(input_list)
