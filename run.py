# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

import argparse
from importlib import import_module

from aoc_io import download_input, submit_output


def _main():
    parser = argparse.ArgumentParser(description="AoC 2021 day 01")
    parser.add_argument("command", choices=("dl", "sub"))
    parser.add_argument("day", type=int, choices=range(1, 26))
    parser.add_argument("part", type=int, choices=(1, 2), nargs="?")
    args = parser.parse_args()

    # Download input
    if args.command == "dl":
        download_input(day=args.day)
        return

    # Run and submit solution
    if args.command == "sub":
        if args.part is None:
            raise ValueError("No part number provided.")
        dir_name = f"day_{args.day:>02}"
        data_module = import_module(f"{dir_name}.data")
        data_func = getattr(data_module, "process_data")
        data = data_func()
        solution_module = import_module(f"{dir_name}.part_{args.part}")
        solution_func = getattr(solution_module, "solution")
        solution = solution_func(data)
        submit_output(day=args.day, part=args.part, answer=solution)


if __name__ == "__main__":
    _main()
