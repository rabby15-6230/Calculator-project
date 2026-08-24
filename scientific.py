"""Scientific operations built on top of the math standard library."""
import math


def power(base: float, exponent: float) -> float:
    return math.pow(base, exponent)


def sqrt(x: float) -> float:
    if x < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(x)


def log(x: float, base: float = math.e) -> float:
    if x <= 0:
        raise ValueError("Cannot take log of a non-positive number")
    return math.log(x, base)


def sin(x_radians: float) -> float:
    return math.sin(x_radians)


def cos(x_radians: float) -> float:
    return math.cos(x_radians)
