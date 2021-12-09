# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations


def solution(data: list[list[int]]) -> int:
    """
    Day 09 part 2 solution.
    """
    max_i = len(data) - 1
    max_j = len(data[0]) - 1
    # Get the low points
    low_point_coords: list[tuple[int, int]] = []
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
            low_point_coords.append((i, j))
    # Calculate a basin size for each low point
    basin_sizes: list[int] = []
    for li, lj in low_point_coords:
        point_count = 1
        visited_coords: set[tuple[int, int]] = {(li, lj)}
        round_visited_coords: list[tuple[int, int]] = [(li, lj)]
        while round_visited_coords:
            # Expand outwards by 1
            this_round_coords: set[tuple[int, int]] = set()
            for vci, vcj in round_visited_coords:
                if vci > 0:
                    this_round_coords.add((vci - 1, vcj))
                if vci < max_i:
                    this_round_coords.add((vci + 1, vcj))
                if vcj > 0:
                    this_round_coords.add((vci, vcj - 1))
                if vcj < max_j:
                    this_round_coords.add((vci, vcj + 1))
            this_round_coords -= visited_coords
            # Check if we reached the edges
            this_round_visited_coords: list[tuple[int, int]] = []
            for rci, rcj in this_round_coords:
                if data[rci][rcj] == 9:
                    continue
                point_count += 1
                visited_coords.add((rci, rcj))
                this_round_visited_coords.append((rci, rcj))
            # Prepare next round
            round_visited_coords = this_round_visited_coords
        # Finished basin size calculation
        basin_sizes.append(point_count)
    # Get the 3 largest sizes
    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
