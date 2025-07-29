#!/usr/bin/env python3
"""Module element_length
Defines a function that maps each element of an iterable of sequences
to a tuple containing the element and its length.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples (element, length) for each element in the input.

    Args:
        lst (Iterable[Sequence]): An iterable of sequence-type elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of (element, length) pairs.
    """
    return [(i, len(i)) for i in lst]
