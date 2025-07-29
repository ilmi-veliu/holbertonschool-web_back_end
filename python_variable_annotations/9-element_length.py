#!/usr/bin/env python3
"""Module element_length
Provides a function that returns a list of tuples (sequence, length)
from any iterable of sequences.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with each element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequence-type elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        the original sequence and its length.
    """
    return [(i, len(i)) for i in lst]
