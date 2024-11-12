import argparse
from functools import cache


def fibonacci_iterative(n: int) -> int:
    """
    Compute the n-th Fibonacci number.
    :param n: i-th Fibonacci number.
    :return: the n-th Fibonacci number.
    """
    if n < 0:
        raise ValueError("n must be greater or equal to zero.")
    if n < 2:
        return n;
    f0 = 0
    f1 = 1
    # 0 1 1 2 3 5 8 13 21 34 55
    for i in range(n - 1):  # es lo mismo que  for _ in range(n)
        suma = f0 + f1
        f0 = f1
        f1 = suma
    return suma


@cache
def fibonacci_recursive(n: int) -> int:
    """
    Compute the i-th Fibonacci number with recursive method.
    :param n: i-th Fibonacci number.
    :return: the i-th Fibonacci number.
    """
    if n < 0:
        raise ValueError("n must be greater or equal to zero.")
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('nth', type=int, help="Nth Fibonacci number.")
    args = args = parser.parse_args()

    result = fibonacci_iterative(args.nth)
    print(result)
