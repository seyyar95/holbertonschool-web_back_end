#!/usr/bin/env python3
import asyncio
from random import randrange
"""
Module for a function that waits for a random delay
between 0 and max_delay
"""

async def wait_random(max_delay: int = 10) -> float:
    wait = float(randrange(max_delay))
    await asyncio.sleep(wait)
    return wait
