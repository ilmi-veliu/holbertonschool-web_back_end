#!/usr/bin/env python3
"""Module wait_random
Asynchronous coroutine that waits for a random delay and returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay seconds and return it.

    Args:
        max_delay (int, optional): Maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
