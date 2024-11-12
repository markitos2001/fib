import pytest

from fib import fibonacci_iterative, fibonacci_recursive;

from fib import fibonacci_iterative

def test_fib_9_is_34():
    assert fibonacci_iterative(9) == 34

def test_fib_negative_raise_error():
    with pytest.raises(ValueError):
        fibonacci_iterative(-1)

def test_fib_9_is_34_recursive():
    assert fibonacci_recursive(34) == 5702887