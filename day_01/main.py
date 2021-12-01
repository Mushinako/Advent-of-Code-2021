# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

from typing import TYPE_CHECKING

from aoc_io import download_input, submit_output
from .level_1 import day_01_level_1
from .level_2 import day_01_level_2
from .utils import INPUT_PATH

if TYPE_CHECKING:
    from typing import Literal


def day_01(level: Literal[1, 2]) -> None:
    """"""
    download_input(1, INPUT_PATH)
    with INPUT_PATH.open("r") as f:
        data = [int(cleaned_line) for line in f if (cleaned_line := line.strip())]

    result = day_01_level_1(data) if level == 1 else day_01_level_2(data)

    submit_output(1, level, result)
