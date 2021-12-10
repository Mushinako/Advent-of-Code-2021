# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

from statistics import median


def solution(data: list[str]) -> int:
    """
    Day 10 part 2 solution.
    """
    pair_map = {"(": ")", "[": "]", "{": "}", "<": ">"}
    score_map = {"(": 1, "[": 2, "{": 3, "<": 4}
    scores: list[int] = []
    for line in data:
        stack: list[str] = []
        for char in line:
            if char in pair_map:
                stack.append(char)
            else:
                last_open = stack.pop()
                correct_char = pair_map[last_open]
                # Broken line
                if char != correct_char:
                    break
        else:
            # All checked, no broken
            sub_total = 0
            for char in reversed(stack):
                sub_total *= 5
                sub_total += score_map[char]
            scores.append(sub_total)
    return int(median(scores))
