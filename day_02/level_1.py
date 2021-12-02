# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations


def day_02_level_1(data: list[tuple[str, int]]) -> int:
    """
    Day 02 level 1 solution.
    """
    hori = depth = 0
    for direction, distance in data:
        if direction == "forward":
            hori += distance
            continue
        if direction == "down":
            depth += distance
            continue
        if direction == "up":
            depth -= distance
            continue
    return hori * depth
