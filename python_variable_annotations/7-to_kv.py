#!/usr/bin/env python3
"""
Module that defines a function that takes a string k and
an int OR float v as arguments and returns a tuple.
"""

def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """
    Returns a tuple containing the string k and the square of the float v.
    """
    return (k, v * v)