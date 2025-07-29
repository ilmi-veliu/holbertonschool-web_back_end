#!/usr/bin/env python3
"""Module sum_mixed_list
Defines a function that returns the sum of a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of all numbers (int or float) in the list.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of all values as a float.
    """
    return sum(mxd_lst)
