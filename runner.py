# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

import argparse
from importlib import import_module


def _main():
    parser = argparse.ArgumentParser(description="AoC 2021 day 01")
    parser.add_argument("day", type=int, choices=range(1, 26))
    parser.add_argument("level", type=int, choices=(1, 2))
    args = parser.parse_args()

    day_name = f"day_{args.day:>02}"
    day_module = import_module(f"{day_name}.main")
    day_func = getattr(day_module, day_name)
    day_func(args.level)


if __name__ == "__main__":
    _main()
