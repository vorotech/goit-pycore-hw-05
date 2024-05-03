"""Main module for task_2."""

import re

from decimal import Decimal
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[Decimal, None, None]:
    """
    A generator function that yields decimal numbers from a given text.

    Args:
        text (str): The input text.

    Yields:
        Decimal: The decimals extracted from the text.

    """
    for word in text.split():
        if re.match(r"\d+\.\d+", word):
            yield Decimal(word)

def sum_profit(text: str, func: Callable[[str], Decimal]) -> Decimal:
    """
    Returns the sum of numbers extracted from the text by generator function.

    Args:
        text (str): The input text.
        func (Callable[[str], Decimal]): The generator function.

    Returns:
        Decimal: The sum of numbers extracted from the text.
    """
    return sum(func(text))

def main():
    """Main function."""
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 i 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

if __name__ == "__main__":
    main()
