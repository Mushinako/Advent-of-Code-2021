# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations


def solution(data: list[tuple[str, int]]) -> int:
    """
    Day 02 part 1 solution.
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
