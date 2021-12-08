# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations


def solution(data: list[tuple[list[frozenset[str]], list[frozenset[str]]]]) -> int:
    """
    Day 08 part 2 solution.
    """
    sum_ = 0
    for digits, values in data:
        digit_list: list[frozenset[str]] = [frozenset() for _ in range(10)]
        digit_map: dict[frozenset[str], int] = {}
        seg_length_map: dict[int, set[frozenset[str]]] = {
            5: set(),  # 2, 3, 5
            6: set(),  # 0, 6, 9
        }
        # Identify the easy digits
        for d in digits:
            len_ = len(d)
            if len_ == 2:
                digit_list[1] = d
                digit_map[d] = 1
            elif len_ == 3:
                digit_list[7] = d
                digit_map[d] = 7
            elif len_ == 4:
                digit_list[4] = d
                digit_map[d] = 4
            elif len_ == 7:
                digit_list[8] = d
                digit_map[d] = 8
            else:
                seg_length_map[len_].add(d)
        # Identify 0, 6, and 9
        for s6 in seg_length_map[6]:
            if len(s6 & digit_list[1]) == 1:
                digit_list[6] = s6
                digit_map[s6] = 6
            elif len(s6 & digit_list[4]) == 4:
                digit_list[9] = s6
                digit_map[s6] = 9
            else:
                digit_list[0] = s6
                digit_map[s6] = 0
        # Identify 2, 3, and 5
        for s5 in seg_length_map[5]:
            if len(s5 & digit_list[6]) == 5:
                digit_list[5] = s5
                digit_map[s5] = 5
            elif len(s5 & digit_list[1]) == 2:
                digit_list[3] = s5
                digit_map[s5] = 3
            else:
                digit_list[2] = s5
                digit_map[s5] = 2
        sub_sum = 0
        # Calculate sum
        for v in values:
            sub_sum *= 10
            sub_sum += digit_map[v]
        sum_ += sub_sum
    return sum_
