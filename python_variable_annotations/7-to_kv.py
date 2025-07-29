#!/usr/bin/env python3

def to_kv(k :str ,  v :float) -> tuple:
    """Convert a string and a float to a tuple.

    Args:
        k (str): The string key.
        v (float): The float value.

    Returns:
        tuple: A tuple containing the string key and the square of the float value.
    """
    return (k, v ** 2)
