#!/usr/bin/env python3
""" Contains the 'task_wait_n' function """
import asyncio
from typing import List

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns 'wait_random' n times with the specified 'max_delay'

    Args:
        n(int): number of times to spawn
        max_delay(int): upper limit of the random delay time

    Return:
        a list of all the delays in ascending order
    """
    delays = await asyncio.gather(
            *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
            )

    return sorted(delays)
