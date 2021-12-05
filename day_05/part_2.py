# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    _Coord = tuple[int, int]
    _CoordPair = tuple[_Coord, _Coord]


def solution(data: list[_CoordPair]) -> int:
    """
    Day 05 part 2 solution.
    """
    coord_count: defaultdict[_Coord, int] = defaultdict(lambda: 0)
    for (x1, y1), (x2, y2) in data:
        # Vertical
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                coord_count[(x1, y)] += 1
            continue
        # Horizontal
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                coord_count[(x, y1)] += 1
            continue
        # Get coordinate's relative positions for diagonals
        if x1 < x2:
            big_x = x2
            small_x = x1
            start_y = y1
        else:
            big_x = x1
            small_x = x2
            start_y = y2
        # Bottom-left to top-right
        if x1 - y1 == x2 - y2:
            for s in range(big_x - small_x + 1):
                coord_count[(small_x + s, start_y + s)] += 1
            continue
        # Top-left to bottom-right
        if x1 + y1 == x2 + y2:
            for s in range(big_x - small_x + 1):
                coord_count[(small_x + s, start_y - s)] += 1
            continue
    count_gt_1 = [n for n in coord_count.values() if n > 1]
    return len(count_gt_1)
