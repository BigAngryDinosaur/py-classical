from functools import lru_cache
from typing import Generator


@lru_cache(maxsize=None)
def fib(n):
   if n < 2:
       return n
   return fib(n-1) + fib(n-2)

def fib_gen(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 1: yield 1
    prev: int = 0
    cur: int  = 1
    for _ in range(1, n):
        prev, cur = cur, prev + cur
        yield cur
