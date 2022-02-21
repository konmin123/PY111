from typing import Iterator

def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    print(n)
    return 0


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    a = 0
    b = 1
    if n == 1:
        return a
    if n == 2:
        return b
    for _ in range(2, n):
        a, b = b, a + b
    return b

    print(n)
    return b

print(fib_iterative(10))

def fib_generator(n: int) -> Iterator[int]:
    a = 0
    b = 1
    yield a
    yield b

    for _ in range(n-2):
        a, b = a, a + b
        yield b

print(fib_generator(10))
