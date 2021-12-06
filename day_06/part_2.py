# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations


def solution(data: list[int]) -> int:
    """
    Day 06 part 2 solution.
    """
    counts = [0] * 9
    for d in data:
        counts[d] += 1
    for _ in range(256):
        mature_count = counts.pop(0)
        counts.append(mature_count)
        counts[6] += mature_count
    return sum(counts)
