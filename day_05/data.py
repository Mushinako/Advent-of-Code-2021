# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

from typing import TYPE_CHECKING

from aoc_io import get_input_path

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Optional

    _Coord = tuple[int, int]
    _CoordPair = tuple[_Coord, _Coord]


def process_data(path: Optional[Path] = None) -> list[_CoordPair]:
    """
    Process day 05 data.
    """
    if path is None:
        path = get_input_path(5)
    with path.open("r") as f:
        data: list[_CoordPair] = []
        for line in f:
            datum = line.strip()
            if not datum:
                continue
            c1_str, c2_str = datum.split("->")
            c1: _Coord = tuple(int(n.strip()) for n in c1_str.strip().split(","))
            c2: _Coord = tuple(int(n.strip()) for n in c2_str.strip().split(","))
            data.append((c1, c2))
    return data
