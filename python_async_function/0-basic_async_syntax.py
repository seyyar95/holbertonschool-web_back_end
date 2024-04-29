#!/usr/bin/env python3
"""
asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay (included and float value)
seconds and eventually returns it.
"""
import asyncio
from random import randrange


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that takes in an integer argument
    and return the random seconds it waits
    """
    wait = float(randrange(max_delay))
    await asyncio.sleep(wait)
    return wait
