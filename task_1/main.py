"""Main module for task_1."""

from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """
    Returns a callable function that calculates the Fibonacci sequence and stores results in cache.

    Returns:
        Callable: A function that calculates the Fibonacci sequence.
    """
    cache = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

def main():
    """Main function."""
    fib = caching_fibonacci()

    print(fib(10))
    print(fib(15))

if __name__ == "__main__":
    main()
