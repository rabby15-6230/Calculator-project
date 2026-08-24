"""Quick manual sanity checks for the calculator (not pytest, just illustrative)."""
from calculator import add, subtract, multiply, divide
from scientific import power, sqrt, log, sin, cos

assert add(2, 3) == 5
assert subtract(5, 2) == 3
assert multiply(4, 3) == 12
assert divide(10, 2) == 5
assert power(2, 3) == 8
assert sqrt(16) == 4
print("All manual checks passed")
