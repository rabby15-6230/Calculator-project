"""Scientific operations built on top of the math standard library."""
import math


def power(base: float, exponent: float) -> float:
    return math.pow(base, exponent)


def sqrt(x: float) -> float:
    if x < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(x)
