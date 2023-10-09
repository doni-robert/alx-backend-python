#!/usr/bin/env python3
""" Contains the 'task_wait_random' function """
import asyncio
from asyncio import Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task[float]:
    """
    Returns an asyncio.Task

    Args:
        max_delay(int): upper limit of the random delay time
    """
    return asyncio.create_task(wait_random(max_delay))
