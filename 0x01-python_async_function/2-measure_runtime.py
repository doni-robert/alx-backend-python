#!/usr/bin/env python3
""" Contains the 'measure_time' function """
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n

    Args:
        n(int): number of times to spawn
        max_delay(int): upper limit of the random delay time

    Return:
        total_time / n
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    stop_time = time.time()

    return (stop_time - start_time) / n
