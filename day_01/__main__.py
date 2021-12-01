# pyright: reportMissingTypeStubs=false
""""""

import argparse
from pathlib import Path
from typing import TYPE_CHECKING

from aoc_io import download_input, submit_output
from .level_1 import day_01_level_1
from .level_2 import day_01_level_2

if TYPE_CHECKING:
    from typing import Literal

_INPUT_PATH = Path(__file__).resolve().parent / "input.txt"


def _main() -> None:
    """"""
    parser = argparse.ArgumentParser(description="AoC 2021 day 01")
    parser.add_argument("level", type=int, choices=(1, 2))
    args = parser.parse_args()

    download_input(1, _INPUT_PATH)

    level: Literal[1, 2] = args.level
    if level == 1:
        result = day_01_level_1()
    else:
        result = day_01_level_2()

    submit_output(1, level, result)


_main()
