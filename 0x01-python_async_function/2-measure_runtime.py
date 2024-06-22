#!/usr/bin/env python3
""" Module documentation """

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """total time to execute"""
    start = time.time()
    await wait_n(n, max_delay)
    end = time.time()
    total = end - start

    return (total / n)
