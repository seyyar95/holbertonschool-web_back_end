#!/usr/bin/env python3
"""
Module that defines a type-annotated funtion
"""
from typing import Callable


def make_multiplier(multipler: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the multiplier.
    """
    def mul(x: float) -> float:
        return x * multipler
    return mul
