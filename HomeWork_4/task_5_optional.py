"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


# >>> list(fizzbuzz(5))
# ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from itertools import cycle
from typing import List, Generator


def return_next(value):
    while True:
        a = cycle(
            [
                f"{value}",
                f"{i}",
                "fizz",
                f"{i}",
                "buzz",
                "fizz",
                f"{i}",
                f"{i}",
                f"{i}",
                "buzz",
                f"{i}",
                "fizz",
                f"{i}",
                f"{i}",
                "fizzbuzz",
            ]
        )
        value = yield next(a)


def fizzbuzz(n: int):

    for i in range(1, n + 1):
        yield next(a)


gen = fizzbuzz(32)
for i in range(1, 32):
    print(i, next(gen))
