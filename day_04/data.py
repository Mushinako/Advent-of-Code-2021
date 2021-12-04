# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

from typing import TYPE_CHECKING

from aoc_io import get_input_path

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Optional


def process_data(
    path: Optional[Path] = None,
) -> tuple[list[int], list[list[list[int]]]]:
    """
    Process day 04 data.
    """
    if path is None:
        path = get_input_path(4)
    with path.open("r") as f:
        numbers = [int(n) for n in next(f).split(",")]
        next(f)
        lines = f.readlines()
        boards: list[list[list[int]]] = []
        for board_count in range(len(lines) // 6):
            boards.append(
                [[int(n) for n in lines[6 * board_count + i].split()] for i in range(5)]
            )
    return numbers, boards
