# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

import heapq
import math
from typing import TYPE_CHECKING

from utils import SolutionAbstract

if TYPE_CHECKING:
    _Coord = tuple[int, int]
    _Data = list[list[int]]


class Solution(SolutionAbstract):
    day = 15
    data: _Data

    @staticmethod
    def _process_data(raw_data: list[str]) -> _Data:
        """
        Process day 15 data.
        """
        return [[int(n) for n in line] for line in raw_data]

    def part_1(self) -> int:
        """
        Day 15 part 1 solution.
        """
        return self._solve(_Cave(self.data, 1, 1))

    def part_2(self) -> int:
        """
        Day 15 part 2 solution.
        """
        return self._solve(_Cave(self.data, 5, 5))

    def _solve(self, cave: _Cave) -> int:
        """
        Generic solution.
        """
        # Keep track of all the visited nodes
        visited: set[_Coord] = set()
        # Initiate the cave distances from start point. Set everywhere to infinity,
        #   except the start point, which has a value of 0
        distances: dict[_Coord, int | float] = {
            (r, c): math.inf
            for r in range(cave.last_row + 1)
            for c in range(cave.last_col + 1)
        }
        distances[(0, 0)] = 0
        target_coord = (cave.last_row, cave.last_col)

        # A heap is used so that we can get calculate the unvisited node with the
        #   smallest distance from start point first
        priority_queue: list[tuple[int, _Coord]] = [(0, (0, 0))]
        while target_coord not in visited:
            distance, coord = heapq.heappop(priority_queue)
            # No need to check a visied node twice
            if coord in visited:
                continue
            # This probably will never happen, because we already visited all the nodes
            #   with a smaller distance (because of `heappop`). Nevertheless, still nice
            #   to do it as a sanity check
            if distance > distances[coord]:
                continue

            r, c = coord
            # Get all possible nodes to go to
            valid_next_coords: set[_Coord] = set()
            if r != 0:
                valid_next_coords.add((r - 1, c))
            if r != cave.last_row:
                valid_next_coords.add((r + 1, c))
            if c != 0:
                valid_next_coords.add((r, c - 1))
            if c != cave.last_col:
                valid_next_coords.add((r, c + 1))

            for new_coord in valid_next_coords:
                new_distance = distance + cave[new_coord]
                # Skip if we already have a shorter distance
                if new_distance >= distances[new_coord]:
                    continue
                # Record the lowest distance
                distances[new_coord] = new_distance
                # Queue the neighbors for visiting
                heapq.heappush(priority_queue, (new_distance, new_coord))
            # Mark current node as visited
            visited.add(coord)

        # Makes linter happy
        return int(distances[target_coord])


class _Cave:
    """
    Custom 2D cave map that supports the duplication of original cave map.
    """

    def __init__(self, data: list[list[int]], r_dup: int, c_dup: int) -> None:
        self._data = data
        self._data_row_count = len(data)
        self._data_col_count = len(data[0])
        self.row_count = r_dup * self._data_row_count
        self.col_count = c_dup * self._data_col_count
        self.last_row = self.row_count - 1
        self.last_col = self.col_count - 1

    def __getitem__(self, coord: _Coord, /) -> int:
        if not isinstance(coord, tuple):
            raise TypeError(
                f"The cave position must be a pair of integers, not {type(coord).__name__}."
            )
        r, c = coord
        if not isinstance(r, int):
            raise TypeError(
                "The first coordinate of the cave position must be an integer, not "
                f"{type(r).__name__}."
            )
        if not isinstance(c, int):
            raise TypeError(
                "The second coordinate of the cave position must be an integer, not "
                f"{type(r).__name__}."
            )
        if r < 0 or c < 0:
            raise IndexError("Negative indices are not supported.")
        if r >= self.row_count:
            raise IndexError("The first coordinate is out of range.")
        if c >= self.col_count:
            raise IndexError("The second coordinate is out of range.")

        # Get the position in the original map, and add offset for row and column, and
        #   wrap overflows
        return (
            self._data[r % self._data_row_count][c % self._data_col_count]
            + r // self._data_row_count
            + c // self._data_col_count
            - 1
        ) % 9 + 1
