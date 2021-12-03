# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

from collections import Counter


def solution(data: list[str]) -> int:
    """
    Day 03 part 1 solution.
    """
    gamma_str = ""
    epsilon_str = ""
    for digits in zip(*data):
        counter = Counter(digits)
        common_order = counter.most_common()
        gamma_str += common_order[0][0]
        epsilon_str += common_order[-1][0]
    return int(gamma_str, 2) * int(epsilon_str, 2)
