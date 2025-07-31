#!/usr/bin/env python3
"""
Module 0-async_generator.py
"""
import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """        # ← 4 espaces
    Asynchronous generator that yields 10 random float numbers between 0 and 10.
    
    Waits 1 second asynchronously between each yield.
    
    Yields:
        float: Random number between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
