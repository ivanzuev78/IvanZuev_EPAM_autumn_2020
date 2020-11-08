import time
import struct
import random
import hashlib
import threading
from typing import List


def slow_calculate(value: int) -> int:
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def fast_calculate(values: List[int]) -> int:

    total_sum_list = []

    def tread_calculate(args):
        total_sum_list.append(slow_calculate(args))

    tasks = {}

    for i in range(len(values)):
        tasks[i] = threading.Thread(target=tread_calculate, args=[values[i]])
        tasks[i].start()

    for i in range(len(values)):
        tasks[i].join()

    return sum(total_sum_list)
