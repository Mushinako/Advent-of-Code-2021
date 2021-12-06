# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

import argparse
import webbrowser
from importlib import import_module

from aoc_io import download_input, submit_output

_PREPARATION_COMMANDS = {"e", "er", "prepare"}
_DOWNLOAD_COMMANDS = {"d", "dl", "download"}
_PRINT_COMMANDS = {"p", "pr", "print"}
_SUBMIT_COMMANDS = {"s", "sub", "submit"}


def _main() -> None:
    parser = argparse.ArgumentParser(description="AoC 2021 day 01")
    parser.add_argument(
        "command", choices=_DOWNLOAD_COMMANDS | _PRINT_COMMANDS | _SUBMIT_COMMANDS
    )
    parser.add_argument("day", type=int, choices=range(1, 26))
    parser.add_argument("part", type=int, choices=(1, 2), nargs="?")
    args = parser.parse_args()

    # Prepare
    if args.command in _PREPARATION_COMMANDS:
        webbrowser.open("https://adventofcode.com/2021")
        download_input(day=args.day)
        return

    # Download input
    if args.command in _DOWNLOAD_COMMANDS:
        download_input(day=args.day)
        return

    # Run and get solution
    if args.part is None:
        raise ValueError("No part number provided.")
    solution = _get_solution(args.day, args.part)
    if args.command in _PRINT_COMMANDS:
        print(f"Got solution {solution!r}")
    elif args.command in _SUBMIT_COMMANDS:
        submit_output(day=args.day, part=args.part, answer=solution)


def _get_solution(day: int, part: int) -> str | int:
    """"""
    dir_name = f"day_{day:>02}"
    data_module = import_module(f"{dir_name}.data")
    data_func = getattr(data_module, "process_data")
    data = data_func()
    solution_module = import_module(f"{dir_name}.part_{part}")
    solution_func = getattr(solution_module, "solution")
    return solution_func(data)


if __name__ == "__main__":
    _main()
