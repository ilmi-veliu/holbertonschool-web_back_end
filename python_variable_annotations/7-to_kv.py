#!/usr/bin/env python3
"""Module to_kv
Defines a function that returns a tuple with a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string and the square of the number as a float.

    Args:
        k (str): The string key.
        v (Union[int, float]): An int or float number to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string
        and the second element is the square of the number, as a float.
    """
    return (k, float(v ** 2))
