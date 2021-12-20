# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

from typing import TYPE_CHECKING

from utils import SolutionAbstract

if TYPE_CHECKING:
    _Coord = tuple[int, int]
    _Data = tuple[list[int], list[list[int]]]


class Solution(SolutionAbstract):
    day = 20
    data: _Data

    def __init__(self) -> None:
        super().__init__()
        self.algo, self.pic = self.data

    @staticmethod
    def _process_data(raw_data: list[str]) -> _Data:
        """
        Process day 20 data.
        """
        algo = [0 if char == "." else 1 for char in raw_data[0]]
        pic = [[0 if char == "." else 1 for char in row] for row in raw_data[1:]]
        return algo, pic

    def part_1(self) -> ...:
        """
        Day 20 part 1 solution.
        """
        return self._solution(2)

    def part_2(self) -> ...:
        """
        Day 20 part 2 solution.
        """
        return self._solution(50)

    def _solution(self, round_: int) -> int:
        """
        Generic solution.
        """
        if round_ % 2:
            raise ValueError(f"Round count {round_} must be an even number.")
        if self.algo[0] and self.algo[511]:
            raise ValueError(
                "This solution assumes that not both the first and last rules of the "
                "algorithm are lit."
            )

        # Parse data into set of lit coordinates
        lit: set[_Coord] = set()
        for i, row in enumerate(self.pic):
            for j, cell in enumerate(row):
                if cell:
                    lit.add((i, j))

        for _ in range(round_ // 2):
            # Get boundry for the next 2 rounds
            i_set: set[int] = set()
            j_set: set[int] = set()
            for i, j in lit:
                i_set.add(i)
                j_set.add(j)
            min_i = min(i_set) - 1
            max_i = max(i_set) + 1
            min_j = min(j_set) - 1
            max_j = max(j_set) + 1

            # 1st round
            lit = self._process_round(
                lit,
                default=0,
                offset=0,
                min_i=min_i,
                max_i=max_i,
                min_j=min_j,
                max_j=max_j,
            )

            # 2nd round. Keep in mind that everywhere else on the infinite board may be
            #   lit
            lit = self._process_round(
                lit,
                default=self.algo[0],
                offset=1,
                min_i=min_i,
                max_i=max_i,
                min_j=min_j,
                max_j=max_j,
            )

        return len(lit)

    def _process_round(
        self,
        lit: set[_Coord],
        *,
        default: int = 0,
        offset: int = 0,
        min_i: int,
        max_i: int,
        min_j: int,
        max_j: int,
    ) -> set[_Coord]:
        """
        Solution for one of the 2 rounds.
        """
        new_lit: set[_Coord] = set()
        for i in range(min_i - offset, max_i + offset + 1):
            for j in range(min_j - offset, max_j + offset + 1):
                num: int = 0
                for ni in range(i - 1, i + 2):
                    for nj in range(j - 1, j + 2):
                        num *= 2
                        if min_i <= ni <= max_i and min_j <= nj <= max_j:
                            num += (ni, nj) in lit
                        else:
                            num += default
                if self.algo[num]:
                    new_lit.add((i, j))
        return new_lit
