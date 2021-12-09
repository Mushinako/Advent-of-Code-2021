# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

from typing import TYPE_CHECKING

from aoc_io import get_input_path

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Optional


def process_data(path: Optional[Path] = None) -> list[list[int]]:
    """
    Process day 09 data.
    """
    if path is None:
        path = get_input_path(9)
    with path.open("r") as f:
        data = [[int(n) for n in d] for line in f if (d := line.strip())]
    return data
