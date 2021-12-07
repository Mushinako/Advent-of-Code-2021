# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

from math import inf


def solution(data: list[int]) -> int:
    """
    Day 08 part 2 solution.
    """
    min_ = min(data)
    max_ = max(data)
    min_fuel = inf
    for t in range(min_, max_):
        fuel = sum(abs(n - t) * (abs(n - t) + 1) // 2 for n in data)
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel
