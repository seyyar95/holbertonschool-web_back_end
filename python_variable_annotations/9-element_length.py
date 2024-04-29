#!/usr/bin/env python3
"""
Model that defines a type-annotated function element_length
"""


def element_length(lst: list[str]) -> list[int]:
    """
    Returns a list of integers representing the lengths of the strings in lst.
    """
    return [len(i) for i in lst]
