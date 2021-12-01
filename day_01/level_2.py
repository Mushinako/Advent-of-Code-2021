# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations


def day_01_level_2(data: list[int]) -> int:
    """
    Day 01 level 2 solution.

    Args:
        data (list[int]): List of depths

    Returns:
        (int): Number of sliding windows depth sums that are larger than the previous
    """
    return sum(data[i + 3] > data[i] for i in range(len(data) - 3))
