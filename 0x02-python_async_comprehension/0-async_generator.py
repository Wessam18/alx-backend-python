#!/usr/bin/env python3
""" import module"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Func doc"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
