# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations


def solution(data: list[tuple[str, int]]) -> int:
    """
    Day 02 part 2 solution.
    """
    hori = depth = aim = 0
    for direction, distance in data:
        if direction == "forward":
            hori += distance
            depth += aim * distance
            continue
        if direction == "down":
            aim += distance
            continue
        if direction == "up":
            aim -= distance
            continue
    return hori * depth
