# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

from statistics import median


def solution(data: list[int]) -> int:
    """
    Day 07 part 1 solution.
    """
    median_ = round(median(data))
    return sum(abs(n - median_) for n in data)
