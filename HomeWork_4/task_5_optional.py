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
['1', '2', 'fizz', '4', 'buzz']

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from itertools import cycle
from typing import Generator


def fizzbuzz(numb: int) -> Generator:
    def take_fizz_or_buzz() -> Generator:
        fizzes = cycle(["", "", "fizz"])
        buzzes = cycle(["", "", "", "", "buzz"])
        while True:
            yield next(fizzes) + next(buzzes)

    return (i[0] or str(i[1]) for i in zip(take_fizz_or_buzz(), range(1, numb + 1)))
