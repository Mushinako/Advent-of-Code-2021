# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations


def solution(data: list[int]) -> int:
    """
    Day 01 part 2 solution.
    """
    return sum(data[i + 3] > data[i] for i in range(len(data) - 3))
