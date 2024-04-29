#!/usr/bin/env python3
import asyncio
from random import randrange
"""
Module for a function that waits for a random delay
between 0 and max_delay
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that takes in an integer argument
    and return the random seconds it waits
    """
    wait = float(randrange(max_delay))
    await asyncio.sleep(wait)
    return wait
