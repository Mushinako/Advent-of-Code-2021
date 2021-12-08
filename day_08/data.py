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
) -> list[tuple[list[frozenset[str]], list[frozenset[str]]]]:
    """
    Process day 08 data.
    """
    if path is None:
        path = get_input_path(8)
    data: list[tuple[list[frozenset[str]], list[frozenset[str]]]] = []
    with path.open("r") as f:
        for line in f:
            datum = line.strip()
            if not datum:
                continue
            digits, value = datum.split("|")
            data.append(
                (
                    [frozenset(d) for d in digits.strip().split()],
                    [frozenset(v) for v in value.strip().split()],
                )
            )
    return data
