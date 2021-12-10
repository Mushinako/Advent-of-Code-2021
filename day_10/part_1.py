# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations


def solution(data: list[str]) -> int:
    """
    Day 10 part 1 solution.
    """
    pair_map = {"(": ")", "[": "]", "{": "}", "<": ">"}
    score_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
    sum_ = 0
    for line in data:
        stack: list[str] = []
        for char in line:
            if char in pair_map:
                stack.append(char)
            else:
                last_open = stack.pop()
                correct_char = pair_map[last_open]
                if char != correct_char:
                    sum_ += score_map[char]
                    break
    return sum_
