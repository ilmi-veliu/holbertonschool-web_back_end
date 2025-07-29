from typing import Callable
def make_multiplier(multiplicer :float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a given multiplier.

    Args:
        multiplicer (float): The multiplier to apply.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the product.
    """
    return lambda x: x * multiplicer
