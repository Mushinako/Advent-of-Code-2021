# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations


def day_01_level_1(data: list[int]) -> int:
    """
    Day 01 level 1 solution.

    Args:
        data (list[int]): List of depths

    Returns:
        (int): Number of depths that are larger than the previous
    """
    return sum(data[i + 1] > data[i] for i in range(len(data) - 1))
