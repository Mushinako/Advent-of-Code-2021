# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations


def solution(data: list[int]) -> int:
    """
    Day 01 part 1 solution.
    """
    return sum(data[i + 1] > data[i] for i in range(len(data) - 1))
