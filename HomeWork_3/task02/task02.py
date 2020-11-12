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


def fast_calculate(values: List[int], numb_of_threads=10) -> int:

    if numb_of_threads > len(values):
        numb_of_threads = len(values)

    total_sum_list = []

    def tread_calculate(*args):
        for val in args:
            total_sum_list.append(slow_calculate(val))

    tasks = {}
    values_ranges = []
    interval_of_values_range = int(len(values) / numb_of_threads) + 1

    for i in range(numb_of_threads):
        if values[i * interval_of_values_range : (i + 1) * interval_of_values_range]:

            values_ranges.append(
                values[
                    i * interval_of_values_range : (i + 1) * interval_of_values_range
                ]
            )
        else:
            break

    numb_of_threads = len(values_ranges)

    for i in range(numb_of_threads):
        tasks[i] = threading.Thread(target=tread_calculate, args=values_ranges[i])
        tasks[i].start()

    for i in range(numb_of_threads):
        tasks[i].join()

    return sum(i for i in total_sum_list)
