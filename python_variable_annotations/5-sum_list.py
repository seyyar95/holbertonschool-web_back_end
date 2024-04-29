#!/usr/bin/env python3
"""Model that defines a type-annotated function that takes a list"""


def sum_list(input_list: list[float]) -> float:
    """
    Returns the sum of the list of floats.
    """
    return sum(input_list)