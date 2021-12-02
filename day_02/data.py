# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

from typing import TYPE_CHECKING

from aoc_io import get_input_path

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Optional


def process_data(path: Optional[Path] = None) -> list[tuple[str, int]]:
    """
    Process day 02 data.
    """
    if path is None:
        path = get_input_path(2)
    with path.open("r") as f:
        data: list[tuple[str, int]] = []
        for line in f:
            if line:
                a, b = line.split()
                data.append((a.lower(), int(b)))
    return data
