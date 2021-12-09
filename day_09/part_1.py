# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations


def solution(data: list[list[int]]) -> int:
    """
    Day 09 part 1 solution.
    """
    max_i = len(data) - 1
    max_j = len(data[0]) - 1
    sum_ = 0
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if i > 0 and cell >= data[i - 1][j]:
                continue
            if i < max_i and cell >= data[i + 1][j]:
                continue
            if j > 0 and cell >= data[i][j - 1]:
                continue
            if j < max_j and cell >= data[i][j + 1]:
                continue
            sum_ += cell + 1
    return sum_
