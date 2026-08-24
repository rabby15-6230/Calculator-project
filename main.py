"""Command-line interface for the scientific calculator."""
import argparse

from calculator import add, subtract, multiply, divide
from scientific import power, sqrt, log, sin, cos

OPS = {
    "add": add,
    "sub": subtract,
    "mul": multiply,
    "div": divide,
    "pow": power,
    "log": log,
    "sin": sin,
    "cos": cos,
}


def main():
    parser = argparse.ArgumentParser(description="Scientific calculator")
    parser.add_argument("op", choices=list(OPS.keys()) + ["sqrt"])  # sqrt kept as special-case
    parser.add_argument("values", type=float, nargs="+")
    args = parser.parse_args()

    if args.op == "sqrt":
        print(sqrt(args.values[0]))
    else:
        print(OPS[args.op](*args.values))


if __name__ == "__main__":
    main()
