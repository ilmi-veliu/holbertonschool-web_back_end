#!/usr/bin/env python3
"""Module make_multiplier
Provides a function that creates a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to apply.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the product.
    """
    return lambda x: x * multiplier
