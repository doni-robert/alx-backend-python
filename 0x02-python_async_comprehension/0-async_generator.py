#!/usr/bin/env python3
""" Contains the 'async_generator' function """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loops 10 times eash time asyncronously waiting 1 second then yielding
    a random number between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
