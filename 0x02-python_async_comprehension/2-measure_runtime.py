#!/usr/bin/env python3
""" Contains the 'measure_runtime' function"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes 'async_comprehension' four times in parallel
    """
    start_time = time.time()

    await asyncio.gather(*tuple(map(
        lambda _: async_comprehension(), range(4))))

    stop_time = time.time()

    return stop_time - start_time
