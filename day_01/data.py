# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

from typing import TYPE_CHECKING

from aoc_io import get_input_path

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Optional


def process_data(path: Optional[Path] = None) -> list[int]:
    """
    Process day 01 data.
    """
    if path is None:
        path = get_input_path(1)
    with path.open("r") as f:
        data = [int(cleaned_line) for line in f if (cleaned_line := line.strip())]
    return data
