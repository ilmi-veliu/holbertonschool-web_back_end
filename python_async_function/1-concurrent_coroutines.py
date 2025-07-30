#!/usr/bin/env python3
"""Module 1-concurrent_coroutines
Spawns multiple coroutines concurrently and returns their delays.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random



async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
