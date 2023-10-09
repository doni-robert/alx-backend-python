#!/usr/bin/env python3
"""Contains the asynchronous coroutine 'wait_random' """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> int | float:
    """
    Returns the argument after a random delay

    Args:
        max_delay(int): the integer argument

    Return:
        the integer 'max_delay'
    """
    rand: int | float = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
