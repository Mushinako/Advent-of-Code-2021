# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

from typing import TYPE_CHECKING

from aoc_io import get_input_path

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Optional


def process_data(path: Optional[Path] = None) -> list[str]:
    """
    Process day 03 data.
    """
    if path is None:
        path = get_input_path(3)
    with path.open("r") as f:
        data: list[str] = [d for line in f if (d := line.strip())]
    return data
