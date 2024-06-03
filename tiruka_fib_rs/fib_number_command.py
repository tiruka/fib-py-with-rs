import argparse
from .tiruka_fib_rs import fib_number


def fib_number_command() -> None:
    parser = argparse.ArgumentParser(
        description="Print the Fibonacci number of a given index"
    )
    parser.add_argument(
        "--number",
        action="store",
        dest="number",
        type=int,
        required=True,
        help="Fibonacci number to calculate",
    )
    args = parser.parse_args()
    print(fib_number(args.number))
