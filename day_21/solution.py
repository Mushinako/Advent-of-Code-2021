# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

from typing import TYPE_CHECKING

from utils import SolutionAbstract

if TYPE_CHECKING:
    _Data = tuple[int, int]


class Solution(SolutionAbstract):
    day = 21
    data: _Data

    def __init__(self) -> None:
        super().__init__()
        self.p1, self.p2 = self.data

    @staticmethod
    def _process_data(raw_data: list[str]) -> _Data:
        """
        Process day 21 data.
        """
        p1_str, p2_str = raw_data
        p1 = int(p1_str.split()[-1])
        p2 = int(p2_str.split()[-1])
        return p1, p2

    def part_1(self) -> int:
        """
        Day 21 part 1 solution.
        """
        curr_dice = 1
        roll_count = 0
        p1 = self.p1
        p2 = self.p2
        p1_score = p2_score = 0
        while True:
            for _ in range(3):
                p1 += curr_dice
                curr_dice = curr_dice % 10 + 1
            p1 = (p1 - 1) % 10 + 1
            roll_count += 3
            p1_score += p1
            if p1_score >= 1000:
                return p2_score * roll_count
            for _ in range(3):
                p2 += curr_dice
                curr_dice = curr_dice % 10 + 1
            p2 = (p2 - 1) % 10 + 1
            roll_count += 3
            p2_score += p2
            if p2_score >= 1000:
                return p1_score * roll_count

    def part_2(self) -> int:
        """
        Day 21 part 2 solution.
        """
        score_dist_map = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
        p1_win_count = p2_win_count = 0

        def part_2_round(
            weight: int,
            top: bool,
            *,
            p1: int,
            p2: int,
            p1_score: int,
            p2_score: int,
            # p1_rolls: list[int],
            # p2_rolls: list[int],
        ) -> None:
            """"""
            nonlocal p1_win_count, p2_win_count
            for roll1, roll1_weight in score_dist_map.items():
                # new_p1_rolls = p1_rolls + [roll1]
                new_p1 = (p1 + roll1 - 1) % 10 + 1
                new_p1_score = p1_score + new_p1
                new_p1_weight = weight * roll1_weight
                if new_p1_score >= 21:
                    p1_win_count += new_p1_weight
                    continue
                for roll2, roll2_weight in score_dist_map.items():
                    # new_p2_rolls = p2_rolls + [roll2]
                    new_p2 = (p2 + roll2 - 1) % 10 + 1
                    new_p2_score = p2_score + new_p2
                    new_p2_weight = new_p1_weight * roll2_weight
                    if new_p2_score >= 21:
                        p2_win_count += new_p2_weight
                        continue
                    if top:
                        print(roll1, roll2)
                    part_2_round(
                        new_p2_weight,
                        False,
                        p1=new_p1,
                        p2=new_p2,
                        p1_score=new_p1_score,
                        p2_score=new_p2_score,
                        # p1_rolls=new_p1_rolls,
                        # p2_rolls=new_p2_rolls,
                    )

        part_2_round(
            1,
            True,
            p1=self.p1,
            p2=self.p2,
            p1_score=0,
            p2_score=0,  # p1_rolls=[], p2_rolls=[]
        )
        return max(p1_win_count, p2_win_count)
