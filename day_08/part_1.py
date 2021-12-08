# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations


def solution(data: list[tuple[list[frozenset[str]], list[frozenset[str]]]]) -> int:
    """
    Day 08 part 1 solution.
    """
    return sum(len(v) in {2, 3, 4, 7} for _, values in data for v in values)
